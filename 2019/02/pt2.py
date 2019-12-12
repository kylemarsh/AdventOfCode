import sys

DEBUG = False


def main(args):
    initial_state = load_input(args[1])
    for noun in xrange(99):
        for verb in xrange(99):
            test_state = list(initial_state)
            test_state[1] = noun
            test_state[2] = verb
            prog = intcoder(test_state)
            prog.exec_all()
            result = prog.get_state()[0]
            if result == 19690720:
                print "noun=%s\nverb=%s" % (noun, verb)
                break
        else:
            continue
        break
    print prog.get_state()[0]


class intcoder:
    def __init__(self, initial_state):
        self.state = initial_state
        self.pc = 0
        self.hist = [initial_state]
        if DEBUG:
            print "Initial State: %s" % initial_state

    def exec_one(self):
        inst = self.state[self.pc]  # get current opcode
        if inst == 99:  # opcode 99 terminates program
            raise StopIteration("Halt Instruction Read")

        # All other opcodes specify tape locations for 2 operands and 1 output
        loc_a = self.state[self.pc+1]
        loc_b = self.state[self.pc+2]
        loc_out = self.state[self.pc+3]
        val_a = self.state[loc_a]
        val_b = self.state[loc_b]

        # Should dispatch here but whatever.
        if inst == 1:
            self.state[loc_out] = val_a + val_b
        elif inst == 2:
            self.state[loc_out] = val_a * val_b
        else:
            # Got an invalid opcode (valid opcodes are 1, 2, and 99)
            msg = "Invalid Opcode [%s]\nState is %s" % (inst, self.get_state())
            raise ValueError(msg)

        self.pc += 4
        self.hist.append(list(self.state))  # save history

    def exec_all(self):
        try:
            while(True):
                self.exec_one()
        except StopIteration:
            if DEBUG:
                print "Received StopIteration. State is: %s" % self.get_state()

    def history(self, i=None):
        if i is None:
            return self.hist
        else:
            return self.hist[i]

    def get_state(self):
        return self.state


def load_input(filename):
    infile = open(filename, "r")
    text = infile.read().strip()
    return [int(x) for x in text.split(",")]


if __name__ == "__main__":
    main(sys.argv)
