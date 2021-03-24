#Question 1 

X = matrix(1:1000,100,10)
head(X)
X[25,3]
dim(X)

#Question 2 
x = 1:10
Y = cbind(x1=x, x2=2*x, x3=3*x, x4=4*x, x5=5*x)
sum(Y[7,])
dim(Y)

#Question 3

q3 <- matrix(1:60,20,3,byrow=TRUE)
all(q3[,3]%%3==0)
dim(q3)

#Question 5
Z <- seq(10,1,-2)
Z[length(Z)]
