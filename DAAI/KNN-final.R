#Setup
#Session > set working directory 
setwd("~/Desktop/Warwick/DAAI/KNN-Part/")
LCA0 <- read.csv("VARIABLE_PROCESS_LCA2019.csv")
#LCA.df <- read.csv(file.choose(), header = T)

#Data processsing 
#For Y
library(sampling)
library(caret)
library(FNN)

table(LCA0$CASE_STATUS)

st = strata(LCA0, stratanames = c("CASE_STATUS"), size = c(2053,27947), method = "srswor")
LCA <- LCA0[st$ID_unit,]
LCA <- na.omit(LCA)

#Drop column 
data <- LCA[ ,-c(2,5,9)]

#data$certify <- data$CASE_STATUS== 1
#data$non_certify<- data$CASE_STATUS== 0
data$EMPLOYER_STATE <- as.numeric(factor(data$EMPLOYER_STATE))
#data$CASE_STATUS <- factor(data$CASE_STATUS,levels = c(1,0),
                             #labels = c("CERTIFIED", "NON-CERTIFIED"))
#data$INDUSTRY_CODE <- as.integer(data$INDUSTRY_CODE)
#data$EMPLOYER_STATE <- as.integer(data$EMPLOYER_STATE)
row_labels = data[,1]



#Train Test 
set.seed(111)
#Size 80/20
size <- floor(0.6 * nrow(data))
#Obtain row numbers 
train_ind <- sample(seq_len(nrow(data)), size = size) 
#Training labels (Y)
train.index <- data[train_ind , 1]
#Testing Labels (Y)
valid.index <- row_labels[-train_ind]
#Training data (X)
train.df <- data[train_ind ,]
#Testing data (X)
valid.df <- data[-train_ind ,]

#Scale our data 
# initialize normalized training, validation data, complete data frames to originals
train.norm.df <- train.df
valid.norm.df <- valid.df
data.norm.df <- data
#Small in order to quicker 
#data[,2:3] <- scale(2:3)
#Normailization 
#norm.values <- caret::preProcess(train.df[, 2:3], method=c("center", "scale")) 
#train.norm.df[, 2:3] <- predict(norm.values, train.df[, 2:3])
#valid.norm.df[, 2:3] <- predict(norm.values, valid.df[, 2:3])
#data.norm.df[, 2:3] <- predict(norm.values, data.df[, 2:3])
norm.values <- caret::preProcess(train.df[, c(3,5,7)], method=c("center", "scale")) 
train.norm.df[, c(3,5,7)] <- predict(norm.values, train.df[, c(3,5,7)])
valid.norm.df[, c(3,5,7)] <- predict(norm.values, valid.df[, c(3,5,7)])
data.norm.df[, c(3,5,7)] <- predict(norm.values, data[, c(3,5,7)])
#new.norm.df <- predict(norm.values, new.df)

#Model run
predictions <- knn(train = train.norm.df, test = valid.norm.df, 
          cl = train.norm.df[,1], k = 2)


# initialize a data frame with two columns: k, and accuracy.
accuracy.df <- data.frame(k = seq(1, 14, 1), accuracy = rep(0, 14))

for(i in 1:14) {
  knn.pred <- knn(train.norm.df[, ], valid.norm.df[,], 
                  cl = train.norm.df[, 1], k = i)
  accuracy.df[i, 2] <- confusionMatrix(knn.pred, as.factor(valid.norm.df[, 1]))$overall[1] 
}
accuracy.df



knn.pred <- knn(train.norm.df[, ], valid.norm.df[,], 
                cl = train.norm.df[, 1], k = 2)
confusionMatrix(knn.pred, as.factor(valid.norm.df[, 1]))

