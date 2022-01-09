def sort_and_CountInv(a):
    n = len(a)
    if n == 0 or n == 1:
        return a,0
    else:
        c, leftInv = sort_and_CountInv(a[:n//2])
        d, rightInv = sort_and_CountInv(a[n//2:])
        b, splitInv = _merge_and_CountSplitInv(c,d,n)
        
        total = leftInv+rightInv+splitInv
        return b, total

def _merge_and_CountSplitInv(c,d,n): 
    # using naive method 
    # to combine two sorted lists
    size_1 = len(c)
    size_2 = len(d)
      
    res = []
    i, j = 0, 0
    splitInv = 0
      
    while i < size_1 and j < size_2:
        if c[i] < d[j]:
          res.append(c[i])
          i += 1
        else:
          res.append(d[j])
          j += 1
          splitInv += len(c) - i
      
    res += c[i:] + d[j:]
    return res, splitInv

def main():
    # read array from file
    a = []
    with open('./IntegerArray.txt') as f:
        a = f.readlines()
    for i in range(len(a)):
        a[i] = int(a[i].strip())

    # a = [11,12]
    # b = [4,5]
    # c = _merge_and_CountSplitInv(a,b,2)
    # print(c)

    # a = [6,5,4,3,2,1]
    b = sort_and_CountInv(a)
    print(b[1])

if __name__ == '__main__':
    main()