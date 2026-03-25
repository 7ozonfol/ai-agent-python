import os 
import subprocess


from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_path = os.path.abspath(working_directory) 
        target_file = os.path.normpath(os.path.join(abs_path, file_path))
        valid_target_dir = os.path.commonpath([abs_path, target_file]) == abs_path

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not '.py' in file_path:
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]

        if args:
            command.extend(args)
        
        result= subprocess.run(command, text=True, timeout=30, capture_output=True)
        output=''
        if not result.returncode == 0:
            output += f'Process exited with code {result.returncode}'
        if result.stdout is None or result.stderr is None:
            output += f'no output produced'
        else:
            output += f'STDOUT: {result.stdout}, STDERR: {result.stderr}'
        
        return output

    except Exception as e:
        return f"Error runing file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a python file in the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                type=types.Type.STRING,
                description="file path to find the file in, relative to working directory (default  is working directory)"
            ),
            "args":types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="arguments to be sent with execuation"
            )
        },
        required=["file_path"]
    )
)