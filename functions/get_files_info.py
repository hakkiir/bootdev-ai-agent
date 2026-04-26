from os import path, listdir


def validate_path(working_directory: str, target_path: str) -> tuple[str, bool]:
    
    working_abspath = path.abspath(working_directory)
    target_path = path.normpath(path.join(working_abspath, target_path))
    
    valid_dir = path.commonpath([working_abspath, target_path]) == working_abspath

    return [target_path, valid_dir]


def get_files_info(working_directory: str, directory: str = ".") -> str :

    target_path, valid_dir = validate_path(working_directory, directory)

    if not valid_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not path.isdir(target_path):
        return f'Error: "{directory} is not a directory'
    
    val = ""
    for item in listdir(target_path):
        try:
            item_path = path.join(target_path, item)
            val += f"- {item}: file_size={path.getsize(item_path)} bytes, is_dir={path.isdir(path.join(item_path))}\n"
            print(val)
        except:
            return f"Error: error while reading contents"
    return val.strip()