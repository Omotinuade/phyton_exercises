
from pathlib import Path
fake_path = Path("C:/Kelloges/hello.txt")
cwd_path = Path.cwd() /"tinuade"
print(cwd_path)
#print("Parent -->", fake_path.parent)
#print(fake_path.parents)
#print(list(fake_path.parents))
#print("Anchor-->", fake_path.anchor)
#print("Name-->", fake_path.name)
#print("Stem-->", fake_path.stem)
#print("Suffix-->", fake_path.suffix)
cwd_path.mkdir(exist_ok=True)


new_file_path = cwd_path/"private.txt"
new_file_path.touch()

print(fake_path.exists())
print("Exist-", cwd_path.exists())
print("isfile- ", cwd_path.is_file())
print("isDir- ", cwd_path.is_dir())
print(cwd_path.stem)