from textnode import text_type_text, TextNode

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
