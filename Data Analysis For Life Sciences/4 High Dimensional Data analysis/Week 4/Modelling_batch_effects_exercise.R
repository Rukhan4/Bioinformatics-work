library(GSE5859Subset)
data(GSE5859Subset)
#purposely confound month and sex but not completely:
sex = sampleInfo$group
month = factor(format(sampleInfo$date,"%m"))
table(sampleInfo$group,month)

#Question 1 compare the 2 groups and find qvalue <0.1
library(qvalue)
library(genefilter)
pvals = rowttests(geneExpression,factor(sampleInfo$group))$p.value
qvals = qvalue(pvals)
sum(qvals$qvalues<0.1)

#Question 2 evaluate false and true positives with experimental data
#Here, evaluate results using the proportion genes on the list that are on ChrX or ChrY
index = geneAnnotation$CHR[qvals$qvalues<0.1]%in%c("chrX","chrY")
mean(index)

#Question 3 for autosomal genes for which qval<0.1, compare samples processed in june to october
index = which(qvals$qvalues<0.1 & !geneAnnotation$CHR%in%c("chrX","chrY"))
month = factor(format(sampleInfo$date,"%m"))
pvals = rowttests(geneExpression[index,],month)$p.value
mean(pvals<0.05)

#Question 4 fit a regression model using lm for each gene.
X = model.matrix(~sex+month)
pvals = sapply(1:nrow(geneExpression),function(i){
  y = geneExpression[i,]
  fit = lm(y~X-1)
  summary(fit)$coef[2,4] #June vs October
})
qvals = qvalue(pvals)$qvalue
sum(qvals<0.1)

#Question 6 proportion on chrX and chrY
index = geneAnnotation$CHR[qvals<0.1]%in%c("chrX","chrY")
mean(index)

#Question 7 from lm in q6, extract pvalues related to coefficients for obc vs june differences
#using same LM ---> Basically approach for combat 
pvals = sapply(1:nrow(geneExpression),function(i){
  y = geneExpression[i,]
  fit = lm(y~X)
  summary(fit)$coef[3,4]
})
qvals = qvalue(pvals)$qvalue
sum(qvals<0.1)

