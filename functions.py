#!/usr/bin/env python3
# -*- coding: cp1252 -*-

def main():
    print_name()
    give_temp()
    if_test()
    give_temp()

def print_name():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    fullname = fname + " " + lname
    print("Your name is:", fullname)

def give_temp():
    print("temp is 88F"*3)

def if_test():
    result = input("is this true?(1 for true")
    if result == True:
        print("true")
    else:
        print("false")



main()