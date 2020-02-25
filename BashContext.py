from typing import Dict, Tuple
import random
import logging
import string
from CommandOutput import CommandOutput

import Local

def generate_magic_string()->str:
    return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))


class ShellContext:
    def __init__(self, env: Dict[str, str]) -> None:
        self.env = env
        self.env["forced"] = "value"
        self.conn = Local.Local()
        self.env_prefix = "ENV_"
    
    def get_environment(self, env: str) -> Dict[str, str]:
        ret = {}
        lines = env.split("\n")
        for line in lines:
            if len(line) > 0:
                key = line.split("=")[0].split(" ")[-1]
                if key.startswith(self.env_prefix):
                    value = None
                    try:
                        value = line.split("=")[1]
                    except:
                        pass
                    ret[key] = value
        return ret

    def cmd(self, command: str) -> CommandOutput:
        token_begin = generate_magic_string()
        token_mid = generate_magic_string()
        token_end = generate_magic_string()
        cmd = ""
        for item in self.env.items():
            cmd += "export {}{}=\"{}\";\n".format(self.env_prefix, item[0], item[1])
            # pass
        cmd += "echo " + token_begin + ";\n"
        cmd += "export;\n"
        cmd += "echo " + token_mid + ";\n"
        cmd += command + ";\n"
        cmd += "echo " + token_end + ";\n"
        cmd += "export;"
        
        r = self.conn.execute(cmd)
        env_str_begin = r.stdout[r.stdout.find(token_begin)+len(token_begin):r.stdout.find(token_mid)]
        env_begin = self.get_environment(env_str_begin)

        actual_stdout = r.stdout[r.stdout.find(token_mid)+len(token_mid):r.stdout.find(token_end)]

        env_str_end = r.stdout[r.stdout.find(token_mid)+len(token_mid):]
        env_end = self.get_environment(env_str_end)

        print(env_end)
        self.env = env_end
        print(self.env)

        return r


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG, format="%(relativeCreated)6d %(threadName)s %(message)s"
    )
    logging.info("Started")

    env = {}
    env["COUNTER"] = "999 777"
    ctx = ShellContext(env)

    print(env)
    rv = ctx.cmd("echo $ENV_COUNTER; export ENV_a=\"123\"")
    print(env)