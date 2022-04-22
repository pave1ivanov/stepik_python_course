class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        if self.capacity >= self.count + v:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.count += v
        else:
            print("Money box is too full. Try adding less.")


capacity = None
while capacity is None:
    try:
        capacity = int(input("Money box capacity: "))
    except ValueError:
        capacity = None
money_box = MoneyBox(capacity)

while True:
    user_input = input()
    if user_input == "exit":
        break
    else:
        money_box.add(int(user_input.split()[1]))
        print(f"In Money Box: {money_box.count}")
