'''
You are given two string S1 and S2. Write a Python program to predict whether the strings
falls under anagram
'''

s1 ="race"
s2 ="care"

def check(s1, s2):
     
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
check(s1, s2)