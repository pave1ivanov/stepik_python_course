import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, i):
        super(LoggableList, self).append(i)
        self.log(str(i))


loggable_list = LoggableList([1, 2, 3])
loggable_list.append(3)
print(loggable_list)
