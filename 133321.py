class Node:
    def __init__(self, data, link, next):
        self.data = data
        self.link = link
        self.next = next

    def find_next(self):
        for i in range(len(self.next)):
            if self.link[i] == self.data:
                return self.next[i]


def main(x):
    n8_2 = Node(8, [], [])
    n8_1 = Node(7, [], [])
    n8 = Node(x[0], ['CLEAN', 'FLUX'], [n8_1, n8_2])
    n3_2 = Node(10, [], [])
    n3_1 = Node(9, [], [])
    n3 = Node(x[2], ['LUA', 'APL', 'CSON'], [n8, n3_1, n3_2])
    n7_2 = Node(6, [], [])
    n7_1 = Node(5, [], [])
    n7 = Node(x[0], ['CLEAN', 'FLUX'], [n7_1, n7_2])
    n6_3 = Node(4, [], [])
    n6_2 = Node(3, [], [])
    n6_1 = Node(2, [], [])
    n6 = Node(x[2], ['LUA', 'APL', 'CSON'], [n6_1, n6_2, n6_3])
    n5_2 = Node(1, [], [])
    n5_1 = Node(0, [], [])
    n5 = Node(x[0], ['CLEAN', 'FLUX'], [n5_1, n5_2])
    n2 = Node(x[3], [1973, 1979, 2003], [n5, n6, n7])
    n_1 = Node (11, [], [])
    n = Node(x[1], ['URWEB', 'SHELL', 'HCL'], [n2, n3, n_1])

    while n:
        res = n
        n = n.find_next()

    return res.data


print(main(['CLEAN', 'SHELL', 'APL', 1979]))
print(main(['FLUX', 'URWEB', 'CSON', 2003]))
print(main(['CLEAN', 'HCL', 'CSON', 2003]))
print(main(['FLUX', 'URWEB', 'CSON', 1973]))
print(main(['CLEAN', 'URWEB', 'LUA', 1973]))
