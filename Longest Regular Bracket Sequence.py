s = input()

stack = []

for i in range(len(s)):
  if s[i] == "(":
    stack.append(["(",i])
  elif stack and stack[-1][0] == "(":
    stack.pop()
  else:
    stack.append([")",i])


ct = 0
mx = 0


for i in range(len(stack)-1):
  mx = max(stack[i+1][1]-stack[i][1]-1,mx)
  
  # print(i,stack)
  
if stack:
  if stack[0][1] - 0 > 0:
    mx = max(stack[0][1],mx)
  if (len(s) - stack[-1][1] ) > 1:
    mx = max(len(s) - stack[-1][1]-1,mx)



# print(stack)
for i in range(len(stack)-1):
  if (stack[i+1][1]-stack[i][1]-1) == mx:
    ct += 1

if stack:
  if stack[0][1] - 0 == mx:
    ct += 1
    
  if (len(s) - stack[-1][1]-1 ) == mx:
    ct += 1


if not stack:
  print(len(s),1)
elif mx == 0:
  print(0,1)
else:
  print(mx,ct)
  

