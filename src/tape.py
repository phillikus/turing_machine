from enum import Enum


class Direction(Enum):
    Left = 1
    Right = 2


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

    def read(self):
        if self.head_position < 0 or self.head_position > len(self._tape):
            raise Exception('Trying to read character at invalid position: ' + self.head_position)
        return self._tape[self.head_position]

    def get_tape(self):
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