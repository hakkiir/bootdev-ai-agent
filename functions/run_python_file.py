import sys
from os import path
from argparse import ArgumentParser
import subprocess
from functions.get_files_info import validate_path

def run_python_file(working_directory, file_path, args=None):
    try:
        valid_path, isvalid = validate_path(working_directory, file_path)
        if not isvalid:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not path.isfile(valid_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not valid_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = [sys.executable, valid_path]
        
        if args:
            command.extend(args)
        
        print(command)
        sp = subprocess.run(
            command,
            check=False,
            text=True,
            capture_output=True,
            timeout=30,
            cwd=path.dirname(valid_path),
        )

        outputstr = ""
        if sp.returncode != 0:
            outputstr += f'Process exited with code {sp.returncode}\n'
        if sp.stdout:
            outputstr += f"STDOUT:\n{sp.stdout}\n"
        if sp.stderr:
            outputstr += f"STDERR:\n{sp.stderr}\n"
        if not sp.stdout and not sp.stderr:
            outputstr += "No output produced\n"
        return outputstr
    except:
        return f"Error: executing Python file: {valid_path}"