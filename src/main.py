import shutil
import os
from copystatic import copy_file_tree
from generate_page import generate_page

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copy_file_tree(dir_path_static, dir_path_public)
    generate_page("./content/index.md", "./template.html", f"{dir_path_public}/index.html")

main()
