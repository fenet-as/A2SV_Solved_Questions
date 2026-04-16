class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        path = []


        def explore(i):
            # print(path)
            if i == len(num):
                if len(path) >= 3:
                    return True
                return False

            
            for j in range(i,len(num)):
                val = num[i:j+1]

                if num[i] == "0" and len(val) > 1:
                    break
                val = int(val)
                    
                # print("val: ",val)

                if len(path) >= 2:
                    if path[-1] + path[-2] == val:
                        path.append(val)
                        if explore(j+1):
                            return True
                        path.pop()
                        
                    elif path[-1] + path[-2] > val:
                        continue
                    else:
                        break
                else:
                    path.append(val)
                    if explore(j+1):
                        return True
                    path.pop()

            return False

        return explore(0)


