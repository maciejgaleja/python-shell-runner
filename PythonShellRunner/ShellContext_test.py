import unittest
import sys
import os
import ShellContext

class TestShellContext(unittest.TestCase):

    def setUp(self):
        self.env = {}
        self.ctx = ShellContext.ShellContext(self.env)

    def test_constructor(self):
        self.assertEqual(len(self.env), 0)

    def test_constructor_does_not_remove(self):
        env = {}
        env['a'] = 'b'
        ctx = ShellContext.ShellContext(env)
        self.assertEqual(len(env), 1)
        self.assertEqual(env['a'], 'b')

    def test_command_does_not_destroy(self):
        self.ctx.cmd('echo 123')
        self.assertEqual(len(self.env), 0)

    def test_command_append(self):
        self.ctx.cmd('export A=123')
        self.assertEqual(len(self.env), 1)
        self.assertEqual(self.env['A'], '123')
        self.assertEquals(int(self.env['A']), 123)
    
    def test_variable_case(self):
        self.ctx.cmd('export a=432; export A=1432')
        self.assertEqual(len(self.env), 2)
        self.assertEqual(self.env['a'], '432')
        self.assertEqual(self.env['A'], '1432')
        self.assertEquals(int(self.env['a']), 432)
        self.assertEquals(int(self.env['A']), 1432)

    def test_variable_injection(self):
        self.env['A'] = '32'
        self.ctx.cmd('export B=$(( $A * 2))')
        self.assertEqual(len(self.env), 2)
        self.assertEqual(int(self.env['B']), 64)

    def test_multi_word_variables(self):
        self.env['var'] = 'Lorem ipsum'
        r = self.ctx.cmd("export TOKEN=$(echo $var | awk '{print $1}')")
        print(r)
        self.assertEqual(len(self.env), 2, str(self.env))
        self.assertEqual(self.env['TOKEN'], 'Lorem')

    def test_stdout(self):
        r = self.ctx.cmd('echo Lorem ipsum')
        self.assertEqual(r.stdout, 'Lorem ipsum\n')

    def test_stdout_no_newline(self):
        r = self.ctx.cmd('echo -n Lorem ipsum')
        self.assertEqual(r.stdout, 'Lorem ipsum')

    