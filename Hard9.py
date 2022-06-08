class FSM:
    def __init__(self):
        self.A = "A"
        self.B = "B"
        self.C = "C"
        self.D = "D"
        self.E = "E"
        self.F = "F"
        self.G = "G"

        self.start = self.A
        self.current_state = self.start

    def model(self):
        if self.current_state == self.A:
            self.current_state = self.B
            return 0
        elif self.current_state == self.D:
            return 7
        elif self.current_state == self.E:
            self.current_state = self.F
            return 8
        elif self.current_state == self.F:
            self.current_state = self.G
            return 9
        else:
            raise KeyError

    def grow(self):
        if self.current_state == self.A:
            self.current_state = self.G
            return 1
        elif self.current_state == self.B:
            self.current_state = self.C
            return 4
        elif self.current_state == self.C:
            self.current_state = self.D
            return 5
        else:
            raise KeyError

    def hop(self):
        if self.current_state == self.A:
            return 2
        elif self.current_state == self.D:
            self.current_state = self.E
            return 6
        else:
            raise KeyError

    def unite(self):
        if self.current_state == self.A:
            self.current_state = self.F
            return 3
        else:
            raise KeyError


def main():
    state_machine = FSM()

    return state_machine

o = main()
print(o.hop()) # 0
print(o.model()) # 3
print(o.grow()) # 5
print(o.grow()) # 0
print(o.model()) # 3
print(o.hop()) # 6
print(o.model()) # 7
print(o.model())