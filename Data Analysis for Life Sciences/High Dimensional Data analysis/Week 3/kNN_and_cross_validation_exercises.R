library(GSE5859Subset)
data(GSE5859Subset)

#Define outcome and predictors with only autosomal genes
y = factor(sampleInfo$group)
x = t(geneExpression)
out = which(geneAnnotation$CHR%in%c("chrx","chrY"))
x = x[,-out]

library(caret)

#Question 1 2nd entry in fold 3 -------------------------------------------------
RNGkind(sample.kind = "Rounding")
set.seed(1)
idx = createFolds(y,k=10)
idx[[3]][2]
sapply(idx,function(ind) table(y[ind])) ##make sure every fold has 0s and 1s

#Question 2----------------------------------------------------------------------
#For the following questions we are going to use kNN. We are going to consider 
#a smaller set of predictors by filtering genes using t-tests. 
#Specifically, we will perform a t-test and select the  m  genes with 
#the smallest p-values.
library(class)
library(genefilter)
m = 8
k = 5
ind = idx[[2]] #Leave out 2nd row
pvals = rowttests(t(x[-ind,]),factor(y[-ind]))$p.val #on training data
ind2=order(pvals)[1:m]
predict = knn(x[-ind,ind2],x[ind,ind2],y[-ind],k=k)
sum(predict!=y[ind]) #Mistakes made on test set

#Question 3 all 10 folds---------------------------------------------------------
result = sapply(idx,function(ind){
  pvals = rowttests(t(x[-ind,]),factor(y[-ind]))$p.val 
  ind2=order(pvals)[1:m]
  predict = knn(x[-ind,ind2],x[ind,ind2],y[-ind],k=k)
  sum(predict!=y[ind]) 
})
sum(result)/length(y) #error rate


#Question 4-------------------------------------------------------------------------
#Selecting best values of k and m
ms = 2^c(1:11)
ks = seq(1,9,2)
params = expand.grid(k=ks,m=ms)
#Finding minimum error rate

errors = apply(params,1,function(param){
  k = param[1]
  m = param[2]
  result = sapply(idx,function(ind){
    pvals = rowttests(t(x[-ind,]),factor(y[-ind]))$p.val 
    ind2=order(pvals)[1:m]
    predict = knn(x[-ind,ind2],x[ind,ind2],y[-ind],k=k)
    sum(predict!=y[ind]) 
  })
  sum(result)/length(y)
})
params[which.min(errors),] #minimum error rate

#Question 5 repeat Q4 but perform t-test filtering before cross validation
pvals = rowttests(t(x),factor(y))$p.value
errors = apply(params,1,function(param){
  k = param[1]
  m = param[2]
  result = sapply(idx,function(ind){
    ind2=order(pvals)[1:m]
    predict = knn(x[-ind,ind2],x[ind,ind2],y[-ind],k=k)
    sum(predict!=y[ind]) 
})
  sum(result)/length(y)
})
min(errors) #Minimum error rate

#Question 5 changing y ---------------------------------------------------------------
y = factor(as.numeric(format( sampleInfo$date, "%m")=="06"))
errors = apply(params,1,function(param){
  k =  param[1]
  m =  param[2]
  result = sapply(idx,function(ind){
    pvals = rowttests(t(x[-ind,]),factor(y[-ind]))$p.val
    ind2 = order(pvals)[1:m]
    predict=knn(x[-ind,ind2],x[ind,ind2],y[-ind],k=k)
    sum(predict!=y[ind])
  })
  sum(result)/length(y)
})
min(errors)
