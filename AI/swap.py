def swap(list1):
    return [(y,x) for (x,y) in list1]
if __name__=="__main__":
    print(swap([('a', 1), ('b', 2), ('c', 3)]))