class Math:   
    @staticmethod # don't keed any special argument like self or cls
    def add(a,b):
        return a+b
    
s1 = Math()
result = s1.add(3,2)
print(result)