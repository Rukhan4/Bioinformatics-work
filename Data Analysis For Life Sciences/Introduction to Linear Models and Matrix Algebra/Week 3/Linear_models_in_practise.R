#Practise 1 -------------------------------------------------------------------------------------------

library(downloader)
url = "https://raw.githubusercontent.com/genomicsclass
/dagdata/master/inst/extdata/femaleMiceWeights.csv"
filename = "femaleMiceWeights.csv"
if (!file.exists(filename)) download (url,filename)

dat = read.csv("femaleMiceWeights.csv")
dat
#Stripchart to visualize weights
stripchart(dat$Bodyweight~dat$Diet,
           vertical=TRUE,method="jitter",
           main="Bodyweight and Diet")

#Linear model with 1 Variable
levels(dat$Diet)
X = model.matrix(~Diet,data=dat)
X #chooses Diethf because chow is the reference/base level

#See Dietchow
dat$Diet = relevel(dat$Diet,ref="hf")
Y = model.matrix(~Diet,data=dat)
Y

#Can Use factor(x=character(),levels="hf" or chow or whatever)

#Practise 2 look at results from linear model-------------------------------------------------------------

fit = lm(Bodyweight~Diet,data=dat)
summary(fit) #in my case, summary stands on chow since i releveled dat$Diet
(coefs = coef(fit))

#OR using split method
s = split(dat$Bodyweight, dat$Diet)
mean(s[["chow"]])
mean(s[["hf"]]) - mean(s[["chow"]])

#Results we got from linear model will be equal to results obtained from t-test
summary(fit)$coefficients
s = split(dat$Bodyweight, dat$Diet)

ttest = t.test(s[["chow"]],s[["hf"]],var.equal=TRUE)
ttest
ttest$statistic
# same as : summary(fit)$coefficients[2,3]

