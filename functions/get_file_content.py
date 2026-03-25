import os

from google.genai import types
def get_file_content(working_directory, file_path):
    try:
        abs_path = os.path.abspath(working_directory) 
        target_file = os.path.normpath(os.path.join(abs_path, file_path))
        valid_target_dir = os.path.commonpath([abs_path, target_file]) == abs_path



        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        MAX_CHARS = 10000

        with open(target_file, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
        


        

    except Exception as e:
        return f"Error listing files: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the file content to the declared MAX_CHARS in the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                type=types.Type.STRING,
                description="file path to find the file, relative to working directory (default is working directory)"
            )
        },
        required=["file_path"]
    )
)
