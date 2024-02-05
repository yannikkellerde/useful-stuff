import json, argparse


def replacements_map():
    parser = argparse.ArgumentParser(description="Replace text in a file using a map")
    parser.add_argument("map", help="Path to the map file")
    parser.add_argument("file", help="Path to the file to replace text in")
    parser.add_argument(
        "--dry", action="store_true", help="Only print replaced file contents"
    )
    args = parser.parse_args()
    with open(args.map, "r") as f:
        replace_map = json.load(f)

    with open(args.file, "r") as f:
        text = f.read()

    for k, v in replace_map.items():
        text = text.replace(k, v)

    if args.dry:
        print(text)
    else:
        with open(args.file, "w") as f:
            f.write(text)
