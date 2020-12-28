import json
import os


def prettify():
    root_path = os.path.abspath(os.pardir)
    src_dir = os.path.join(root_path, "json")
    dest_dir = os.path.join(root_path, "prettified")

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for filename in os.listdir(src_dir):
        src_filepath = os.path.join(src_dir, filename)
        with open(src_filepath, "r") as fin:
            json_obj = json.load(fin)

        dest_filepath = os.path.join(dest_dir, filename)
        with open(dest_filepath, "w") as fout:
            json.dump(json_obj, fout, indent=2)


if __name__ == "__main__":
    prettify()
