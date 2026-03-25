import os

from google.genai import types
def write_file(working_directory, file_path, content):
    try:
        abs_path = os.path.abspath(working_directory) 
        target_file = os.path.normpath(os.path.join(abs_path, file_path))
        valid_target_dir = os.path.commonpath([abs_path, target_file]) == abs_path



        if not valid_target_dir:
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
        
        
        if  os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'


        os.makedirs(os.path.dirname( abs_path), exist_ok = True)


        with open(target_file, 'w') as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

        

    except Exception as e:
        return f"Error writing file: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content in the file in the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                type=types.Type.STRING,
                description="file path to find the file, relative to working directory (default is working directory)"
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="content to be written in the file"
            )
        },
        required=["file_path", "content"]
    )
)