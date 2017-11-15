#import Python function tool to easily cache stored value (n) as fib sequence progresses.
#If we do not use a cache, then every time the recursion goes back to add the next n, it must recalculate all previous values of n behind it.
#After about 20 numbers, the program will slow way down and take a long time to compute the next n value. 
#The cache will store each n value after it computes it, so that when it does the function again, instead of having to compute back values, it has them stored.
#You can setup a cache manually, but importing the python cache tool is the quickest way to do it.
from functools32 import lru_cache

#define max cache vale (default size is 128, meaning by default lry_cache will store 128 values even if you don't define the size)
@lru_cache(maxsize = 1000)
#n is the input value that you can set to be any starting number
def fib(n):
#because the fib sequence (if n >=1 is 1, 1, 2, 3, 5 . . . if the input begins at "1", the first 2 values will be "1")
    if n==1:
        return 1 
    if n==2:
        return 1
#for all other number values, the formula will set n to be the sum of the previous "n" value + the "n" value before that one ((n-1) + (n-2)).
# So the third "n" value would be "1" + "1": "2".
# The fourth "n" value would be the previous n, in this case "2" + the n before that one, in this case "1". So the fourth "n" value would be "3".
# The fifth "n" value would be the previous n, in this case "3" + the n before that one, in this case "2". So the fifth "n" value would be "5".     
    elif n > 2:
         return fib(n-1) + fib(n-2)
#here we set the range of how many n values we want to return. Remember, the n value is not the result of the function, but how many total numbers we want to return. 
#So n in range (1, 101) does not mean, "return all fibonacci numbers that are below 100." It means, "return the first 100 numbers in the fibonacci sequence."
#The range is set to max 101, because the range doesn't include the last number, so 1-101 will return 100 n values.
for n in range (1, 101):
#This print function will return the fibonacci numbers formatted like this: "fib #: value." 1: 1, 2: 1, 3: 2, 4:5 . . .    
    print("{0}: {1}") .format(n, fib(n)) 
   