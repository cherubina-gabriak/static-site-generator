import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "Paragraph text")
        self.assertEqual("HTMLNode(p, Paragraph text, None, None)", repr(node))

    def test_props_to_html(self):
        node = HTMLNode("a", "This is a link", None, {"target": "_blank", "href": "https://www.boot.dev"})
        html_props = node.props_to_html()

        self.assertEqual(" target=\"_blank\" href=\"https://www.boot.dev\"", html_props)

    def test_raises(self):
        node = HTMLNode("h1", "This is a title")
        self.assertRaises(NotImplementedError, node.to_html)

if __name__ == "__main__":
    unittest.main()
