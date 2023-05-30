def hello(**kwargs):
    print("Hello" , end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(first="NAMAN",last="GARG") # we can now add unlimited key and values tot this function
