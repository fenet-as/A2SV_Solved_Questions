class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        
        def search(i,j,m,row,col,word):
            if m == len(word):
                return True

            if board[i][j] == "#":
                return False
            if board[i][j] == word[m]:
                temp = board[i][j]
                board[i][j] = "#"
                m += 1
                if m == len(word):
                    return True

                if i+1 < row:
                    if search(i+1,j,m,row,col,word):
                        return True
                if i-1 >= 0:
                    if search(i-1,j,m,row,col,word):
                        return True
                if j+1 < col:
                    if search(i,j+1,m,row,col,word):
                        return True
                if j-1 >= 0:
                    if search(i,j-1,m,row,col,word):
                        return True
                
                board[i][j] = temp
            return False

            

        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i,j,0,len(board),len(board[0]),word):
                    return True

        return False

        
            


                

                