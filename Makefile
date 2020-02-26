test:
	coverage run --source PythonShellRunner setup.py test
	coverage report -m
	coverage html