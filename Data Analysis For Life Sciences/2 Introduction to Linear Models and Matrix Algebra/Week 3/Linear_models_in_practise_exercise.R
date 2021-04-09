nx = 5
ny = 7
X = cbind(rep(1,nx + ny),
          rep(c(0,1),
              c(nx, ny)))

#Question 1 (What is X^T by X)
ans = t(X)%*%X
ans[1,1]

#Question 2
t(X)%*%X

#Matrix inversion (X^t by X)^-1
#1/determinant x inverted matrix

determinant = 1/((12*7)-(7*7))
invert = matrix(c(7,-7,-7,7)) 
matrixinversion = determinant*invert
matrix(matrixinversion)
