
print("Enter the string:")
str=input()
def frequency(str):
    dict = {}
    for i in str:
        keys = dict.keys()
        if i in keys:
            dict[i] = dict[i]+ 1
        else:
            dict[i] = 1
    return dict
print(frequency(str))


