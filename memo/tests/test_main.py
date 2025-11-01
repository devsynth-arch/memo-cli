
import unittest
from unittest.mock import patch, MagicMock
import os
import json
import io
from memo.main import main

class TestMemo(unittest.TestCase):

    def setUp(self):
        self.test_storage_path = 'test_memo.json'
        self.patcher = patch('memo.storage.get_storage_path', return_value=self.test_storage_path)
        self.mock_get_storage_path = self.patcher.start()

    def tearDown(self):
        if os.path.exists(self.test_storage_path):
            os.remove(self.test_storage_path)
        self.patcher.stop()

    def test_save_and_list_commands(self):
        # Test saving a command
        with patch('sys.argv', ['memo', 'save', 'test', 'echo "hello"']):
            main()

        # Test listing commands
        with patch('sys.argv', ['memo', 'list']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                main()
                self.assertIn('test: echo "hello"', mock_stdout.getvalue())

    def test_search_command(self):
        with patch('sys.argv', ['memo', 'save', 'test', 'echo "hello"']):
            main()

        with patch('sys.argv', ['memo', 'search', 'test']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                main()
                self.assertIn('test: echo "hello"', mock_stdout.getvalue())

    def test_delete_command(self):
        with patch('sys.argv', ['memo', 'save', 'test', 'echo "hello"']):
            main()

        with patch('sys.argv', ['memo', 'delete', 'test']):
            main()

        with patch('sys.argv', ['memo', 'list']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                main()
                self.assertNotIn('test: echo "hello"', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
