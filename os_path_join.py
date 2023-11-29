import os

def join(path, *paths):
    if contains_absolute_path(path, *paths):
        raise ValueError("Absolute paths are not allowed as arguments")  

    return os.path.join(path, *paths)

def contains_absolute_path(path, *paths):
    parts = [path] + list(paths)
    return any(os.path.isabs(part) for part in parts)

