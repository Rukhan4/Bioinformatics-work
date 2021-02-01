library(dslabs)
data(heights)
head(heights)
#Quiz Conditional Expectations

heights$height = round(heights$height)
y = heights$sex =="Female"

x = mean(y[heights$height=="67"])

hts = c(60:80)
pr = sapply(hts,function(x0)mean(y[heights$height==x0]))
plot(hts,pr)              
abline(h=0.5) #above half
abline(v=64) #the exact hit

#Assignment setup 
library(BiocManager)
BiocManager::install("leukemiasEset")
library(leukemiasEset)
data(leukemiasEset)
dat = exprs(leukemiasEset)
leuk = leukemiasEset$LeukemiaType

#Question 1
#A and #B
dim(dat)
#C
sum(leuk=="AML")

#Question 2
d = dist(t(dat))
mds = cmdscale(d)
plot(mds[,1],mds[,2],bg=as.numeric(leuk),pch=21)
legend("bottomright",levels(leuk),col=seq(along=levels(leuk)),pch=15)

#Question 3
hc = hclust(d)
plot(hc,label=leuk)
table(cutree(hc,h=150))

#Question 5
library(matrixStats)
library(gplots)
library(RColorBrewer)
cols = colorRampPalette(rev(brewer.pal(11,"RdBu")))(25)
gcol=brewer.pal(5,"Dark2")
gcol=gcol[as.numeric(leuk)]

sds = rowMads(dat)
fold_ind = order(sds,decreasing=TRUE)[1:25]
heatmap.2(dat[fold_ind,],
          trace="none",
          scale = "row",
          key = FALSE,
          ColSideColors = gcol,
          labCol = leuk,
          col = cols)
#over 20 of the genes with the highest across sample variance are upregulated in CML
#and NoL and downregulated in other leukemias

#The bottom 2 genes in the plot tend to be upregulated in ALL and CLL and 
#downregulated in AML and CML

#Based on these 25 genes, the type of leukemia with the closest expression pattern
#to normal(NoL) bone marrow is CML

#Question 6 
leukTF = leuk == "NoL"
library(caret)
set.seed(2)
idx = createFolds(leukTF,k=5)
#A and #B
sapply(idx,function(fold_ind)table(leukTF[fold_ind]))

#OR
#A
idx = createFolds(leukTF, k=5)

normal_counts = sapply(1:length(idx), function(x){
  fold_fold_ind = idx[[x]]
  sum(leukTF[fold_fold_ind]==TRUE)
})

sum(normal_counts > 0)
#B
sum(normal_counts==3)

#Question 7 
library(genefilter)
m = 3 
fold_ind = idx[[1]]
pvals = rowttests(dat[,-fold_ind],factor(leukTF[-fold_ind]))$p.val
gene_ind = order(pvals)[1:m]
gene_ind

#Question 8 
library(class)

# use gene_fold_ind and fold_fold_ind to define training and test sets and training classes
train_set = t(dat[gene_ind, -fold_ind])
test_set = t(dat[gene_ind,fold_ind])
train_classes = leukTF[-fold_ind]

# set k=number of nearest neighbors
k = 5

# run knn
pred = knn(train_set, test_set, train_classes, k)

# count the number of errors
sum(pred!=leukTF[fold_ind])

#Question 9 #ALL 5 FOLDS
#A 
result = sapply(1:length(idx),function(x){
  fold_ind=idx[[x]]
  pvals = rowttests(dat[,-fold_ind],factor(leukTF[-fold_ind]))$p.val
  gene_ind = order(pvals)[1:m]
  train_set = t(dat[gene_ind, -fold_ind])
  test_set = t(dat[gene_ind,fold_ind])
  train_classes = leukTF[-fold_ind]
  pred = knn(train_set, test_set, train_classes, k=k)
  sum(pred!=leukTF[fold_ind])
  
})
sum(result)
#B
mean(result)/length(leukTF)
#C
1- (sum(result)/length(leukTF))
