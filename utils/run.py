import subprocess

def run_git_command(command, cwd=None):
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        result = e.output
    return result

def run_command_clone(command, cwd=None):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, cwd=cwd, text=True)
        return {"success": True, "output": output}
    except subprocess.CalledProcessError as e:
        return {"success": False, "error": e.output}