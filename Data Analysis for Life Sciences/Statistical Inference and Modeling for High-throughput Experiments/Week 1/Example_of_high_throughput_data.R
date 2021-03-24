library(devtools)
install_github("genomicsclass/GSE5859Subset")

library(GSE5859Subset)
data(GSE5859Subset)

dim(geneExpression)

#Grabbing sample information
head(sampleInfo)
dim(sampleInfo)

#Check if sampleinfo contains info directly from gene expression's measured matrix
identical(colnames(geneExpression),sampleInfo$filename)

#To know what group each column of gene expression matrix comes from:
sampleInfo$group
#1 = case 0 = control

#Find symbols(genes)
geneAnnotation
head(geneAnnotation)
#Eg. DDR1 represents a gene with its chromosome,chr location and ID