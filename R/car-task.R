#Jedlueng 26 oct 2021
setwd("~/Documents/GitHub/MISDI-WBS-Programming/R/Dataset")
library(dplyr)
library(geosphere)

mydata <- read.csv(file.choose(), header = T)

mydata1 <- na.omit(mydata)


mydata1 <- mutate(mydata1, distance = distHaversine(cbind(mydata1$start.station.longitude,mydata1$start.station.latitude),cbind(mydata1$end.station.longitude, mydata1$end.station.latitude)))


#Scatter plot 
plot(mydata1$distance,mydata1$tripduration, col = 'blue',main = "Trip Duration AGAINST Distance(Scatter plot)", xlab = "Distance" , ylab = "Duration")
lines(lowess(mydata1$distance,mydata1$tripduration), col ="green")

library(rgl)
library(car)
scatter3d(x = mydata$Length, y = mydata$Weight , z = mydata$Height, surface = F)

#Line plot 
plot(mydata1$distance,mydata1$tripduration , type = "l", lty = 1 ,col = 'blue', main = "Trip Duration AGAINST Distance(Line Plot)", xlab = "Distance" , ylab = "Duration")
lines(lowess(mydata1$distance,mydata1$tripduration ), col ="green")

#Linear Regression 
plot(mydata1$distance,mydata1$tripduration , pch = 16, cex = 1.3, col = "blue", main = "Trip Duration AGAINST Distance(Linear-Regression)", xlab = "Trip-Duration", ylab = "Distance")
lm(mydata1$distance ~ mydata1$tripduration,)
abline(398.8847, 0.3145)




