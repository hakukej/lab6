def mult(nums):
    res = 1
    for num in nums:
        res*=num
    print(f"The result of multiplication: {res}")
lst = [5, 4, 3, 1, 7]
mult(lst)
def str(string):
    lst = list(string)
    upper = 0
    lower = 0
    for letter in lst:
        if 64 < ord(letter) < 91:
            upper += 1
        else:
            lower += 1
    print(f"number of uppercase letters:{upper}; number of lowercase letter:{lower}")
str("AKerke")
def palin(string):
    if string == string[::-1]:
        print("Palindrom")
    else:
        print("not a palindrom")
palin("darad")

import time 
import math  
def delayed(number, delay):
    time.sleep(delay / 1000)  
    result = math.sqrt(number) 
    print(f"Square root of {number} after {delay} milliseconds is {result}")
delayed(25100, 2123)

def alltrue(tpl):
    a = False
    for elem in tpl:
        if elem == False:
            print("tuple is false")
            a = True    
    if a == False:
        print("tuple is true")
tpl = (True, True, True)
alltrue(tpl)
    