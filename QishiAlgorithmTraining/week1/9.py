#https://leetcode.com/problems/game-of-life/description/
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        Input: 
        [
          [0,1,0],     0 -1 0    
          [0,0,1],     12 0 1    
          [1,1,1],     -1 1 1    
          [0,0,0]      12 0 0   
        ]              
       
       die  negativ original val
       live original val + n
       
       val=abs(valnow) % n
       
       
       die 0 1
       live 1 0
       die 2 0
       live 3 1
        Output: 
        [
          [0,0,0],
          [1,0,1],
          [0,1,1],
          [0,1,0]
        ]
        
        Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population..
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

        """
        
        #add padding:
        nrow=len(board)
        ncol=len(board[0])
        n=nrow*ncol
        
         
            
        
        def findneighborsum(i,j,nrow,ncol,board):
            me=None
            neighborsum=0
            for deltax in [-1,0,1]:
                for deltay in [-1,0,1]:
                    if deltax==0 and deltay==0:
                        me=abs(board[i][j])%n
                        
                    
                    if i+deltax >=0 and i+deltax<nrow and j+deltay>=0 and j+deltay<ncol:
                        neighborsum+=abs(board[i+deltax][j+deltay])%n
            neighborsum-=me
            if me==1:
                #me is live
                #rule1 
                if neighborsum<2:
                    #me die:
                    print("die %i %i" % (i,j))
                    board[i][j]=-(abs(board[i][j])%n)
                   
                if neighborsum>3:
                    #me die:
                    print("die %i %i" % (i,j))
                    board[i][j]=-(abs(board[i][j])%n)
                   
            else:
                if neighborsum==3:
                    #me relive
                    print("live %i %i" % (i,j))
                    board[i][j]=(abs(board[i][j])%n)+n
                     
                    
        if n==1:
            board[0][0]=0
        else:
            for i in range(nrow):
                for j in range(ncol):
                    findneighborsum(i,j,nrow,ncol,board)

            print(board)

            for i in range(nrow):
                for j in range(ncol):
                    if board[i][j]<0:
                        board[i][j]=0

                    if board[i][j]>1:
                        board[i][j]=1
                    
        
                    
                    
            
                
                        
                        
                    
                    
            
        
