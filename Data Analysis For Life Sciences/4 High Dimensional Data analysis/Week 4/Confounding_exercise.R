library(dagdata)
data(admissions)
print(admissions)

#Question 1 proportion of men accepted
index = which(admissions$Gender==1)
accepted= sum(admissions$Number[index] * admissions$Percent[index]/100)
applied = sum(admissions$Number[index])
accepted/applied
#Women accepted
index = which(admissions$Gender==0)
accepted= sum(admissions$Number[index] * admissions$Percent[index]/100)
applied = sum(admissions$Number[index])
accepted/applied

#Question 2 chi-square independance test for p-value
index=admissions$Gender==1
men = admissions[index,]
women=admissions[!index,]
menYes = sum(men$Number*men$Percent/100)
menNo = sum(men$Number*(1-men$Percent/100))
womenYes = sum(women$Number*women$Percent/100)
womenNo = sum(women$Number*(1-women$Percent/100))
tab = matrix(c(menYes,womenYes,menNo,womenNo),2,2)
chisq.test(tab)$p.value
#NB looking at the data by major the difference disappears:
index = admissions$Gender==1
men = admissions[index,]
women = admissions[!index,]
print( data.frame( major=admissions[1:6,1],men=men[,3], women=women[,3]) )

#Question 3 hardest major
major = admissions[1:6,1]
men = admissions[1:6,]
women = admissions[7:12,]
H = (men$Number*men$Percent/100 + women$Number*women$Percent/100)/(men$Number+women$Number)
major[which.min(H)]

#Question 4 proportion students admitted to F major
min(H)

#Question 5 correlation between no. applications across majors and H for men
cor(H,men$Number)

#Question 6 
cor(H,women$Number)

