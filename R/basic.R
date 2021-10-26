#Jedlueng 26 Oct 2021 
#Source: WBS AI 
#Set working directory 
#Session > set working directory 
setwd("~/Documents/GitHub/MISDI-WBS-Programming/R")

#Choose your dataset 
mydata <- read.csv(file.choose(), header = T)

#Summary of all data frame 
summary(mydata)

#Find out missing data 
rowSums(is.na(mydata))
colSums(is.na(mydata))

#Create a subset > drop all missing value (Delete all the missing value)
#Create a new variable 
mydata1 <- na.omit(mydata)


#New package > Need to install it 
#Using tools > Install package 
#Load package here 
library(pastecs)

#Summarize your data-frame with descriptive statisitics 
stat.desc(mydata)

#Formular 
#Okay so use $ to choose the row.
#No missing value please 
mean(mydata1$Height)
median(mydata1$Height)
var(mydata1$Height)
sd(mydata1$Height)
max(mydata1$Height)
min(mydata1$Height)
range(mydata1$Height)
quantile(mydata1$Height)

#Visualization plot(x,y)
#Always use this logic 
plot(mydata$Length, mydata$Weight)
plot(mydata$Height, mydata$Weight)
#Okay, So this is how to change the name (X,Y)
plot(mydata$Length, mydata$Weight)

#To smooth the line and change the color (lowess)
lines(lowess(mydata$Length, mydata$Weight), col ="green")
#Create a line that connect 
lines(mydata$Length, mydata$Weight, col = "green")


#Clear plots using broom icon 


#Create histrogram 
hist(mydata$Height)

#Create box plot 
boxplot((mydata$Height))



#for scatterplot 
#Install library first
library(rgl)
library(car)
scatter3d(x = mydata$Length, y = mydata$Weight , z = mydata$Height, surface = F)


#Linear regression 
result = lm(mydata$Weight ~ mydata$Height + mydata$Length)
summary(result)
 


