BiocManager::install("sva")
library(sva)
library(Biobase)
library(GSE5859Subset)
data(GSE5859Subset)
#First factor correlated with outcome of interest
s = svd(geneExpression- rowMeans(geneExpression))
cor(sampleInfo$group,s$v[,1])
#Use SVA to estimate the effects of finding genes that are differentially expressed
#While using factor analysis approach to account for batch effects
#svafit() estimates factors but downweighting the genes that appear to correlate with the outcome
#of interest
#It also tries to estimate the number of factors and returns the estimated factors like:
sex = sampleInfo$group
mod = model.matrix(~sex)
svafit = sva(geneExpression,mod)
head(svafit$sv)
#Note resulting estimated factors are not that different from principal component(PCs):
for(i in 1:ncol(svafit$sv)){
  print( cor(s$v[,i],svafit$sv[,i]) )
}

#Question 1 fit a LM to estimate the difference between male and females for each gene
#but instead of accounting for batch effects using month,, it includes the 
#factors estimated by sva in the model. 
library(qvalue)
X = model.matrix(~sex+svafit$sv)
pvals = sapply(1:nrow(geneExpression),function(i){
  y = geneExpression[i,]
  fit = lm(y~X-1)
  summary(fit)$coef[2,4]
})
qvals = qvalue(pvals)
sum(qvals$qvalues<0.1)

#Question 2 proportion of genes from Q1 are from chrY and chrX
index = geneAnnotation$CHR[qvals$qvalues<0.1]%in%c("chrX","chrY")
mean(index)
