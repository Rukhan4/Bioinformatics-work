#Question 1

X = matrix(1:6,2,3)
test1 = t (t(X)) #Transpose the transpose 
test2 = X%*% matrix(1,ncol(X)) #Wtf
test3 = X*1 #Just multiply by 1
test4 = X%*%diag(ncol(X)) #Multiply by identity matrix

#Question 2

Y = matrix(c(3,2,1,5,4,2,-1,0,-5,2,5,0,1,-1,-5,4),4,4)
Z = matrix(c(10,5,7,4),4,1)
head(Y)
solve(Y)%*%Z

#Question 3
a = matrix(1:12,nrow=4)
b = matrix(1:15,nrow=3)
dim(a) # 4 x 3
dim(b) # 3 x 5
sol = a%*%b
sol[3,2]

#Question 4
weird = a[3,]%*%b[,2]
sum(weird)

#Question 5 

