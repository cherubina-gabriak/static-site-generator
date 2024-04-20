import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

class TestTexyNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold))
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", text_type_italic)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", text_type_text)
        self.assertIsNone(node.url)

    def test_property(self):
        node = TextNode("This is a text node", text_type_code)
        self.assertIs(node.text_type, text_type_code)



if __name__ == "__main__":
    unittest.main()
