#!/usr/bin/python3
import re
print("Takes file that has numbers and words, and adds all the numbers.")
answer = input("What file?\n>")

#regex to match number
num_regex = (r"^*\d\.*\d\s")

#add numbers
with open (answer, "r") as file:
    lst = []
    for line in file:
        for num in line.split():
            try:
                num = float(num)
            except ValueError:
                None
            if type(num) == float:
                lst.append(num)
print(sum(lst))
        #if num == num_reg:
         #   print(num)
