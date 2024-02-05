import json, argparse
import os


def replacements_map():
    parser = argparse.ArgumentParser(description="Replace text in a file using a map")
    parser.add_argument("map", help="Path to the map file")
    parser.add_argument("file", help="Path to the file to replace text in")
    parser.add_argument(
        "--dry", action="store_true", help="Only print replaced file contents"
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recurse through directories and replace text in all files",
    )
    parser.add_argument(
        "-e",
        "--extensions",
        nargs="+",
        default=[],
        help="Only replace text in files with these extensions",
    )
    args = parser.parse_args()
    with open(args.map, "r") as f:
        replace_map = json.load(f)

    if os.path.isfile(args.file):
        filelist = [args.file]
    elif os.path.isdir(args.file):
        assert args.recursive, "Directory provided without --recursive flag"
        filelist = []
        for root, _dirs, files in os.walk(args.file):
            for file in files:
                if args.extensions:
                    if os.path.splitext(file)[-1] in args.extensions:
                        filelist.append(os.path.join(root, file))
                else:
                    filelist.append(os.path.join(root, file))
    else:
        raise ValueError("Invalid file path")

    for file in filelist:
        with open(file, "r") as f:
            text = f.read()

        for k, v in replace_map.items():
            text = text.replace(k, v)

        if args.dry:
            print(text)
        else:
            with open(file, "w") as f:
                f.write(text)
