#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if type(value) not in [str]:
            print('The value must be a string.')
        else:
            self._value = value

    def is_sentence(self):
        return True if self.value[-1] == '.' else False
    
    def is_question(self):
        return True if self.value[-1] == '?' else False
    
    def is_exclamation(self):
        return True if self.value[-1] == '!' else False
    
    def count_sentences(self):
        return len(re.split(r'[\.!?]+', self.value)) -1