import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestleafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "This is a link", {"target": "_blank", "href": "#", "id": "link" })
        html = node.to_html()

        expected = '<a target="_blank" href="#" id="link">This is a link</a>'

        self.assertEqual(html, expected)

    def test_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_no_tag(self):
        node = LeafNode(None, "This is raw text")
        html = node.to_html()
        self.assertEqual(html, "This is raw text")


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("p", [LeafNode("b", "bold text"), LeafNode(None, " and raw text"), LeafNode("i", "and italic")])
        expected = "<p><b>bold text</b> and raw text<i>and italic</i></p>"
        self.assertEqual(node.to_html(), expected)

    def test_nested_html(self):
        node = ParentNode("div", [ParentNode("div", [LeafNode("span", "i'm in nested div")])])
        expected = "<div><div><span>i'm in nested div</span></div></div>"
        self.assertEqual(node.to_html(), expected)

    def test_diff_nodes(self):
        node = ParentNode("div", [
            ParentNode("div", [LeafNode("span", "i'm in nested div")]), 
            LeafNode("span", "i'm direct div child"), 
            ParentNode("p", [LeafNode(None, "i'm nested paragraph child")])
        ], {"class": "div"})
        expected = "<div class=\"div\"><div><span>i'm in nested div</span></div><span>i'm direct div child</span><p>i'm nested paragraph child</p></div>"
        self.assertEqual(node.to_html(), expected)

    def test_raises_empty(self): 
        node = ParentNode("div", None)
        self.assertRaises(ValueError, node.to_html)

if __name__ == "__main__":
    unittest.main()
