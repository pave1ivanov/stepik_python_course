class Classes:
    def __init__(self):
        self.classes = {}

    def add_class(self, cls, parents):
        if parents is None:
            parents = []
        self.classes[cls] = parents

    def is_parent(self, parent, child):
        if child in self.classes:
            if parent in self.classes[child]:
                return True
            elif self.classes[child]:
                for prnt in self.classes[child]:
                    if self.is_parent(parent, prnt):
                        return True


classes = Classes()

for _ in range(int(input())):
    cls, *parents = input().replace(":", " ").split()
    classes.add_class(cls, parents)

no_need_exceptions_list = []
exceptions_list = []
exceptions_list_len = int(input())
for i in range(exceptions_list_len):
    exception = input()
    exceptions_list.append(exception)
    if i > 0:
        for item in exceptions_list:
            if classes.is_parent(item, exception):
                if exception not in no_need_exceptions_list:
                    no_need_exceptions_list.append(exception)

for item in no_need_exceptions_list:
    print(item)
