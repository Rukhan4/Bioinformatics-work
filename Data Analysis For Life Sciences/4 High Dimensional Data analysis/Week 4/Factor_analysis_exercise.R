library(Biobase)
library(GSE5859Subset)
data(GSE5859Subset)

y = geneExpression - rowMeans(geneExpression)

#Question 1

library(rafalib)
mypar(1,2)
sex = sampleInfo$group
cors = cor(y)
image(cors)
o = order(sampleInfo$date)
image(cors[o,o])
#The fact that in the plot ordered by month we see two groups mainly driven by month and 
#within these, we see subgroups driven by date seems to suggest date more than month per se 
#are the hidden factors

#Question 2 use PCA to estimate the 2 factors we believe are present from q1
pcs = svd(y)$v[,1:2]

#Question 3
month = factor(format(sampleInfo$date,"%m"))
cols = as.numeric(month)[o]
for(i in 1:2){
  plot(pcs[o,i],col=cols,xaxt="n",xlab="")
  label = gsub("2005-","",sampleInfo$date[o])
  axis(1,1:ncol(y),label,las=2)
}
#Most different is june 23 and june 27

#Question 4 use svd to obtain principal components(PCs) for detrended gene expression data y
#and find PCs explain more than 10% each of the variability
s = svd(y)
variability = s$d^2/sum(s$d^2)
sum(variability>0.10)

#Question 5
#A which pc most correlates (negative or positive correlation) with month
cors = cor(as.numeric(month),s$v)
which.max(cors)
#B cor in abs value
max(abs(cors))

#Question 6 with sex
cors = cor(as.numeric(sex),s$v)
which.max(cors)
max(abs(cors))

#Question 7 add the two estimated factors in Q6 to the LM:
X = model.matrix(~sex+s$v[,1:2])
#Apply this model to each gene, and compute q-values for the sex difference

pvals = sapply(1:nrow(geneExpression),function(i){
  y = geneExpression[i,]
  fit = lm(y~X-1)
  summary(fit)$coef[2,4]
  })
library(qvalue)
qvals = qvalue(pvals)
sum(qvals$qvalues<0.1)

#Proportion of the genes on chrX and chrY
index = geneAnnotation$CHR[qvals$qvalues<0.1]%in%c("chrX","chrY")
mean(index)
