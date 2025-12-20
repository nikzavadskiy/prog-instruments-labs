import random
import string
import sys


alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
polybius_square = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'k'],
    ['l', 'm', 'n', 'o', 'p'],
    ['q', 'r', 's', 't', 'u'],
    ['v', 'w', 'x', 'y', 'z']
]
DEBUG = True


def get_key_stream(key, text):
    """
    Generate a keystream for the Vigenere cipher.
    """
    key_stream = []
    ki = 0
    for i in range(len(text)):
        if text[i].isalpha():
            key_stream.append(key[ki % len(key)])
            ki += 1
        else:
            key_stream.append(text[i])
    return key_stream


def encrypt_vigenere(text, key):
    """
    Encrypt text using the Vigenere cipher.
    """
    result = ""
    key_stream = getKeyStream(key, text)
    for i in range(len(text)):
        ch = text[i]
        if ch.islower():
            pi = alphabet.index(ch)
            ki = alphabet.index(key_stream[i].lower())
            ci = (pi + ki) % 26
            result += alphabet[ci]
        elif ch.isupper():
            pi = alphabet_upper.index(ch)
            ki = alphabet_upper.index(key_stream[i].upper())
            ci = (pi + ki) % 26
            result += alphabet_upper[ci]
        else:
            result += ch
    return result


def decrypt_vigenere(text, key):
    """
    Decrypt text encrypted with the Vigenere cipher.
    """
    result = ""
    key_stream = get_key_stream(key, text)
    for i in range(len(text)):
        ch = text[i]
        if ch.islower():
            ci = alphabet.index(ch)
            ki = alphabet.index(key_stream[i].lower())
            pi = (ci - ki) % 26
            result += alphabet[pi]
        elif ch.isupper():
            ci = alphabet_upper.index(ch)
            ki = alphabet.index(key_stream[i].lower())
            pi = (ci - ki) % 26
            result += alphabet[pi]
        else:
            result += ch
    return result


def find_in_square(ch):
    """
    Find coordinates of a character in the Polybius square.
    """
    if ch == 'j':
        ch = 'i'
    for i in range(5):
        for j in range(5):
            if polybius_square[i][j] == ch:
                return i + 1, j + 1
    return None, None


def encrypt_polybius(text):
    """
    Encrypt text using the Polybius square cipher.
    """
    res = ""
    for ch in text.lower():
        if ch.isalpha():
            r, c = findInSquare(ch)
            if r is not None:
                res += str(r) + str(c) + " "
        else:
            res += ch
    return res.strip()


def decrypt_polybius(code):
    """
    Decrypt a Polybius square encoded message.
    """
    res = ""
    parts = code.split()
    for p in parts:
        if p.isdigit() and len(p) == 2:
            r = int(p[0]) - 1
            c = int(p[1]) - 1
            if 0 <= r < 5 and 0 <= c < 5:
                res += polybius_square[r][c]
        else:
            res += p
    return res


def encrypt_caesar(text, shift):
    """
    Encrypt text using the Caesar cipher.
    """
    res = ""
    for ch in text:
        if ch.islower():
            i = alphabet.index(ch)
            res += alphabet[(i + shift) % 26]
        elif ch.isupper():
            i = alphabet_upper.index(ch)
            res += alphabet_upper[(i + shift) % 26]
        else:
            res += ch
    return res


def decrypt_caesar(text, shift):
    """
    Decrypt text encrypted with the Caesar cipher.
    """
    res = ""
    for ch in text:
        if ch.islower():
            i = alphabet.index(ch)
            res += alphabet[(i - shift) % 26]
        elif ch.isupper():
            i = alphabet_upper.index(ch)
            res += alphabet_upper[(i - shift) % 26]
        else:
            res += ch
    return res


def print_menu():
    """Print the command-line menu."""
    print("1 Vigenere encrypt")
    print("2 Vigenere decrypt")
    print("3 Polybius encrypt")
    print("4 Polybius decrypt")
    print("5 Caesar encrypt")
    print("6 Caesar decrypt")
    print("7 Exit")


def do_stuff():
    """
    Run the interactive command-line interface.
    """
    while True:
        print_menu()
        c = input("Choice:")
        if c == "1":
            t = input("Text:")
            k = input("Key:")
            print(encrypt_vigenere(t, k))
        elif c == "2":
            t = input("Text:")
            k = input("Key:")
            print(decrypt_vigenere(t, k))
        elif c == "3":
            t = input("Text:")
            print(encrypt_polybius(t))
        elif c == "4":
            t = input("Code:")
            print(decrypt_polybius(t))
        elif c == "5":
            t = input("Text:")
            s = int(input("Shift:"))
            print(encrypt_caesar(t, s))
        elif c == "6":
            t = input("Text:")
            s = int(input("Shift:"))
            print(decrypt_caesar(t, s))
        elif c == "7":
            break
        else:
            print("Wrong input")


def main():
    """
    Entry point of the program.
    """
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            test_vigenere()
            test_polybius()
        elif sys.argv[1] == "demo":
            autoDemo()
        else:
            do_stuff()
    else:
        do_stuff()


if __name__ == "__main__":

    main()

