import unittest

from textnode import (
    TextNode,
    text_type_text, 
    text_type_bold, 
    text_type_code,
    text_type_italic,
    text_type_image,
    text_type_link
)

from inline_markdown import (
    extract_markdown_images, 
    extract_markdown_links, 
    split_nodes_image,
    split_nodes_link,
    split_nodes_delimiter,
    text_to_textnodes
)

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

    def test_images_match(self):
        matches = extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)")
        expected = [
            ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), 
            ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")
        ]        
        self.assertEqual(matches, expected)

    def test_links_match(self):
        matches = extract_markdown_links("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)") 
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")] 
        self.assertEqual(matches, expected)

    def test_split_image(self):
        nodes = split_nodes_image([TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)", text_type_text)])
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and ", text_type_text),
            TextNode("another", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")
        ]
        self.assertEqual(nodes, expected)

    def test_split_link(self):
        nodes = split_nodes_link([TextNode("This is text with a [link](https://www.example.com) and text after", text_type_text)])
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.example.com"),
            TextNode(" and text after", text_type_text),
        ]
        self.assertEqual(nodes, expected)
        
    def test_split_link_at_start(self):
        nodes = split_nodes_link([TextNode("[link](https://www.example.com) This is text with link", text_type_text)])
        expected = [
            TextNode("link", text_type_link, "https://www.example.com"),
            TextNode(" This is text with link", text_type_text),
        ]
        self.assertEqual(nodes, expected)

    def test_text_to_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected)

if __name__ == "__main__":
    unittest.main()
