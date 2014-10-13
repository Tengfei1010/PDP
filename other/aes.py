__author__ = 'kevin'
# -*- coding:utf-8 -*-
from Crypto import Random
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC
        self.iv = Random.new().read(AES.block_size)
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        length = 16
        count = len(text)
        if count < length:
            add = (length-count)
            #\0 backspace
            text += '\0' * add
        elif count > length:
            add = (length-(count % length))
            text += '\0' * add
        self.ciphertext = cryptor.encrypt(text)
        print(len(b2a_hex(self.ciphertext)))
        print(int(str(b2a_hex(self.ciphertext)), 16) % 100)
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')

if __name__ == '__main__':
    """
    pc = prpcrypt('keyskeyskeyskeys')
    import sys
    e = pc.encrypt(sys.argv[1])
    d = pc.decrypt(e)
    print "encrypt:", e
    print "decrypt:", d
    """
    print (b2a_hex(Random.new().read(AES.block_size)))