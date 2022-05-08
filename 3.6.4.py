from xml.etree import ElementTree


def get_children(root, level):
    scores[root.attrib["color"]] += level
    for child in root:
        get_children(child, level + 1)


root = ElementTree.fromstring(input())
scores = {
    "red": 0,
    "green": 0,
    "blue": 0
}
level = 1
get_children(root, level)
print(scores["red"], scores["green"], scores["blue"])
