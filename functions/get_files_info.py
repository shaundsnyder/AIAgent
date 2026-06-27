import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_directory_abspath = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abspath, directory))

        target_dir_valid = os.path.commonpath([target_dir, working_directory_abspath]) == working_directory_abspath
        output_message = str("")


        if not target_dir_valid:
            output_message += f"Result for '{directory}' directory: \n"
            output_message += f"    Error: Cannot list \"{directory}\" as it is outside the permitted working directory"

            return output_message
        
        if not os.path.isdir(target_dir):
            return f"Error: \"{directory}\" is not a directory"

        if target_dir_valid:


            if directory == ".":
                output_message += "Result for current directory: \n"
            else:
                output_message += f"Result for '{directory}' directory: \n"

            sub_dir = os.listdir(target_dir)

            for sub in sub_dir:
                sub_path = os.path.join(target_dir,sub)
                output_message += f"  - {str(sub)}: file_size={os.path.getsize(sub_path)} bytes, is_dir={os.path.isdir(sub_path)}\n"

            return output_message
    except Exception as ex:
        return f'Error: {str(ex)}'