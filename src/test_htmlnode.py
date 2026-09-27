import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_empty_htmlnode(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_one_prop(self):
        test_prop = {"prop": "value"}
        expected_str = " prop=\"value\""
        node = HTMLNode(props=test_prop)
        self.assertEqual(node.props_to_html(), expected_str)

    def test_props_to_html_with_multiple_props(self):
        test_props = {"prop1": "value1", "prop2": "value2"}
        expected_str = " prop1=\"value1\" prop2=\"value2\""
        node = HTMLNode(props=test_props)
        self.assertEqual(node.props_to_html(), expected_str)


if __name__ == "__main__":
    unittest.main()