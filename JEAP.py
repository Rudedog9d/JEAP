#!/usr/bin/env python3
class JEAP():
    @classmethod
    def get_char(cls):
        # todo: return a random char here
        return 'a'

    @classmethod
    def encrypt(cls, text, key, start=1, func=lambda key, i: key + i, verbose=False):
        '''
        Encrypt a string
        :param str text: Text to encrypt
        :param int key:  Key to decode
        :param function func: Optional function to return next key location. 
                              Takes a two parameters, the key and the current index of the encrypted string
        :return: 
        '''
        # Fill return string with padding before the first char
        ret_str = "".join(JEAP.get_char() for x in range(0, start - 1))

        # Verbose print, allows for easy debug mode or clean mode
        def v_print(*args):
            if verbose:
                print(len(ret_str), c, next, ': ', *args)

        for c in text:
            # Add the current letter to the string
            ret_str += c
            # get the next key
            next = func(key, len(ret_str))  # todo: do some error handling here on func() and ret val
            # Verbose print adding the character
            v_print(c)

            while len(ret_str) != next:
                # Fill the return string until the location of the next char appears
                ret_str += JEAP.get_char()
                # Print the char that was just added
                v_print(ret_str[-1])

        return ret_str

    @classmethod
    def decrypt(cls, text, key, func=lambda x: x):
        pass


if __name__ == '__main__':
    TEXT = "Jodah Encryption Algorithm in Python"
    print("Encrypting '{}'".format(TEXT))
    ret = JEAP.encrypt(TEXT, 1, verbose=False)
    print(ret)
