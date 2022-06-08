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
    n6_3 = Node(8, [], [])
    n6_2 = Node(7, [], [])
    n6_1 = Node(6, [], [])
    n6 = Node(x[0], ['CSON', 'M4', 'CIRRU'], [n6_1, n6_2, n6_3])
    n5_3 = Node (5, [], [])
    n5_2 = Node(4, [], [])
    n5_1 = Node(3, [], [])
    n5 = Node(x[4], ['R', 'PIKE', 'MUPAD'], [n5_1, n5_2, n5_3])
    n4_3 = Node(2, [], [])
    n4_2 = Node(1, [], [])
    n4_1 = Node(0, [], [])
    n4 = Node(x[0], ['CSON', 'M4', 'CIRRU'], [n4_1, n4_2, n4_3])
    n3 = Node(x[1], ['DM', 'VCL', 'R'], [n4, n5, n6])
    n2_2 = Node(10, [], [])
    n2_1 = Node(9, [], [])
    n2 = Node(x[3], [1965, 2002, 1981], [n3, n2_1, n2_2])
    n_1 = Node (11,[],[])
    n = Node(x[2], [2002, 2018], [n2, n_1])

    while n:
        res = n
        n = n.find_next()

    return res.data


if __name__ == "__main__":
    print(main(['M4', 'VCL', 2002, 1965, 'PIKE']),
          main(['CIRRU', 'DM', 2002, 1981, 'MUPAD']),
          main(['M4', 'DM', 2002, 2002, 'MUPAD']),
          main(['M4', 'R', 2018, 1965, 'R']),
          main(['CSON', 'R', 2002, 1965, 'PIKE']))