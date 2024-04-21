import unittest

from textnode import (
    TextNode,
    text_type_text, 
    text_type_bold, 
    text_type_code,
    text_type_italic
)

from inline_markdown import split_nodes_delimiter

class TestInlineMarkdwon(unittest.TestCase):
    def test_to_node(self):
        nodes = split_nodes_delimiter([TextNode("This is **bold** text", text_type_text)], "**", text_type_bold)
        expected = [TextNode("This is ", text_type_text), TextNode("bold", text_type_bold), TextNode(" text", text_type_text)]
        self.assertEqual(nodes, expected)

    def test_multiple_nodes(self):
        nodes = split_nodes_delimiter([TextNode("This is *italic text* and more *italic text*", text_type_text)], "*", text_type_italic)
        expected = [
            TextNode("This is ", text_type_text), 
            TextNode("italic text", text_type_italic), 
            TextNode(" and more ", text_type_text), 
            TextNode("italic text", text_type_italic)
        ]
        self.assertEqual(nodes, expected)

    def test_no_text_nodes(self):
        nodes = split_nodes_delimiter([TextNode("This is text", text_type_bold)], "**", text_type_bold)
        expected = [TextNode("This is text", text_type_bold)]
        self.assertEqual(nodes, expected)

    def test_raises_invalid(self):
        self.assertRaises(
            ValueError,
            split_nodes_delimiter, 
            [TextNode("I only `have one tag", text_type_text)], "`", text_type_code)

if __name__ == "__main__":
    unittest.main()
