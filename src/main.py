import shutil
import os
from copystatic import copy_file_tree
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"

def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copy_file_tree(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, "./template.html", dir_path_public)

main()
