class Classes:
    def __init__(self):
        self.classes = {}

    def add_class(self, cls, parents):
        if parents is None:
            parents = []
        self.classes[cls] = parents

    def is_parent(self, parent, child):
        if child in self.classes:
            if parent == child or parent in self.classes[child]:
                return True
            elif self.classes[child]:
                for prnt in self.classes[child]:
                    if self.is_parent(parent, prnt):
                        return True


classes = Classes()

for _ in range(int(input())):
    cls, *parents = input().replace(":", " ").split()
    classes.add_class(cls, parents)

for _ in range(int(input())):
    parent, child = input().split()
    if classes.is_parent(parent, child):
        print("Yes")
    else:
        print("No")
