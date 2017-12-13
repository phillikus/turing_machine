from direction import Direction

class Tape:
    def __init__(self, word, alphabet):
        self.alphabet = alphabet + "$#"
        self.__init_tape(word)
        self.head_position = 0

    def __init_tape(self, word):
        tape = "$";
        for char in (c for c in word if c in self.alphabet):
            tape += char
        tape += "#";
        self._tape = list(tape)

    def write(self, character):
        if self.head_position < 1 or character not in self.alphabet:
            return
        self._tape[self.head_position] = character

        last_item_index = len(self._tape) - 1
        if self.head_position == last_item_index:
            self._tape += '#'

    def read(self):
        if self.head_position < 0 or self.head_position > len(self._tape) - 1:
            raise Exception('Trying to read character at invalid position: ' + self.head_position)
        return self._tape[self.head_position]

    def get_tape(self):
        self._remove_trailing_sharps()
        return ''.join(self._tape)

    def move_head(self, direction):
        if direction == Direction.Right:
            self.head_position += 1
        elif direction == Direction.Left:
            self.head_position -= 1

        if self.head_position > len(self._tape) - 1:
            self._tape += '#'
        if self.head_position < 0:
            self.head_position = 0

    def get_length(self):
        return len(self._tape)

    def _remove_trailing_sharps(self):
        for i in range(len(self._tape) - 1, 1, -1):
            if self._tape[i] == '#' and self._tape[i-1] == '#':
                del self._tape[-1:]
            else:
                break
