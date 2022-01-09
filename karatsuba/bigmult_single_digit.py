def kara(x, y):
    l1 = len(x)
    l2 = len(y)

    if l1 == 0 or l2 == 0:
        raise ValueError('zero length number found.')

    if (l1==1) and (l2==1):
        return int(x) * int(y) # fall back to single digit multiplication 
    
    # Calculates the size of the larger numbers.
    m = max(l1, l2) // 2
    
    # Split the digit sequences in the middle. 
    if l1 == 1:
        x1, x0 = '0', x[:]
    else:
        x1, x0 = x[:l1-m], x[l1-m:]
    
    if l2 == 1:
        y1, y0 = '0', y[:]
    else:
        y1, y0 = y[:l2-m], y[l2-m:]

    # 3 recursive calls made to numbers approximately half the size.
    z0 = kara(x0, y0)
    z2 = kara(x1, y1)
    z1 = kara(str(int(x0) + int(x1)), str(int(y0) + int(y1))) - z2 - z0
    
    return ((z2 * 10 ** (m * 2)) + (z1 * 10 ** m) + z0)

def main():
    a = '3141592653589793238462643383279502884197169399375105820974944592'
    b = '2718281828459045235360287471352662497757247093699959574966967627'
    # a = '188'
    # b = '3'
    c = kara(a,b)
    print(c)
if __name__ == '__main__':
    main()
