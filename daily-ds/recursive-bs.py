def recursive_bs(list,target):
    if len(list)==0:
        return False
    else:
        mid = len(list)//2
        if list[mid] == target:
            return True
        else:
            if list[mid]< target:
                return recursive_bs(list[mid+1:],target)
            else:
                return recursive_bs(list[:mid],target)
def verify(index):
    if index is not None:
        print("target foound",res)           
num = [x for x in range(20)]
res = recursive_bs(num,12)
verify(res)
