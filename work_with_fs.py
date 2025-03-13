import shutil
from pathlib import Path


def copy_files_recurs(src, destination):
    source = Path(src)
    dest = Path(destination)

    if source.is_dir():
        if not dest.exists():
            dest.mkdir(parents=True, exist_ok=False)
        for child in source.iterdir():
            copy_files_recurs(child, dest / child.name)        

    if source.is_file():
        if not dest.parent.exists():
            dest.parent.mkdir(parents=True, exist_ok=False)
        shutil.copy2(source, dest)
        return 



if __name__ == "__main__":
    source = '/home/unixsv/python_module_goit/goit-algo-hw-03/new_folder/'
    dest = '/home/unixsv/python_module_goit/goit-algo-hw-03/destination_folder'
    copy_files_recurs(source, dest)



# if not dest.exists():
#     dest.mkdir(mode=0o755, parents=True, exist_ok=False)





