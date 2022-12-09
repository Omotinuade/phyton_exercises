from pathlib import Path

new_dir = Path.cwd() / "new directory"
new_dir.mkdir(exist_ok=True)

nested_dir = new_dir / "folder_a" / "folder_b"
nested_dir.mkdir(parents=True, exist_ok=True)

file_path = [nested_dir / "file.txt",
             nested_dir / "private.img"]
# for file in file_path:
#    file.touch()

# file_path2 = [new_dir / "my_file.txt",
#             new_dir / "alone.vid"]
# for file in file_path2:
#   file.touch()

# for file in new_dir.iterdir():
#    print(file.name)

# for file in new_dir.glob("**/*.txt"):
#    print(file.name)

#source = new_dir / "alone.vid"
#destination = new_dir / "folder_a" / "alone.vid"
#source.replace(destination)

from pathlib import Path
import shutil
file_path = Path.home()/"my_folder/"
file_path.mkdir(exist_ok=True)
file = [file_path/"file1.txt",
        file_path/"file2.txt",
        file_path/"image1.png"]

for files in file:
    files.touch()

path = file_path/"images/"
path.mkdir(exist_ok=True)

source = file_path/"image1.png"
destination = path/"image1.png"
source.replace(destination)

file1_delete = file_path/"file1.txt"
file1_delete.unlink(missing_ok=True)

#my_folder_delete = Path.home()/"my_folder/"
#my_folder_delete.rmdir()

shutil.rmtree(file_path)


new_dir = Path.cwd



py_file = new_dir/"files_assignment.py"
py_file.touch()