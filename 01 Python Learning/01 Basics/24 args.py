def add(*args): # * is must args is just a variable
    sum = 0
    args = list(args) # now args is a list
    args[0] = 0 # first input will be zero
    for i in args:
        sum+= i
    return sum

print(add(1,2,3,4,5,6)) # ans will be (ans-1) bcz first element is now zero 