#Transpose --------------------------------------------------------------------------
X = matrix(1:15,5,3) #5x3 matrix
X #a 5x3 matrix

t(X) #Becomes 3x5 matrix 

#Scalar multiplication--------------------------------------------------------------
Y = matrix(1:12,4,3)
Y

a = 2 #The scalar quantity
Y*a

#Multiplication---------------------------------------------------------------------

Z<- matrix(c(1,3,2,1,-2,1,1,1,-1),3,3) #Matrix from book created
#We know answer is (6,2,1) we can try guessing
beta = c(1,2,3)
Z%*%beta #It works!!!

#Inverse (solving question under matrix operations)---------------------------------

A = matrix(c(1,3,2,1,-2,1,1,1,-1),3,3)
B = matrix(c(6,2,1),3,1)
solve(A)%*%B
#Hence, a = 1, b = 2 and c = 3