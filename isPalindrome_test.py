#!/usr/bin/env python3

from isPalindrome import isPalindrome

if __name__ == "__main__":
    print("should be True: " + str(isPalindrome("nostakaunisnaamasipisamaansinuakatson")))
    print("should be True: " + str(isPalindrome("12233221")))
    print("should be False: " + str(isPalindrome("10")))
    print("should be True: " + str(isPalindrome("121")))
    print("should be False: " + str(isPalindrome("-121")))
    print("should be True: " + str(isPalindrome("121")))