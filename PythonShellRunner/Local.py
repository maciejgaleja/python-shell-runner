import CommandOutput
import subprocess


class Local:
    def __init__(self) -> None:
        pass

    def execute(self, cmd: str) -> CommandOutput.CommandOutput:
        new_cmd = cmd
        args = ["bash", "-c", cmd]
        r = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = r.stdout.decode("utf-8")
        stderr = r.stderr.decode("utf-8")
        return CommandOutput.CommandOutput(r.returncode, stdout, stderr)
