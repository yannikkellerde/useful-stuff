import os,sys
from tqdm import tqdm

def get_all_files(target_dir,code_endings):
    all_stuff = os.listdir(target_dir)
    file_paths = []
    for stuff in all_stuff:
        target_path = os.path.join(target_dir,stuff)
        if os.path.isdir(target_path):
            file_paths.extend(get_all_files(target_path,code_endings))
        else:
            if "." in stuff and stuff.split(".")[-1] in code_endings:
                file_paths.append(target_path)
    return file_paths

def count_filled_lines(file_path):
    fl = 0
    with open(file_path, 'r') as f:
        for line in f.read().splitlines():
            if len(line.strip())>0:
                fl += 1
    return fl

target_dir = sys.argv[1]
if len(sys.argv) > 2:
    code_endings = sys.argv[2].split(",")
else:
    code_endings = ["py"]
files = get_all_files(target_dir, code_endings)

sammelo = []
for file_path in tqdm(files):
    fill_lines = count_filled_lines(file_path)
    sammelo.append((os.path.basename(file_path),fill_lines))

sammelo.sort(key=lambda x:x[1])
print("\n".join([f"{x[0]}\t{x[1]}" for x in sammelo]))
print(f"\nSum: {sum(x[1] for x in sammelo)}")