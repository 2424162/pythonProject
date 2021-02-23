def haha():
    i =0
    return i
def haha1():
    i =0
    yield i

for i in range(1,20):
    print(haha1().__next__())
    print(haha())
