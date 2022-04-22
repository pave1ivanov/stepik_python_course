def create(namespace, parent):
    data[namespace] = {"parent": parent, "vars": []}


def add(namespace, var):
    data[namespace]["vars"].append(var)


def get(namespace, var):
    if var in data[namespace]["vars"]:
        print(namespace)
    else:
        get(data[namespace]["parent"], var) if data[namespace]["parent"] else print(None)


n = int(input())

data = {
    "global": {"parent": None, "vars": []}
}

for _ in range(n):
    cmd, namespace, arg = input().split()
    globals()[cmd](namespace, arg)
