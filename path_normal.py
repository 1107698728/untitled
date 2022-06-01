import os.path as osp
import sys

def absolute_path(*kwargs):
    base_dir = osp.dirname(__file__)
    lib_path = osp.join(base_dir, *kwargs)
    return lib_path

def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)