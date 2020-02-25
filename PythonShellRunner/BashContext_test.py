import unittest
import sys
import os
import BashContext

class TestBashContext(unittest.TestCase):

    def test_constructor(self):
        env = {}
        ctx = BashContext.ShellContext(env)
        self.assertEqual(len(env), 0)

if __name__ == '__main__':
    unittest.main()
