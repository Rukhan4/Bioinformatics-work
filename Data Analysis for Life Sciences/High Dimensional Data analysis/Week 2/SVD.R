set.seed(1)
library(MASS)
library(rafalib)
n = 100
y = t(mvrnorm(n,c(0,0),matrix(c(1,0.95,0.95,1),2,2)))

mypar()
LIM = c(-3.5,3.5)
plot(y[1,],y[2,],xlim=LIM,ylim=LIM)

#SVD
s = svd(y)
pc1 = s$d[1]*s$v[,1]
pc2 = s$d[2]*s$v[,2]
plot(pc1,pc2,xlim=LIM,ylim=LIM)

#REAL DATA
library(tissuesGeneExpression)
data(tissuesGeneExpression)
dim(e)

#Standardize rows
set.seed(1)
ind = sample(nrow(e),500)
Y = t(apply(e[ind,],1,scale))

s = svd(Y)

V = s$v

D = diag(s$d)

Yhat = U%*%D%*%t(V)

resid = Y-Yhat
max(abs(resid))

plot(s$d) #See D that are 0, we remove them with dimension reduction

k = ncol(U)-4
Yhat = U[,1:k]%*%D[1:k,1:k]%*%t(V[,1:k])
resid = Y-Yhat
max(abs(resid))

plot(s$d^2 / sum(s$d^2)*100)

#Remove half of the dimensions 
k = ncol(U)-95
Yhat = U[,1:k]%*%D[1:k,1:k]%*%t(V[,1:k])
resid = Y-Yhat
boxplot(resid,ylim=LIM) #very small residuals, close to the original y even with half reduced dim.

#calculate percent kept

1 - var(as.vector(resid))/var(as.vector(Y)) #we lost about 5%

#Same as
sum(s$d[1:k]^2)/sum(s$d^2)


#Simulation with highly correlated data

m = 100 
n = 2
x = rnorm(m)
e = rnorm(n*m,0,0.01)
Y = cbind(x,x)+e

cor(Y)
D = svd(Y)$d
D[1]^2/sum(D^2)
