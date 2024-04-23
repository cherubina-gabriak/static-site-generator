import unittest

from markdown_blocks import (
    block_to_block_type, 
    block_type_heading, 
    markdown_to_blocks, 
    block_type_paragraph, 
    block_type_ordered_list,
    block_type_quote
)

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

    def test_block_to_block_type(self):
        heading = "## This is heading 2"
        self.assertEqual(block_to_block_type(heading), block_type_heading)
        ol = "1. First item\n2. Second item"
        self.assertEqual(block_to_block_type(ol), block_type_ordered_list)
        para = "1. First item\n2. Second item\n4. This is not third item"
        self.assertEqual(block_to_block_type(para), block_type_paragraph)
        quote = ">this is quote"
        self.assertEqual(block_to_block_type(quote), block_type_quote)
