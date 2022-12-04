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

print(file_try.exists())
print(file_try.parent.name)
print(file_try.name)
