#Exercise 1

babies <- read.table("babies.txt", header=TRUE)
bwt.nonsmoke <- filter(babies, smoke==0) %>% select(bwt) %>% unlist 
bwt.smoke <- filter(babies, smoke==1) %>% select(bwt) %>% unlist

N=12
set.seed(1)
nonsmokers <- sample(bwt.nonsmoke , N)
smokers <- sample(bwt.smoke , N)
obs <- mean(smokers) - mean(nonsmokers)

dat <- c(smokers,nonsmokers)
shuffle <- sample( dat )
smokersstar <- shuffle[1:N]
nonsmokersstar <- shuffle[(N+1):(2*N)]
mean(smokersstar)-mean(nonsmokersstar)

#Actual code
N <- 12
avgdiff <- replicate(1000, {
  all <- sample(c(smokersstar,nonsmokersstar))
  smokersstar <- all[1:N]
  nonsmokersstar <- all[(N+1):(2*N)]
  mean(nonsmokersstar) - mean(smokersstar)
})
hist(avgdiff)
abline(v=obs, col="red", lwd=2)

v = (sum(abs(avgdiff) > abs(obs)) + 1) / (length(avgdiff) + 1)
v

#Exercise 2 #BULLLSHITTTTTT

babies <- read.table("babies.txt", header=TRUE)
bwt.nonsmoke <- filter(babies, smoke==0) %>% select(bwt) %>% unlist 
bwt.smoke <- filter(babies, smoke==1) %>% select(bwt) %>% unlist

N=12
set.seed(1)
nonsmokers <- sample(bwt.nonsmoke , N)
smokers <- sample(bwt.smoke , N)
obs <- median(smokers) - median(nonsmokers)

dat <- c(smokers,nonsmokers)
shuffle <- sample( dat )
smokersstar <- shuffle[1:N]
nonsmokersstar <- shuffle[(N+1):(2*N)]
median(smokersstar)-median(nonsmokersstar)

#Actual code
N <- 12
avgdiff <- replicate(1000, {
  all <- sample(c(smokersstar,nonsmokersstar))
  smokersstar <- all[1:N]
  nonsmokersstar <- all[(N+1):(2*N)]
  median(nonsmokersstar) - median(smokersstar)
})
hist(avgdiff)
abline(v=obs, col="red", lwd=2)

v = (sum(abs(avgdiff) > abs(obs)) + 1) / (length(avgdiff) + 1)
v
