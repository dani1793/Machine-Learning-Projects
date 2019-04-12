library(dplyr)
list.files()
pf <- read.csv('cup98LRN.txt', header = TRUE, stringsAsFactors = FALSE)
names(pf)
head(pf)
names(pf)

table(pf$ODATEDW)
count(pf)

length(pf$CONTROLN)
count(pf)

# 7. Each record has a unique record identifier or index (field name: CONTROLN.) For each record, there are two target/dependent variables
# (field names: TARGET_B and TARGET_D). TARGET_B is a binary variable
# indicating whether or not the record responded to the promotion of
# interest ("97NK" mailing) while TARGET_D contains the donation amount
# (dollar) and is only observed for those that responded to the
# promotion.

# https://www.kdd.org/cupfiles/KDDCupData/1998/cup98dic.txt


# CONTROLN                    Control number (unique record identifier)
# 
# TARGET_B                    Target Variable: Binary Indicator for Response to 97NK Mailing
# TARGET_D                    Target Variable: Donation Amount (in $) associated with the Response to 97NK Mailing
# 
# HPHONE_D                    Indicator for presence of a published home phone number 


prunedPf <- pf[c( 'ADATE_2', 'ADATE_3', 'ADATE_4', 'ADATE_5', 'ADATE_6', 'ADATE_7', 'ADATE_8', 'ADATE_9', 'ADATE_10',
                  'ADATE_11', 'ADATE_12', 'ADATE_13', 'ADATE_14', 'ADATE_15', 'ADATE_16', 'ADATE_17', 'ADATE_18', 'ADATE_19',
                  'ADATE_20', 'ADATE_21', 'ADATE_23', 'ADATE_24',
                  'RFA_2', 'RFA_3', 'RFA_4', 'RFA_5', 'RFA_6', 'RFA_7', 'RFA_8', 'RFA_9', 'RFA_10', 'RFA_11', 'RFA_12',
                  'RFA_13', 'RFA_14', 'RFA_15', 'RFA_16', 'RFA_17', 'RFA_18', 'RFA_19', 'RFA_20', 'RFA_21', 'RFA_22', 'RFA_23',
                  'RFA_24' , 'CONTROLN', 'TARGET_B', 'TARGET_D', 'HPHONE_D')]
count(prunedPf)

convertRFAToState <- function (rfa) {
  # print(rfa)
  if(is.na(rfa) || is.null(rfa)) {
    return(0)
  } else {
    letter = substr(rfa, 1, 1)  
    if(letter == 'I' || letter == 'L') {
      return(0)
    }
    if(letter == 'F' || letter == 'N' || letter == 'A') {
      return(1)
    } 
    if(letter == 'S') {
      return(2)
    }
  }
  return(0)
}

getColName <- function(ind) {
  return(paste('RFA_', as.character(ind) , sep=''))
}


convertRecords <- function(df) {
  for(i in 1:nrow(df)) {
    if(i%%5000 == 0) {
      print(paste('percentage completed',as.character(i/nrow(df))));
    }
    for(j in 2:24) {
      df[i,getColName(j)] = convertRFAToState(df[i,getColName(j)])
    }
  }
  return(df)
}

prunedCopy <- data.frame(prunedPf, stringsAsFactors=FALSE)

transforedPrune <- readRDS('transforedPrune.rds')
#nrow(prunedCopy)
#transforedPrune <- convertRecords(prunedCopy)
#head(transforedPrune)

# Inactive doner || '' (Dont Care) 0
# LAPSING DONOR || FIRST TIME DONOR || NEW DONOR (Interested) 1
# STAR DONOR STAR (Very Interested) 2
# Target B is true (Meeting => highest points) => not yet maybe => goal 3
#saveRDS(transforedPrune, "transforedPrune.rds")
smallpf <- prunedPf[1:20,]


getTransitionType <- function (past, current) {
    if (past == 0 && current == 0) {
      return('dctodc')
    } 
    if(past == 0 && current == 1) {
      return('dctoi')
    }
    if(past == 0 && current == 2) {
    return('dctovi')
    }
  
    if (past == 1 && current == 0) {
      return('itodc')
    } 
    if(past == 1 && current == 1) {
      return('itoi')
    }
    if(past == 1 && current == 2) {
      return('itovi')
    }
  
    if (past == 2 && current == 0) {
      return('vitodc')
    } 
    if(past == 2 && current == 1) {
      return('vitoi')
    }
    if(past == 2 && current == 2) {
      return('vitovi')
    }
}

# create a dataframe with transition probabilities
transitionDataFrame <- function(df) {
  transitionDF <- data.frame('id'= 0, 'TARGET_B' = 0, 'TARGET_D' = 0,'dctodc' = 0, 'dctoi' = 0, 'dctovi' = 0, 'itodc' = 0, 'itoi' = 0, 'itovi' = 0, 'vitodc' = 0, 'vitoi' = 0, 'vitovi' = 0)  
  for(i in 1:nrow(df)) {
  #for(i in 1:10) {
    if(i%%5000 == 0) {
      print(paste('percentage completed',as.character(i/nrow(df))));
    }
    transitionDF<- rbind(transitionDF, data.frame('id'= df[i,'CONTROLN'], 'TARGET_B' = df[i,'TARGET_B'], 'TARGET_D' = df[i,'TARGET_D'], 'dctodc' = 0, 'dctoi' = 0, 'dctovi' = 0, 'itodc' = 0, 'itoi' = 0, 'itovi' = 0, 'vitodc' = 0, 'vitoi' = 0, 'vitovi' = 0))
    currentState = df[i,'RFA_24']                     
    for(j in 23:2) {
      transitionDF[i +1, getTransitionType(currentState, df[i,getColName(j)])] = transitionDF[i +1, getTransitionType(currentState, df[i,getColName(j)])] + 1
      currentState = df[i,getColName(j)]
    }
    transitionDF[i+1, c('dctodc', 'dctoi', 'dctovi', 'itodc', 'itoi', 'itovi', 'vitodc', 'vitoi', 'vitovi') ]= transitionDF[i+1, c('dctodc', 'dctoi', 'dctovi', 'itodc', 'itoi', 'itovi', 'vitodc', 'vitoi', 'vitovi')]/sum(transitionDF[i+1, c('dctodc', 'dctoi', 'dctovi', 'itodc', 'itoi', 'itovi', 'vitodc', 'vitoi', 'vitovi')])
  }
  return(transitionDF)
}
transitionProb <- readRDS('transitionProb.rds')
transitionProb <- transitionDataFrame(transforedPrune)
# transitionProb <- transitionCounts[-1,]
saveRDS(transitionProb, "transitionProb.rds")

positiveRes <- subset(transitionProb, TARGET_B == 1)
negRes <- subset(transitionProb, TARGET_B != 1)
