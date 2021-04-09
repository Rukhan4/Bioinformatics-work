library(tissuesGeneExpression)
data(tissuesGeneExpression)

table(tissue)
ind = which(tissue!="placenta")
y = tissue[ind]
x = t(e[,ind])
dim(x)
length(y)

#Create set of indices to facilitate cross validation
library(caret)
set.seed(1)
idx = createFolds(y,k=5)
sapply(idx,function(i)table(y[i]))
#Splits data into 5 groups(folds) when we come to prediction part, leave out 1 fold 
#Test for the other 4 and compare to the left out fold

#Looking at first 2 dimensions from cmdscale (smaller set of predictors)
xsmall=cmdscale(dist(x))
library(rafalib)
mypar(1,1)
plot(xsmall,col=as.fumeric(y))
legend("topleft",levels(factor(y)),fill=seq_along(levels(factor(y))))

#Using KNN with machine learning-----------------------------------------------------
library(class)
#Test set
i = 1 #Only 1 fold
pred = knn(train=xsmall[-idx[[i]],],
           test = xsmall[idx[[i]],],
           cl = y[-idx[[i]] ],k=5)
table(true=y[idx[[i]] ],pred)
#count mistakes (17%)
mean(y[ idx[[i]] ]!=pred)

#Do for every fold (5)
set.seed(1)
k = 5
res.k = sapply(seq_along(idx),function(i){
  #Loop over each of the 5 cross-validation folds
  
  #Predict the held-out samples using k nearest neighbors
  pred = knn(train=xsmall[-idx[[i]],],
             test = xsmall[idx[[i]],],
             cl = y[-idx[[i]] ],k=k)
  #Ratio of misclassified samples
  sum(y[ idx[[i]] ]!=pred)
})
res.k #Made 6 mistakes in each tissue

#Compare different k values---------------------------------------------------------
set.seed(1)
ks = 1:12
res = sapply(ks,function(k){
res.k = sapply(seq_along(idx),function(i){
  #Loop over each of the 5 cross-validation folds
  
  #Predict the held-out samples using k nearest neighbors
  pred = knn(train=xsmall[-idx[[i]],],
             test = xsmall[idx[[i]],],
             cl = y[-idx[[i]] ],k=k)
  #Ratio of misclassified samples
  sum(y[ idx[[i]] ]!=pred)
})
sum(res.k)/length(y) #ERROR rate 
})


plot(ks,res) #Lowest point = least mistakes


#Using more than 2 dimensions----------------------------------------------------
xsmall=cmdscale(dist(x),k=5)
set.seed(1)
ks = 1:12
res = sapply(ks,function(k){
  res.k = sapply(seq_along(idx),function(i){

    #Predict the held-out samples using k nearest neighbors
    pred = knn(train=xsmall[-idx[[i]],],
               test = xsmall[idx[[i]],],
               cl = y[-idx[[i]] ],k=k)
    #Ratio of misclassified samples
    sum(y[ idx[[i]] ]!=pred)
  })
  sum(res.k)/length(y) #ERROR rate 
})
plot(ks,res,type="o",ylim=c(0,0.20)) 
