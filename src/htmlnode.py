class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        result_str = ""
        if self.props == None:
            return result_str

        for prop in self.props:
            prop_str = f" {prop}=\"{self.props[prop]}\""
            result_str += prop_str
        
        return result_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"