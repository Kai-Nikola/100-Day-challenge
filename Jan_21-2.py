from pathlib import Path

# Create Path object
path = Path("N:")
# print(my_path)
# print(path.iterdir())
path_list = [x for x in path.iterdir() if x.is_dir()]
path_list = [x for x in path.rglob("*.py")]

print(path_list)