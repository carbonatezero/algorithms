def quicksort0(A,p,r):
    '''CLRS
    '''
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

def partition0(A,p,r):
    '''
    CLRS version (last element as pivot)
    '''
    x = A[r]
    i = p - 1
    temp = 0
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    return i+1

def ChoosePivote1(A,l,r):
    '''first
    '''
    return l

def ChoosePivote2(A,l,r):
    '''final
    '''
    return r

def ChoosePivote3(A,l,r):
    '''
    median
    '''
    if r - l < 2:
        return l
    m = (r-l)//2 + l # don't forget plus the number l  !!!
    dic = {A[l]:l,A[m]:m,A[r]:r}
    b = [A[l],A[m],A[r]]
    b.sort()
    return dic[b[1]]

def quicksort(A,l,r):
    '''
    lecture
    '''
    if l >= r:
        return 0
    total = r - l
    i = ChoosePivote3(A,l,r)
    temp = A[l]
    A[l] = A[i]
    A[i] = temp 
    j = partition(A,l,r)
    total += quicksort(A,l,j-1)
    total += quicksort(A,j+1,r)
    return total

def partition(A,l,r):
    '''
    lecture version (first element as pivot)
    '''
    p = A[l]
    i = l+1
    temp = 0 
    for j in range(l+1,r+1):
        if A[j] < p:
            temp = A[j]
            A[j] = A[i]
            A[i] = temp 
            i += 1
    temp = A[l]
    A[l] = A[i-1]
    A[i-1] = temp 
    return i-1

def main():
    A = []
    with open('./QuickSort.txt') as f:
        A = f.readlines()
    for i in range(len(A)):
        A[i] = int(A[i].strip())

    # A = [3,2,1]
    total = quicksort(A,0,len(A)-1) 
    print(total)
    print(A[:100])

    # A = [8,2,4,5,7,1]
    # print('pivot')
    # print(ChoosePivote3(A,0,len(A)-1))



if __name__ == '__main__':
    main()

    print(162085)
    print(164123)
    print(138382)