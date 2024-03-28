# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, input_list):
        answers = []

        for input in input_list:
            control = sorted([letter for letter in self.word])
            test = sorted([letter for letter in input])
            if control == test:
                answers += [input]
                
        return answers
