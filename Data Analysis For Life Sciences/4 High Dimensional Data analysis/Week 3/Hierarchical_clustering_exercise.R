set.seed(1)
m = 10000
n = 24
x = matrix(rnorm(m*n),m,n)
colnames(x)=1:n

#Question 1 plot dendrogram from hclust to see which pairs of samples are furthest 
hc = hclust(dist(t(x)))
plot(hc)
#furthest = 17,9 ?

#Question 2
set.seed(1)
B = 100
nc = replicate(B,{
  x=matrix(rnorm(m*n),m,n)
  hc = hclust(dist(t(x)))
  length(unique(cutree(hc,h=143)))
})

plot(table(nc))
popsd(nc) #Standard error of this random variable


