dat <- read.csv("femaleMiceWeights.csv")
dat[12,2]
dat$Bodyweight
dat[11,]
weights <- dat$Bodyweight
length(weights)
mean(weights[13:24])
set.seed(1)
sampler <- sample(13:24,1)
dat$Bodyweight[sampler]
