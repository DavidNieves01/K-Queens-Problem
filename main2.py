class solution2:
    def totalKqueens(self, n: int) -> int: 
        col = set()
        posdiag = set() # r+j
        negdiag = set() #r-j

        res = 0

        

        def backtrack(r):
            if(r == n):
                nonlocal res
                res = res + 1 
                return
            for j in range(n):
                if j in col and (r+j) in posdiag and (r- j) in negdiag:
                    continue 
                col.add(j)
                posdiag.add(r+j)
                negdiag.add(r-j)
                
                
                backtrack(r+1)

                col.remove(j)
                posdiag.remove(r+j)
                negdiag.remove(r-j)
                   
        backtrack(0)
        return res