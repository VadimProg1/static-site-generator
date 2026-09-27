from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type: TextType = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node is None:
        raise ValueError("Failed convertion of TextNode to HTMLNode: TextNode is None")
    elif text_node.text_type not in TextType:
        raise ValueError("Failed convertion of TextNode to HTMLNode: TextNode.text_type has unknown value")
    
    result = LeafNode(None, text_node.text)
    
    match text_node.text_type:
        case TextType.BOLD:
            result.tag = "b"
        case TextType.ITALIC:
            result.tag = "i"
        case TextType.CODE:
            result.tag = "code"
        case TextType.LINK:
            result.tag = "a"
            result.props = {"href": text_node.url}
        case TextType.IMAGE:
            result.tag = "img"
            result.value = ""
            result.props = {"src": text_node.url, "alt": text_node.text}

    return result
    