# 11.23.21 Tue
# This code is for problem 3 in the quiz.

def main():
    p = [7, 0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23] # quiz
    p = [7, .2, .05, .17, .1, .2, .03, .25] # final exam
    n = p[0]
    A = [[0 for _ in range(n+1)] for _ in range(n+1)]
    print(len(A))

    for s in range(n):
        for i in range(1,n-s+1):
            temp = []
            for r in range(i,i+s+1):
                t = 0
                # print(40*'.-')
                # print(s,i,r)
                # print(i,r-1,r+1,i+s)
                # print(40*'.-')
                if i <= r-1:
                    t += A[i][r-1]
                if r+1 <= i+s:
                    t += A[r+1][i+s]
                temp.append(t)
            A[i][i+s] = sum(p[i:i+s+1]) + min(temp)
    soln = A[1][n]
    print(soln)

if __name__ == '__main__':
    main()