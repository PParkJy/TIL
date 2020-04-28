'''
I found out the count method while processing the string.
How to use the count method?

Version: python 3.7
Author: Jiyeon Park (wldus8677@gmail.com)
Last Update: 2020.04.27

Syntax>
1) str.count(value, start, end)
    -> value = string
    -> start = integer, default is 0
    -> end = integer, default is the end of the string

2) list.count(value)
    -> value = any type
'''

# string
ex1 = "Hello everyone"
print(ex1.count('e')) # print the number of times the value 'e' appears in the ex1 string
print(ex1.count('e',1,7)) #print the number of times the value 'e' appears in the ex1 string's index 1 ~7

# list
ex2 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(ex2.count(2)) #print the number of the times the value 2 appears in the ex2 list
ex2 = ["12",1,2,2]
print(ex2.count("1")) #result is 0 because the string "1" is the ex2's first entry "12"'s sub-entry not the ex2's entry
print(ex2.count(2,1,3)) #resiult is error because the argument of list.count() is one.

'''
Reference>
1) https://www.w3schools.com/python/ref_list_count.asp
'''



