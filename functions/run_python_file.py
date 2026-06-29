import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file that is passed in as an argument.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="This is the file path to the python file to be run",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="These are optional additional arguments that can be passed into the python function for added versatility."
            )
        },
    ),
)


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
        try:
            working_directory_abspath = os.path.abspath(working_directory)
            target_file = os.path.normpath(os.path.join(working_directory_abspath, file_path))

            target_dir_valid = os.path.commonpath([target_file, working_directory_abspath]) == working_directory_abspath

            if not target_dir_valid:
                return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            
            if not os.path.isfile(target_file):
                return f'Error: "{file_path}" does not exist or is not a regular file'
            
            if not file_path.endswith(".py"):
                return f'Error: "{file_path}" is not a Python file'
            

            command = ["python", target_file]

            if args:
                command.extend(args)

            completed_process = subprocess.run(command, cwd=working_directory_abspath, capture_output=True, text=True, timeout=30)


            output_message = ""
            if completed_process.returncode != 0:
                output_message += f"Process exited with code {completed_process.returncode}"
            if not completed_process.stdout and not completed_process.stderr:
                output_message += "No output produced"
            if completed_process.stdout:
                output_message += f"STDOUT: {completed_process.stdout}"
            if completed_process.stderr:
                output_message += f"STDERR: {completed_process.stderr}"

            return output_message
        
        except Exception as ex:
             return f"Error: executing Python file: {ex}"

