# Python Shell Runner

This library allows running shell commands from Python with shared environment.

Example:
```python
import ShellContext

env = {}
env["name"] = "Python"
ctx = ShellContext(env)
r = ctx.cmd("echo \"Hello, $name\"")
print(r.stdout, end="")
r=ctx.cmd("export name_length=$(echo $name | wc -m)")
print("{} has {} letters".format(env["name"], int(env["name_length"])-1))
```
Outputs:
```
Hello, Python
Python has 6 letters
```
