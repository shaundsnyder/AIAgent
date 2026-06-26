import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
        try: 
            working_directory_abspath = os.path.abspath(working_directory)
            target_file = os.path.normpath(os.path.join(working_directory_abspath, file_path))

            target_dir_valid = os.path.commonpath([target_file, working_directory_abspath]) == working_directory_abspath

            if not target_dir_valid:
                return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            
            if os.path.isdir(target_file):
                return f'Error: Cannot write to "{file_path}" as it is a directory'
            
            os.makedirs(working_directory, exist_ok=True)

            with open(target_file, "w") as f:
                file_content = f.write(content)
                if file_content:
                    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as ex:
             return f"Error: {str(ex)}"
        
        
