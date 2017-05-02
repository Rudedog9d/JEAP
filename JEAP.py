#!/usr/bin/env python3
import random

class JEAP():
    def __init__(self, key=1, start=1, end=None, key_func=lambda key, i: key + i, verbose=False):
        self.key = key
        self.start = start
        self.key_func = key_func
        self.verbose = verbose
        self.end = end

    @property
    def key_func(self):
        return self._key_func

    @key_func.setter
    def key_func(self, func):
        if not callable(func):
            raise ValueError("not a function: {}".format(func))
        self._key_func = func

    def get_next(self, key, index):
        '''
        Wrap the func call to do some error handling
        '''
        n = None
        try:
            n = self.key_func(key, index)
        except Exception as e:
            raise LookupError("An error occurred in {}: {}".format(self.key_func, e))
        if n < index:
            raise ValueError("wrong value returned from {}: {} < {}".format(self.key_func, n, index))
        return n

    def get_char(self):
        # return a random char in the printable range
        return chr(random.randint(32, 126))

    def print(self, *args, verbose=None):
        '''
        Verbose print, allows for easy debug mode or clean mode
        :param args: Things to print 
        :return: 
        '''
        if verbose or self.verbose:
            print(*args)

    def encrypt(self, text, key=None, start=None, key_func=None, verbose=False):
        '''
        Encrypt a string
        :param str text: Text to encrypt
        :param int key:  Key to decode
        :param function key_func: Optional function to return next key location. 
                                  Takes a two parameters, the key and the current index of the encrypted string
        :return: Encrypted String
        '''
        key = key or self.key
        start = start or self.start
        if key_func is not None:
            self.key_func = key_func
        # Fill return string with padding before the first char
        ret_str = "".join(self.get_char() for x in range(0, start - 1))

        for c in text:
            # Add the current letter to the string
            ret_str += c
            # Get length of string (current 1-based index)
            i = len(ret_str)
            # get the next key
            next = self.get_next(key, i)
            # Verbose print adding the character
            self.print(len(ret_str), c, next, ': ', c)

            while len(ret_str) != next:
                # Fill the return string until the location of the next char appears
                ret_str += self.get_char()
                # Print the char that was just added
                self.print(len(ret_str), c, next, ': ', ret_str[-1])
        if self.end:
            for i in range(0, self.end):
                ret_str += self.get_char()

        return ret_str

    def decrypt(self, text, key=None, start=None, key_func=None, verbose=False):
        '''
        Encrypt a string
        :param str text: Text to encrypt
        :param int key:  Key to decode
        :param function key_func: Optional function to return next key location. 
                              Takes a two parameters, the key and the current index of the encrypted string
        :return: 
        '''
        # init some variables
        key = key or self.key
        start = start or self.start
        if key_func is not None:
            self.key_func = key_func
        end = len(text) - self.end if self.end else len(text)

        # init some more variables
        i = 1
        next = start
        ret_str = ""
        # ret_str = text[i-1:i]  # get first letter

        for c in text:
            self.print(i, c, next, ': ', c, 'added={}  "{}"'.format(i == next, ret_str), verbose=verbose)
            if i == next:
                # Add the current letter to the string
                ret_str += c
                # Get the next key position - add one to index to account for current character
                next = self.get_next(key, i + 1)
            elif i >= end:
                break
            # increment location in the string
            i += 1
        return ret_str

def test(x,y):
    return x-y

if __name__ == '__main__':
    jeap = JEAP(key=5, start=20, verbose=False)
    TEXT = "Jodah Encryption Algorithm in Python"
    print("Encrypting:\n\n{}\n\n".format(TEXT))
    ret = jeap.encrypt(TEXT, verbose=False)
    print(ret, '\n\n')
    print("Decrypting:\n\n{}\n\n".format(ret))
    ret = jeap.decrypt(ret, verbose=False)
    print(ret)
