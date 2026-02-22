n, k = map(int, input().split())
arr = list(map(int, input().split()))

if k == 1:
    print(arr[-1] - arr[0])
    exit()


gaps = []
for i in range(1, n):
    gaps.append(arr[i] - arr[i-1])


gaps.sort(reverse=True)


total = arr[-1] - arr[0]
answer = total - sum(gaps[:k-1])

print(answer)
