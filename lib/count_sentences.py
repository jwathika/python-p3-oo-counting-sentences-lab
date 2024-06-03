#!/usr/bin/env python3


class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        print("Setting..")
        return self.__value

    @value.setter
    def value(self, userin):
        if isinstance(userin, str):
            self.__value = userin
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self.__value.endswith("."):
            return True
        else:
            return False

    def is_question(self):
        if self.__value.endswith("?"):
            return True
        else:
            return False

    def is_exclamation(self):
        if self.__value.endswith("!"):
            return True
        else:
            return False

    def count_sentences(self):
        for character in ["!", "?"]:
            value = self.value.replace(character, ".")

        sentences = [single for single in value.split(".") if single]
        return len(sentences)


# value = MyString()
# value.value = 123
