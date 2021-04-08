import imaplib, time, json
import requests
import urllib.request
import shutil
import os
import subprocess
import traceback
import mailparser
if os.uname()[1]!="raspberrypi":
    from playsound import playsound

def get_audio(text,tofile="toplay.mp3"):
    url = "https://freetts.com/Home/PlayAudio"
    params = {
        "Language":"de-DE",
        "Voice":"Vicki_Female",
        "TextMessage":text,
        "id":"Vicki",
        "type":"1"
    }
    r = requests.get(url = url, params = params)
    data = r.json()
    print(data)
    if data["msg"] == "True":
        filename = data["id"]
        url = "https://freetts.com/audio/"+filename
        with urllib.request.urlopen(url) as response, open(tofile, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    else:
        raise RuntimeError("Invalid response from server.")

def clean_string(string):
    allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 üäöÜÄÖ"
    out_str = ""
    last_space = False
    for char in string:
        if char in allowed:
            last_space = False
            out_str += char
        else:
            if not last_space:
                last_space = True
                out_str+=" "
    return out_str

def check_clean(string):
    allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890üäöÜÄÖ_-,.#`!?'\"/& ()"
    for char in string:
        if char not in allowed:
            return False
    return True

class Mail():
    def __init__(self):
        with open("secrets.json","r") as f:
            secrets = json.load(f)
        self.user= secrets["user"]
        self.password= secrets["pass"]
        self.M = imaplib.IMAP4_SSL(secrets["server"], secrets["port"])
        self.M.login(self.user, self.password)
        self.known_ids = set()
        self.counter = 0
        
    def read_mail(self,id):
        typ, data = self.M.fetch(id, '(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                parts = mailparser.parse_from_bytes(response_part[1])
                if check_clean(parts._from[0][0]):
                    sender = clean_string(parts._from[0][0])
                else:
                    sender = clean_string(parts._from[0][1])
                to_speak = f"Neue Nachricht. Von {sender}. Betreff. {clean_string(parts.subject)}".replace(r"/\n/g", ' ')
                if len(to_speak) > 200:
                    print("Too long message, probably there is an error")
                    print(to_speak)
                    break
                filename = f"mail{self.counter}.mp3"
                self.counter += 1
                try:
                    get_audio(to_speak,tofile=filename)
                except RuntimeError as e:
                    print(e)
                    break
                if os.uname()[1]=="raspberrypi":
                    subprocess.call(["mplayer",filename],stdout=subprocess.DEVNULL)
                else:
                    playsound(filename, True)
                print("playing sound")

    def checkMail(self):
        self.M.select()
        self.unRead = self.M.search(None, 'UnSeen')
        id_list = self.unRead[1][0].split()
        for id in id_list:
            if not id in self.known_ids:
                try:
                    self.read_mail(id)
                except Exception as e:
                    traceback.print_exc()
                self.known_ids.add(id)
        
email = Mail()

# check for new mail every minute
while 1:
    print("Checking")
    try:
        email.checkMail()
    except Exception as e:
        traceback.print_exc()
    time.sleep(60)


"""
tts --text "Text for TTS" --model_name "tts_models/en/ek1/tacotron2" --vocoder_name "vocoder_models/en/ek1/wavegrad" --out_path test
"""