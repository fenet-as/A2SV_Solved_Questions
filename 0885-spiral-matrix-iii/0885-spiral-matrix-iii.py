class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        

        

        ll = cStart - 2
        rl = cStart + 2
        ul = rStart - 2
        dl = rStart + 2

        cr = rStart
        cc = cStart
        res = [[cr,cc]]

        # print("left limit ", ll)
        # print("right limit ", rl)
        # print("up limit ", ul)
        # print("down limit ", dl)


        while len(res) < (rows*cols):
            # move right

            for j in range(cc+1,rl):
                if 0 <= j < cols and 0 <= cr < rows:
                    res.append([cr,j])
                    # print("move right ")
                    # print([cr,j])

            cc = rl - 1 
        
            
            # move down

            for i in range(cr+1,dl):
                if 0 <= i < rows and 0 <= cc < cols:
                    res.append([i,cc])
                    # print("move down ")
                    # print([i,cc])
            cr = dl - 1

            # move left

            for j in range(cc-1,ll,-1):
                if 0 <= j < cols and 0 <= cr < rows:
                    res.append([cr,j])
                    # print("move left ")
                    # print([cr,j])

            cc = ll + 1

            # move up
            for i in range(cr-1,ul,-1):
                if 0 <= i < rows and 0 <= cc < cols:
                    res.append([i,cc])
                    # print("move up ")
                    # print([i,cc])
            
            cr = ul + 1

            ul -= 1
            dl += 1
            ll -= 1
            rl += 1
        return res

