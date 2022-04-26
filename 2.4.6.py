import os

py_dirs = []
for current_dir, dirs, files in os.walk("main"):
    for file in files:
        if ".py" in file:
            py_dirs.append(current_dir)
            break

with open("pydocs.txt", "w") as pydocs:
    pydocs.write("\n".join(sorted(py_dirs)))
