import unittest
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_with_empty_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_with_empty_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_tag_and_value_and_prop(self):
        node = LeafNode("a", "Google link", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Google link</a>")


if __name__ == "__main__":
    unittest.main()