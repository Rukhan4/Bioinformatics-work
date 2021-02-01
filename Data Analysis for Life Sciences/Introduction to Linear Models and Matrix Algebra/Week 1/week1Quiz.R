#Question 3

g = 9.8
n = 25
h0 = 8848
v0 = 0
time = 10
f = h0+v0*time -0.5*g*time^2

#Question 4
A = matrix(c(2,9,5,2,9,5),2,3)
dim(A)
A[1,2]

#Matrix notation Exercise 6
2.5:6.5
seq(2.5,6.5)
rep(2.5,6.5)
c(2.5,6.5)

#Question 6 
q6 = c(seq(1,2),seq(3,4)) #returns a vector 

#Question 7 
#Det = 0 or
Q7 = matrix(c(2,1,6,3),2,2)
I = matrix(c(1,0,0,1),2,2)
head(I)
solve(Q7,I) #doesnt work because system is exactly singular!

#Question 8 
systemeq = matrix(c(1,0,2,1,2,5,1,5,-1),3,3)
soln = matrix(c(6,-4,27),3,1)
solve(systemeq)%*%soln
