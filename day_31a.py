class Solution:
    def printTriangle(self, N):
          s=0
          for i in range(N,0,-1):
              for j in range(1,i+1):
                  print('*',end='')
              for k in range(0,s):
                  print(end=' ')
              s=s+2
              for h in range(i,0,-1):
                  print('*',end='')
              print()   
          a=2*(N-1)
          for x in range(0,N):
               for v in range(0,x+1):
                   print('*',end='')
               for y in range(0,a):
                   print(end=' ')
               a=a-2
               for z in range(0,x+1):
                   print('*',end='')
               print()   
     
