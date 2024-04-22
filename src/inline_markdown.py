import re
from textnode import (
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_link, 
    text_type_text, 
    text_type_image, 
    TextNode
)

text_node_markdown = {
    "**": text_type_bold,
    "*": text_type_italic,
    "`": text_type_code
}

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            nodes.append(old_node)
            continue
        
        splitted_text = old_node.text.split(delimiter)
        if len(splitted_text) % 2 == 0:
            raise ValueError("Invalid markdown syntax: no closing tag")
        for i in range(0, len(splitted_text)):
            if len(splitted_text[i]) == 0:
                continue
            if i % 2:
                nodes.append(TextNode(splitted_text[i], text_type))
            else: 
                nodes.append(TextNode(splitted_text[i], text_type_text))

    return nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)

        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        
        text = old_node.text
        for image in images:
            sections = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            text = sections[1]

        if text != "":
            new_nodes.append(TextNode(text, text_type_text))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        print("links:::", links)

        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        
        text = old_node.text
        for link in links:
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            text = sections[1]

        if text != "":
            new_nodes.append(TextNode(text, text_type_text))

    return new_nodes


def text_to_textnodes(text):
    textnodes = [TextNode(text, text_type_text)]
    textnodes = split_nodes_image(textnodes)
    textnodes = split_nodes_link(textnodes)
    for key in text_node_markdown:
        textnodes = split_nodes_delimiter(textnodes, key, text_node_markdown[key])
    return textnodes
