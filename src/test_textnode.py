import unittest
from textnode import TextNode, TextType
from textnode import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_text_node_to_html_node_with_none_text_node(self):
        self.assertRaises(ValueError, text_node_to_html_node, None)

    def test_text_node_to_html_node_with_unknown_text_type(self):
        node = TextNode("This is a text node", "unknown", "url")
        self.assertRaises(ValueError, text_node_to_html_node, node)

    def test_text_node_to_html_node_with_text_text_type(self):
        node = TextNode("This is a text node", TextType.TEXT, "url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, node.text)
        self.assertIsNone(html_node.props)

    def test_text_node_to_html_node_with_bold_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD, "url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, node.text)
        self.assertEqual(html_node.tag, "b")
        self.assertIsNone(html_node.props)

    def test_text_node_to_html_node_with_italic_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC, "url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, node.text)
        self.assertEqual(html_node.tag, "i")
        self.assertIsNone(html_node.props)

    def test_text_node_to_html_node_with_code_text_type(self):
        node = TextNode("This is a text node", TextType.CODE, "url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, node.text)
        self.assertEqual(html_node.tag, "code")
        self.assertIsNone(html_node.props)

    def test_text_node_to_html_node_with_link_text_type(self):
        node = TextNode("This is a text node", TextType.LINK, "url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, node.text)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": node.url})

    def test_text_node_to_html_node_with_image_text_type(self):
        node = TextNode("This is a text node", TextType.IMAGE, "url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": node.url, "alt": node.text})

    def test_eq_with_not_equal_nodes(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "url")
        node2 = TextNode("dummy", TextType.BOLD, "url")
        self.assertNotEqual(node1, node2)

        node1 = TextNode("This is a text node", TextType.BOLD, "url")
        node2 = TextNode("This is a text node", TextType.ITALIC, "url")
        self.assertNotEqual(node1, node2)

        node1 = TextNode("This is a text node", TextType.BOLD, "url")
        node2 = TextNode("This is a text node", TextType.BOLD, "not-url")
        self.assertNotEqual(node1, node2)

    def test_eq_with_equal_nodes(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

        node1 = TextNode("This is a text node", TextType.BOLD, "url")
        node2 = TextNode("This is a text node", TextType.BOLD, "url")
        self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()