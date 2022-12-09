from pathlib import Path

#path = Path("C:/my_folder")
#path.mkdir(exist_ok=True)
#file_path = path / "my_file.txt"
#file_path.touch()


#print(file_path.exists())
#print(file_path.name)
#print(file_path.parent.name)

file_try = Path("C:/big_folder/onward.txt")
file_try.parent.mkdir()
file_try.touch()


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


print(file_try.exists())
print(file_try.parent.name)
print(file_try.name)
