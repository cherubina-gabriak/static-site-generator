from textnode import TextNode, split_nodes_delimiter, text_type_bold, text_type_text

def main():
    nodes = split_nodes_delimiter([TextNode("*This* is bold *text", text_type_text)], "*", text_type_bold)
    print("nodes::::", nodes)

main()
