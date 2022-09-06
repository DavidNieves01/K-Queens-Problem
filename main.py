class solution:
    def solveKqueens(self, n: int) -> List[List[str]]: 
        col = set()
        posdiag = set()
        negdiag = set()

        res = []

        board =[["."]* n for i in range(n)]

        def backtrack(r):
            if(r == n):
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for j in range(n):
                if j in col or (r+j) in posdiag or (r- j) in negdiag:
                    continue 
                col.add(j)
                posdiag.add(r+j)
                negdiag.add(r-j)
                board[r][j] = "Q"
                
                backtrack(r+1)

                col.remove(j)
                posdiag.remove(r+j)
                negdiag.remove(r-j)
                board[r][j] = "."   
        backtrack(0)
        return res