from pathlib import Path
import shutil

file_path = Path.home() / "my_folder/"
file_path.mkdir(exist_ok=True)
file = [file_path / "file1.txt",
     file_path / "file2.txt",
      file_path / "image1.png"]

for files in file:
   files.touch()

path = file_path / "images/"
path.mkdir(exist_ok=True)

source = file_path / "image1.png"
destination = path / "image1.png"
source.replace(destination)

file1_delete = file_path / "file1.txt"
file1_delete.unlink(missing_ok=True)
# my_folder_delete = Path.home()/"my_folder/"
# my_folder_delete.rmdir()

shutil.rmtree(file_path)

new_dir = Path(r"C:\Users\Tinuade\PycharmProjects\pythonProject\files_learning\new directory")
folder = new_dir / "images/"
folder.mkdir(exist_ok=True)

image = [new_dir / "folder_a" / 'folder_b' / "pic.png",
         new_dir / "folder_a" / 'folder_b' / "joe.img",
         new_dir / "folder_a" / 'folder_b' / "thicknu.gif",
         new_dir / "folder_a" / 'folder_b' / "C14.jpg", ]
for images in image:
    images.touch()

source = new_dir / "folder_a" / 'folder_b' / "pic.png"
destination = new_dir/"images"/"image1.png"
source.replace(destination)

source = new_dir / "folder_a" / 'folder_b' / "joe.img"
destination = new_dir/"images"/"image2.img"
source.replace(destination)

source = new_dir / "folder_a" / 'folder_b' / "thicknu.gif"
destination = new_dir/"images"/"image3.gif"
source.replace(destination)

source = new_dir / "folder_a" / 'folder_b' / "C14.jpg"
destination = new_dir/"images"/"image4.jpg"
source.replace(destination)
