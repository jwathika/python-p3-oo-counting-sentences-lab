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


# value = MyString()
# value.value = 123
