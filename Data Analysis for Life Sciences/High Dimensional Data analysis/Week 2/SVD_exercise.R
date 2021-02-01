library(tissuesGeneExpression)
data(tissuesGeneExpression)

#Important note: When using the SVD in practice it is important to note that the solution to SVD is not unique. 
#This is because  UDV⊤=(−U)D(−V)⊤ .
#In fact we can flip the sign of each column of  U  and as long as we also flip the respective column in  V  the decompostion works.
#Here is R code demonstrating this:
s = svd(e)
signflips = sample(c(-1,1),ncol(e),replace=TRUE)
signflips

#Switch sign of each column to check if we get same answer using sweep()
#If x is a matrix and a is a vector, then sweep(x,1,y,FUN="*") applies the function FUN to each 
#row i FUN(x[i,],a[i]), in this case x[i,]*a[i]. 
#If instead of 1 we use 2, sweep() applies this to columns. 
newu= sweep(s$u,2,signflips,FUN="*")
newv= sweep(s$v,2,signflips,FUN="*" )
all.equal( s$u %*% diag(s$d) %*% t(s$v), newu %*% diag(s$d) %*% t(newv)) #Function is * (multiply)

#Question 1
#SVD of e:
s = svd(e)
m = rowMeans(e) #mean of each row
cor(s$u[,1],m)

#Note if we change the means, the distance between columns do not change:
newmeans = rnorm(nrow(e)) ##random values we will add to create new means
newe = e+newmeans ##we change the means
sqrt(crossprod(e[,3]-e[,45]))
sqrt(crossprod(newe[,3]-newe[,45]))

#So we might as well make the mean of each row 0 since it does not help us approximate the column distances. 
#We will define y as the detrended e and recompute the SVD:

y = e-rowMeans(e)
s = svd(y)

#We showed that  UDV⊤  is equal to y up to numerical error:
resid = y - s$u %*% diag(s$d) %*% t(s$v)
max(abs(resid))

#Above can be done in 2 different ways
#1 using crossprod and #2 not creating a diagonal matrix. 
#Note in R we can multiply a matrix x by vector a. result is a matrix with row i = x[i,]*a[i]. Example:
x=matrix(rep(c(1,2),each=5),5,2)
x
x*c(1:5)
#The code above is equivalent to:
sweep(x,1,1:5,"*")
#Hence we do not need to convert s$d into a matrix to obtain DVT

#Question 2
diag(s$d)%*%t(s$v)
#Is equal to
s$d*t(s$v)

#Question 3
#If we define vd = t(s$d * t(s$v)), all of the below are the same as UDVT:
#tcrossprod(s$u,vd)
#s$u%*%(s$d*t(s$v))
#s$u%*%t(vd)

#Question 4
z = s$d * t(s$v)
sqrt(crossprod(e[,3]-e[,45]))
sqrt(crossprod(y[,3]-y[,45]))
sqrt(crossprod(z[,3]-z[,45]))
#All the same distances because U is orthogonal
real = sqrt(crossprod(e[,3]-e[,45]))
approx = sqrt(crossprod(z[1:2,3]-z[1:2,45]))
abs(real-approx)

#Question 5 min no of dimensions needed for approx of SVD in 4 to be within 10% or less
ks = 1:189
realdistance = sqrt(crossprod(e[,3]-e[,45]))
approxdistances = sapply(ks,function(k){
  sqrt(crossprod(z[1:k,3,drop=FALSE]-z[1:k,45,drop=FALSE]))
})
percentdiff = 100*abs(approxdistances-realdistance)/realdistance
min(ks[which(percentdiff<10)])

#Visualize question 5:
plot(ks,percentdiff)

#Question 6
#distances between sample 3 and all other samples:
distances = sqrt(apply(e[,-3]-e[,3],2,crossprod))

#Using 2D approximation 
approxdistances = sqrt(apply(z[1:2,-3]-z[1:2,3],2,crossprod))
#spearman correlation between the approx and actual distance
cor(distances,approxdistances,method="spearman")

#Visualize question 6:
plot(distances,approxdistances)
