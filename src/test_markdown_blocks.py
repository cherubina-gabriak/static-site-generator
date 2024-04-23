import unittest

from markdown_blocks import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n\n* This is a list\n* with items"
        blocks = markdown_to_blocks(text)
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]
        self.assertEqual(blocks, expected)
