from setuptools import setup

import unittest
def test_suite():
    test_loader = unittest.TestLoader()
    ts = test_loader.discover('PythonShellRunner', pattern='*_test.py')
    return ts

setup(name='PythonShellRunner',
      version='0.0.0',
      description='Library that allows running shell commands from Python',
      url='',
      author='Maciej Galeja',
      author_email='maciej.galeja@outlook.com',
      license='MIT',
      packages=['PythonShellRunner'],
      test_suite='setup.test_suite',
      zip_safe=False)
