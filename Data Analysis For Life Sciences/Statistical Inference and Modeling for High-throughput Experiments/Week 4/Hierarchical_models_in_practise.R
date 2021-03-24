BiocManager::install("SpikeInSubset")
library(Biobase)
library(SpikeInSubset)
data(rma95)
y <- exprs(rma95)
#This dataset comes from an experiment in which RNA was obtained from the same background pool to create 
#six replicate samples. 
#Then RNA from 16 genes were artificially added in different quantities to each sample.

#These quantities (in PicoMolars) and gene IDs are stored in:
pData(rma95)
#Note quantites same in first and last 3 arrays. define two groups
g = factor(rep(0:1,each=3))
#create index of which rows are associated with the artifically added genes
spike = rownames(y)%in%colnames(pData(rma95))

#Question 1
#Note only these 16 genes are differentially expressed since these 6 samples differ only due to random samp.
#(all come from the same backpool of RNA)
library(genefilter)
rtt = rowttests(y,g)
index = rtt$p.value<0.01
mean(!spike[index]) #NOT part of artificially added(false positives)

#visualize with volcano plot
mask <- with(rtt, abs(dm) < .2 & p.value < .01)
cols <- ifelse(mask,"red",ifelse(spike,"dodgerblue","black"))
with(rtt,plot(-dm, -log10(p.value), cex=.8, pch=16,
              xlim=c(-1,1), ylim=c(0,5),
              xlab="difference in means",
              col=cols))
abline(h=2,v=c(-.2,.2), lty=2)

#Question 2
sds <- rowSds(y[,g==0])

index <- paste0( as.numeric(spike), as.numeric(rtt$p.value<0.01))

index <- factor(index,levels=c("11","01","00","10"),labels=c("TP","FP","TN","FN"))

boxplot(split(sds,index))
#False positives have smaller SDs

#Question 3
#Following 3 steps perform the basic limma analysis:
library(limma)
fit <- lmFit(y, design=model.matrix(~ g))
colnames(coef(fit))

#This step uses hierarchical models that provide a new estimate of the gene specific row:
fit = eBayes(fit)

#New hierarchical model based estimate versus sample based estimate
sampleSD = fit$sigma
posteriorSD = sqrt(fit$s2.post)

LIM = range( c(posteriorSD,sampleSD))
plot(sampleSD, posteriorSD,ylim=LIM,xlim=LIM)
abline(0,1)
abline(v=sqrt(fit$s2.prior))
#Notice that the estimates of sd closer to 0.1

#Question 4 compute p values
fit = lmFit(y, design=model.matrix(~ g))
fit = eBayes(fit)
##second coefficient relates to diffences between group
pvals = fit$p.value[,2] 
index = pvals < 0.01
mean( !spike[index])
