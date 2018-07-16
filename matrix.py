import random

from copy import deepcopy


class Matrix:
    #m=[]
    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.m = []
        self.row=nrows
        self.col=ncols
        for i in range(0,nrows):
            self.m.append([])
            for j in range (0,ncols):
                self.m[i].append(random.randint(0,9))
        
    def add(self, m):
        """return a new Matrix object after summation"""
        M=Matrix(self.row, self.col)
        for i in range(0,self.row):
            for j in range (0, self.col):
                M.m[i][j]=self.m[i][j]+m.m[i][j]
        return M
    def sub(self, m):
        """return a new Matrix object after substraction"""
        M=Matrix(self.row, self.col)
        for i in range(0,self.row):
            for j in range (0, self.col):
                M.m[i][j]=self.m[i][j]-m.m[i][j]
        return M
        
    def mul(self, m):
        """return a new Matrix object after multiplication"""
        M=Matrix(self.row, m.col)
        for i in range(0,self.row):
            for j in range (0, m.col):
                M.m[i][j]=0
                for g in range(0,self.col):
                    M.m[i][j]=M.m[i][j]+self.m[i][g]*m.m[g][j]
        return M
    def transpose(self):
        """return a new Matrix object after transpose"""
        M=Matrix(self.row, self.col)
        for i in range(0,self.row):
            for j in range (0, self.col):
                M.m[i][j]=self.m[j][i]
        return M
  
    def display(self):
        """Display the content in the matrix"""
        #print(self.m)
        for i in range(0,self.row):
            for j in range(0,self.col):
                print(self.m[i][j],end='')
                print(' ',end='')
            print()
        
row=int(input("Enter A Matrix's rows:"))
col=int(input("Enter A Matrix's cols:"))
A=Matrix(row,col)
row=int(input("Enter B Matrix's rows:"))
col=int(input("Enter B Matrix's cols:"))
B=Matrix(row,col)
print('matrix A:')
A.display()
print('matrix B:')
B.display()
print('----A+B----')
if A.row!=B.row or A.col!=B.col:
    print("Matrix's size should be in the same size!")
else:
    A.add(B).display()
print('----A-B----')
if A.row!=B.row or A.col!=B.col:
    print("Matrix's size should be in the same size!")
else:
    A.sub(B).display()
print('----A*B----')
if A.col!=B.row:
    print("Matrix's size should be in the same size!")
else:
    A.mul(B).display()
print('----the transpose of A*B----')
if A.col!=B.row:
    print("Matrix's size should be in the same size!")
else:
    A.mul(B).transpose().display()
