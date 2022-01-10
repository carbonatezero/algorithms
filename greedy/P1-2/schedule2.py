import sys
import functools

def readJobs(file):
    with open(file) as f:
        lines = f.readlines()
        n = lines[0]
        jobs = []
        for i in range(1,len(lines)):
            line = lines[i].split()
            temp = [int(line[0]), int(line[1])]
            jobs.append(temp)
        return n, jobs

def C_len(jobs, j):
    cj = 0 
    for k in range(j+1):
        cj += jobs[k][1]
    return cj

def cmpJobs(a,b):
        p = a[0] / a[1]
        q = b[0] / b[1]
        if p > q: 
            return -1
        elif p == q: 
            if a[0] > b[0]:
                return -1
            elif a[0] == b[0]:
                return 0 
            else:
                return 1
        else: 
            return 1

def getCompletionTime(jobs):
    jobs = sorted(jobs, key=functools.cmp_to_key(cmpJobs))
    # print(jobs)
    completionTime = 0
    for j in range(len(jobs)):
        # print(jobs[j][0],C_len(jobs, j))
        completionTime += jobs[j][0]*C_len(jobs, j)
    return completionTime


def main():
    file = sys.argv[1]
    n, jobs = readJobs(file)
    print(n)
    
    completionTime = getCompletionTime(jobs) 
    print("completionTime={}".format(completionTime))

if __name__ == '__main__':
    main()

# completionTime=67311454237