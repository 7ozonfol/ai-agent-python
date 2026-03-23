import os

def get_files_info(working_directory, directory="."):
    abs_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_path, directory))
    valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    files_list = os.listdir(target_dir)

    record = ''
    for file in files_list:
        record += f'\n- {file}: file_size={os.path.getsize(os.path.join(target_dir,file))}, is_dir={os.path.isdir(os.path.join(target_dir,file))}'

    return record