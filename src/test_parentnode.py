import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_without_children(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_without_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_with_child_leaf_node(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_child_leaf_node_and_prop(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"href": "https://www.google.com"})
        self.assertEqual(parent_node.to_html(), "<div href=\"https://www.google.com\"><span>child</span></div>")

    def test_to_html_with_child_parent_node(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_child_parent_node_and_child_leaf_node(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node1 = ParentNode("span", [grandchild_node])
        child_node2 = LeafNode("i", "child")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span><i>child</i></div>",
        )


if __name__ == "__main__":
    unittest.main()