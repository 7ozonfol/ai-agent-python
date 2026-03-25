import os


from google.genai import types
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

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
        required=["directory"]
    ),
)