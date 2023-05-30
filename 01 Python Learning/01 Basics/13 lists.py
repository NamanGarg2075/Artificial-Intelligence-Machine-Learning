list = ["pizza","burger","noodles","hotdog"]

list[0] = "sushi" # pizza is now sushi
list.append("rolls") # add at last
list.remove("hotdog") # remove hotdog
list.pop() #remove last value
list.insert(1,"pasta") # add pasta at index 1
list.sort() #sort alphabetically
list.clear() #clear all list


# to print all values 👇
for x in list:
    print(x)