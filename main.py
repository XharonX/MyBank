#!/usr/bin/python3
from bank import Bank, selection, menu
if __name__ == '__main__':
    while True:
        MyBank = Bank()
        menu()
        selection(input("Select a option: "))
