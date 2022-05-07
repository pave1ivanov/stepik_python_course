import json


class Classes:
    def __init__(self, classes):
        self.classes = classes

    def is_parent(self, parent, child):
        if child in self.classes:
            if parent in self.classes[child]:
                return True
            elif self.classes[child]:
                for prnt in self.classes[child]:
                    if self.is_parent(parent, prnt):
                        return True

    def count_children(self, parent):
        other_classes = list(self.classes.keys())
        other_classes.remove(parent)
        count = 1
        for another in other_classes:
            if self.is_parent(parent, another):
                count += 1
        return count


json_data = str(input())
data = json.loads(json_data)
data_dict = {}
for item in data:
    data_dict[item["name"]] = item["parents"]


classes = Classes(data_dict)
for cls in sorted(list(classes.classes.keys())):
    print(f"{cls} : {classes.count_children(cls)}")
