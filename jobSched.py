n = int(input("Enter number of jobs: "))
jobs = []
res=[]

print("Enter ID, deadline, and profit respectively for each job:")
for i in range(n):
    while True:
        job_input = list(map(int, input("Job " + str(i+1) + ": ").split()))
        if len(job_input) < 3:
            print("Each job must have at least three elements: ID, deadline, and profit.")
            continue
        break
    jobs.append(job_input)

def printJobScheduling(arr, t):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
  
    result = [False] * t
    sce_job = ['-1'] * t
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                sce_job[j] = arr[i][0]
                break
    for i in sce_job:
        if i!="-1":
            print(i)

printJobScheduling(jobs, n)
