import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))

common = set(a1) & set(a2)
res = 0
i = 0
for e in common:
  res += (a1.count(e) * a2.count(e))
  # print(e,res)


print(res)




