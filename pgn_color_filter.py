import sys

if len(sys.argv)<5:
    raise Exception("Usage: python3 pgn_color_filter.py <input> <output> <color> <player>")

with open(sys.argv[1],"r") as f:
    text = f.read().splitlines()

out = ""
store = ""
putin = False
for line in text:
    if line.startswith("[Event "):
        if putin:
            out+=store
        print(store, putin)
        store = ""
        putin = False
    elif line.startswith("["+sys.argv[3].capitalize()):
        if sys.argv[4] in line:
            putin = True
    store+=line+"\n"
if putin:
    out+=store
with open(sys.argv[2],"w") as f:
    f.write(out)