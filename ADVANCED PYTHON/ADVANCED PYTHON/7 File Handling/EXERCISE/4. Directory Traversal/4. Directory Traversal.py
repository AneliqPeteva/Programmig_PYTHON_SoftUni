import os


def generate_report(dir_path):
    file_info = {}

    for root, _, files in os.walk(dir_path):
        if root.count(os.path.sep) > dir_path.count(os.path.sep) + 1:
            continue
        for filename in files:
            file_ext = filename.split(".")[-1]
            if file_ext not in file_info:
                file_info[file_ext] = []
            file_info[file_ext].append(filename)

    sorted_file_info = {k: sorted(v) for k, v in sorted(file_info.items())}

    with open(os.path.join(dir_path, "report.txt"), "w") as file:
        for ext, files in sorted_file_info.items():
            file.write(f".{ext}\n")
            for f in files:
                file.write(f"- - - {f}\n")


generate_report(".")