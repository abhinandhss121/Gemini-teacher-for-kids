def binary_search(lst,target):
    for i in range(len(lst)):
        if lst[i]==target:
            return i
def verify(index):
    if index is not None:
        print("target found at:",index)
    else:
        print("target not found")
numbers =  [x+2 for x in range(0,30)]
print(numbers)
res=binary_search(numbers,13)
verify(res)