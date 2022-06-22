def kara(x, y):
    l1 = len(x)
    l2 = len(y)

    if l1 == 0 or l2 == 0:
        raise ValueError('zero length number found.')

    if (l1==1) and (l2==1):
        return str(int(x)*int(y)) # fall back to single digit multiplication 

    # padding 0 to the shorter digit string
    if l1 < l2:
        x = (l2-l1)*'0' + x
    elif l2 < l1:
        y = (l1-l2)*'0' + y

    # Calculates the half of the longer digit string.
    l = max(l1,l2)
    m = l // 2
    
    # Split the digit string in the middle. 
    x1, x0 = x[:l-m], x[l-m:]
    y1, y0 = y[:l-m], y[l-m:]

    # 3 recursive calls made to numbers approximately half the size.
    z0 = kara(x0, y0)
    z2 = kara(x1, y1)
    z1 = int(kara(str(int(x0) + int(x1)), str(int(y0) + int(y1)))) - int(z2) - int(z0)
    
    z2 = z2 + (m*2)*'0'
    z1 = str(z1) + (m)*'0'
    
    return str(int(z2)+int(z1)+int(z0))
    # return str((z2 * 10 ** (m * 2)) + (z1 * 10 ** m) + z0)

def main():
    a = '3141592653589793238462643383279502884197169399375105820974944592'
    b = '2718281828459045235360287471352662497757247093699959574966967627'
    a = '6994'
    b = '36'
    c = kara(a,b)
    print(c)
    print(int(a)*int(b))
if __name__ == '__main__':
    main()
