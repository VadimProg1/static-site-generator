from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid ParentNode: No tag")
        elif self.children == None:
            raise ValueError("Invalid ParentNode: No children")
        children_html = ""
        for c in self.children:
            children_html += c.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        
        