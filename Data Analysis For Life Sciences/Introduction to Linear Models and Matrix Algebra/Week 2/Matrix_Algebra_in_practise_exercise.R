X = matrix(c(1,1,1,1,0,0,1,1),nrow=4)
rownames(X) = c("a","a","b","b")
#fitted parameters:
beta = c(5,2)

#Question 1 
fitted = X%*%beta
fitted[1:2,]
#Question 2 
fitted = X%*%beta
fitted[3:4,]
