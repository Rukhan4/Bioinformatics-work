#Question 1

f = matrix(c(1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,0,0,1,1,1,1,0,0,0),6,4)
qr(f)$rank
ncol(f)
#Different hence collinear, expt is designed badly
e = matrix(c(1,1,1,1,0,0,1,1,0,1,0,1,0,0,0,1),4,4)
cat(ncol(e),qr(e)$rank)
#Same hence no cofounding, expt is designed correctly

#Question 2

sex <- factor(rep(c("female","male"),each=4))
trt <- factor(c("A","A","B","B","C","C","D","D"))
X = model.matrix(~sex+trt)
cat(ncol(X),qr(X)$rank)
#Different hence collinear
Y = 1:8 #Observe some random outcome Y

makeYstar <- function(a,b) Y - X[,2] * a - X[,5] * b
fitTheRest <- function(a,b) {
  Ystar <- makeYstar(a,b)
  Xrest <- X[,-c(2,5)]
  betarest <- solve(t(Xrest) %*% Xrest) %*% t(Xrest) %*% Ystar
  residuals <- Ystar - Xrest %*% betarest
  sum(residuals^2)
}

fitTheRest(1,2)

#Question 3 

betas = expand.grid(-2:8,-2:8)
rss = apply(betas,1,function(x) fitTheRest(x[1],x[2])) #NOTE LOWERCASE x

themin = min(rss)
betas[which(rss==themin),]

#Visualize sums of squared residuals over our grid with imagemat() from rafalib
library(rafalib)
plot(betas[which(rss==themin),])

#^^^^^ infinite line of solutions !!!