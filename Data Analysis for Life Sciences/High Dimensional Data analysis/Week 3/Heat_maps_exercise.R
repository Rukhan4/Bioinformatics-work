library(GSE5859Subset)
data(GSE5859Subset)
install.packages("matrixStats")
library(matrixStats)
library(gplots)
library(rafalib)
library(RColorBrewer)

#Question 1 date as labels, rows labelled with chromosomes, scale the rows

#Make colors
cols = colorRampPalette(rev(brewer.pal(11,"RdBu")))(25)
gcol=brewer.pal(3,"Dark2")
gcol=gcol[sampleInfo$group+1]

#Make labels - remove 2005 since its common to all
labcol = gsub("2005","",sampleInfo$date)

#Pick 25 genes with highest across sample variance
sds = rowMads(geneExpression)
ind = order(sds,decreasing=TRUE)[1:25]

#Make heatmap 
heatmap.2(geneExpression[ind,],
          col=cols,
          trace="none",
          scale="row",
          labRow = geneAnnotation$CHR[ind],
          labCol = labcol,
          ColSideColors = gcol,
          key=FALSE)

#Question 2
set.seed(17)
m = nrow(geneExpression)
n = ncol(geneExpression)
x = matrix(rnorm(m*n),m,n)
g = factor(sampleInfo$group)

ttest = rowttests(x,g)
sds=rowSds(x)
Indexes = list(t=order(ttest$p.value)[1:50],s=order(-sds)[1:50])
for(ind in Indexes){
heatmap.2(x[ind,],
          col=cols,
          trace="none",
          scale="row",
          labCol = g,
          key=FALSE)
}
