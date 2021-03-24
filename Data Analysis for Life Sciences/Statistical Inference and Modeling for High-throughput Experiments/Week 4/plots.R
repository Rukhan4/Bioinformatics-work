library(genefilter)
library(GSE5859Subset)
data(GSE5859Subset)
g = factor(sampleInfo$group)
results = rowttests(geneExpression,g)

m = nrow(geneExpression)
n = ncol(geneExpression)
randomdata = matrix(rnorm(n*m),m,n)
nullresults = rowttests(randomdata,g)

#Pvalue histogram(does not give idea of estimated effect size,just prob of seeing somn under null)--------
library(rafalib)
mypar(1,2)
hist(nullresults$p.value,ylim=c(0,1400),main="")
hist(results$p.value,ylim=c(0,1400),main="") #Differentially expressed genes 

#Volcano plot(shows effect size)--------------------------------------------------------------------------
mypar(1,1)
plot(results$dm,-log10(results$p.value),xlab="Effect size",ylab = "-log base 10 p-values")

#Boxplots and histograms
library(Biobase)
library(BiocManager)
BiocManager::install("GSE5859")
library(GSE5859) #NOT AVAILABLE FOR MY VERSION OF R :")
data (GSE5859)
ge = exprs(e)
ge[,49] = ge[,49]/log2(exp(1))#Purposefully put in problem to act as if when data was generated 
#They incorrectly took the natural log ofone of the samples and the rest are in the log2 scale

library(rafalib)
mypar(1,1)
boxplot(ge,range=0,names=1:ncol(e),col=ifelse(1:e))
#plot quantiles instead
qs = t(apply(ge,2,quantile),prob=c(0.05,0.25,0.5,0.75,0.95))
matplot(qs,type="l",lty=1)
sist(ge,unit=0.5)

#MA plot -----------------------------------------------------------------------------------
x = ge[,1]
y = ge[,2]
mypar(1,2)
plot(x,y)
plot((x+y)/2,x-y)
sd(y-x)