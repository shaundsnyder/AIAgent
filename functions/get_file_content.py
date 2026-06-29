import os
from config import MAX_CHARS
from google.genai import types

schema_get_content_info = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of a specific file that is passed as an arguement of the function.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to the file of interest.",
            ),
        },
    ),
)

def get_file_content(working_directory: str, file_path: str) -> str:
    try: 
        working_directory_abspath = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abspath, file_path))

        target_dir_valid = os.path.commonpath([target_file, working_directory_abspath]) == working_directory_abspath

        if not target_dir_valid:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file, "r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return file_content
        
    except Exception as ex:
        return f"Error: {str(ex)}"