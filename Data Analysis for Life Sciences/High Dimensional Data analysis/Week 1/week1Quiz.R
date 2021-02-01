library(GSE5859Subset)
data(GSE5859Subset)

#Question 1
dim(geneExpression) #row=samples,column = features

#Question 2
sum(sampleInfo$ethnicity=="ASN")

which(sampleInfo$ethnicity=="CEU")

#Question 3
sqrt( crossprod(geneExpression[,4]-geneExpression[,14]) )

#Question 4 #finds the mean distance between first sample(column 1) and all other samples
columns = 1:ncol(geneExpression)
mean_dists = sapply(columns, function(column){
  dists = sapply(x, function(x){
    test = geneExpression[,x]
    target = geneExpression[,column]
    sqrt(crossprod(target-test))
  })
  mean(dists)
})
which.max(mean_dists)

#Question 5 #For samples
max(dist(t(geneExpression)))

#Question 6 
sqrt( crossprod(geneExpression["1007_s_at",]-geneExpression["201371_s_at",]) )
sqrt( crossprod(geneExpression["202138_x_at",]-geneExpression["202152_x_at",]) )

#Question 7 #For features
max(dist(geneExpression))
