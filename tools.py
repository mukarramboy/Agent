import subprocess
import webbrowser


def open_url(args: str) -> str:
    """
    Open a URL in the default browser.
    Use this when the user wants to open a website (YouTube, Google, etc).
    """
    url = args

    try:
        webbrowser.open(url)
        return f"Opened URL: {url}"
    except Exception as e:
        return f"Error opening URL: {e}"


def run_command(args: str) -> str:
    """
    Run a shell command on the system.
    Use this for simple system commands like ls, pwd, git status.
    """
    command = args
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )
        return result.stdout or result.stderr or "Command executed"
    except Exception as e:
        return f"Command error: {e}"


def read_file(path: str):
    """
    Read the contents of a given relative file path.
    Use this when you want to see what's inside a file.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = file.read()
            return data
    except Exception as e:
        return f"Error: {str(e)}"


def write_file(path: str, data: str):
    """
    Write or edit a file at the given path with the provided content.
        Use this to create new code files or update existing ones.
    """
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(data)
            return f"Successfully wrote to {path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"
