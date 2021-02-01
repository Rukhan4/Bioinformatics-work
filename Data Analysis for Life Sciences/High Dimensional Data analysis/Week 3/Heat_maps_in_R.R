library(tissuesGeneExpression)
data(tissuesGeneExpression)
image(e[1:100,]) #yellow means high red means low expression

#Reduce rows cus 22,000 rows
library(genefilter)
#Take top 40 varying genes 
rv = rowVars(e)
idx = order(-rv)[1:40]

heatmap(e[idx,])

#change colors 
library(RColorBrewer)
hmcol = colorRampPalette(brewer.pal(9,"GnBu"))(100) #greentoblue
heatmap(e[idx,],col=hmcol) #white means low and blue means high expression

#different function to make heatmaps
library(gplots)
library(rafalib)
cols = palette(brewer.pal(7,"Dark2"))[as.fumeric(tissue)]
cbind(colnames(e),cols)
heatmap.2(e[idx,],labCol=tissue,trace="none",ColSideColors=cols,col=hmcol)
