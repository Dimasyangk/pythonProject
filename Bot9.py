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

    def post(self):
        if self.current_state == self.A:
            self.current_state = self.B
            return 0
        elif self.current_state == self.B:
            self.current_state = self.C
            return 1
        else:
            raise KeyError

    def blame(self):
        if self.current_state == self.B:
            self.current_state = self.E
            return 2
        elif self.current_state == self.D:
            self.current_state = self.E
            return 6
        elif self.current_state == self.C:
            self.current_state = self.A
            return 5
        elif self.current_state == self.E:
            self.current_state = self.F
            return 7
        elif self.current_state == self.F:
            self.current_state = self.G
            return 8
        else:
            raise KeyError

    def sway(self):
        if self.current_state == self.C:
            self.current_state = self.D
            return 4
        elif self.current_state == self.B:
            self.current_state = self.D
            return 3
        elif self.current_state == self.G:
            self.current_state = self.C
            return 9

        else:
            raise KeyError


def main():
    state_machine = FSM()

    return state_machine


o = main()
print(o.post()) # 0
print(o.post()) # 1
print(o.sway()) # 4
print(o.blame()) # 6
print(o.blame()) # 7
print(o.blame()) # 8
print(o.sway()) # 9
print(o.blame()) # 5
print(o.post()) # 0
print(o.blame()) # 2