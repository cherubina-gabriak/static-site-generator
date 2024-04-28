import shutil
import os
from copystatic import copy_file_tree

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copy_file_tree(dir_path_static, dir_path_public)

main()
