############ Version 1

# This one is older and looks a bit more laborious, but generates a monte carlo sample for each language, 
# so you get a z score as well as the raw correlation - montecomp returns more info about the properties of the sample - you 
# might just want the raw correlation though. It is also a bit minging in that it is hard-wired around 16 meanings (4 combinations of 
# shapes and fill patterns) and their associated forms.

#normalised Levenstein distance
normdist <- function(x,y) {
  stringdist::stringdist(x,y,method="lv")/max(nchar(x),nchar(y))
}
# compute pairwise levenstein string distance between x and y, then divide by the length of the larger element


#First step: for each chain and each generation, calculate all pairwise meaning distances and the distance between the associated forms

#first of all, measures of distance between meanings and signals
simple.mdist <- function(m1,m2) {
  (m1$Shape!=m2$Shape) + (m1$Fill!=m2$Fill)}
# ie are they the same shape (0), and do they have the same fill pattern (0)

#data is the data for a particular individual you want to work with
#will use the row number in the data as an index for the meanings and signals
all.pairs.distances.table <- function(data) {
  l <-nrow(data)
  meaning.pairs<-unlist(sapply(1:(l-1),function(x) sapply((x+1):l,function(y) c(x,y))))
  meanings<-data[c("Shape","Fill")]
  meaning.distances<-unlist(sapply(1:(l-1),function(x) sapply((x+1):l,function(y) simple.mdist(meanings[x,],meanings[y,]))))
  
  signal.distances<-unlist(sapply(1:(l-1),function(x) sapply((x+1):l,function(y) normdist(data[x,'Label'],data[y,'Label']))))
  
  distance.matrix <- matrix(meaning.pairs,ncol=2,byrow=TRUE)
  colnames(distance.matrix)<-c("M1","M2")
  distance.matrix<-cbind(distance.matrix,meaning.distances,signal.distances)
  
  data.frame(distance.matrix)
}


#functions which use the distance table
mdist <- function(distance.table,m1,m2) {
  subset(distance.table,(M1==m1 & M2==m2) | (M1==m2 & M2==m1))$meaning.distance}

sdist <- function(distance.table,m1,m2) {
  subset(distance.table,(M1==m1 & M2==m2) | (M1==m2 & M2==m1))$signal.distance}

#ok, so now can look up meaning distances using the table
all.pairs.mdist <- function(distance.table,meanings) {
  l <-length(meanings)
  unlist(sapply(1:(l-1),function(x) sapply((x+1):l,function(y) mdist(distance.table,meanings[x],meanings[y]))))
}

all.pairs.sdist <- function(distance.table,signals) {
  l <-length(signals)
  unlist(sapply(1:(l-1),function(x) sapply((x+1):l,function(y) sdist(distance.table,signals[x],signals[y]))))
}

# data is a list of rows for this chain, this generation
montecomp <- function(data,trials) {
  distance.table <- all.pairs.distances.table(data)
  veridical.meanings <- 1:16
  veridical.forms <- 1:16
  m.dists<- all.pairs.mdist(distance.table,veridical.meanings)
  s.dists <- all.pairs.sdist(distance.table,veridical.forms)
  veridical <- cor(m.dists,s.dists,use='complete.obs') #handles missing data in correlation
  if (is.na(veridical)) {
    return(list(mean=NA,sd=NA,veridical=NA,p=NA,z=NA))
  }
  else {
    msample <- replicate(trials,cor(m.dists,all.pairs.sdist(distance.table,sample(veridical.forms)),use='complete.obs'))
  # ok i think this is saying "return a list of length(trials) (IE the number of simulations) containing the correlations 
  # between the meaning distances for each pair of meanings and a random sample of their signal distances"
  # effectively scrambling which meaning distances correspond with which signal distances and breaking any correlation between
  # meaning distance and signal distance (of which we should expect some)
    
    c=0
    #print(msample)
    for (i in 1:trials) {
      if(msample[i]>=veridical) c=c+1
    }
    return(list(mean=mean(msample),sd=sd(msample),veridical=veridical,p=c/trials,z=(veridical-mean(msample))/sd(msample)))
  }
}

MCTrials=1000

#make a language to test on
#NB it's only the "Label" column we care about
compositional.lang <- data.frame("Shape"=rep(c("1","2","3","4"),each=4),
                                 "Fill"=rep(c("1","2","3","4")),
                                 "ShapeLabel"=rep(c("a","b","c","d"),each=4),
                                 "FillLabel"=rep(c("w","x","y","z")))
compositional.lang$Label <- paste(compositional.lang$ShapeLabel,compositional.lang$FillLabel,sep="")

montecomp(compositional.lang,100)

#NA values for labels are allowed and are just ignored
compositional.lang.missing <- compositional.lang
compositional.lang.missing[1,"Label"] <- NA
compositional.lang.missing[2,"Label"] <- NA
compositional.lang.missing[3,"Label"] <- NA
montecomp(compositional.lang.missing,100)

############ Version 2

#This one is more compressed - I guess I figured out how to use stringdist::stringdistmatrix, but also in this one the 
#meanings are a list of meanings and the forms are the associated forms in the same order. 
#but it doesn't do z-scoring, just returns raw correlation (but it would be easy to get a z-score using the same 
#sample labels method as above)

# m = meanings
# f = forms
# both are vectors, indexes matched
# so m[1] is the meaning associated with the form f[1]

structure_score <- function(m,f) {
  meaning_distances <- stringdist::stringdistmatrix(m,m,method='hamming')
  dists_df <- data.frame()
  for (m1 in 1:(length(m)-1)) {
    for (m2 in (m1+1):length(m)) {
      #print(paste(m1,m2))
      m_dist <- meaning_distances[m1,m2]
      form1 <- f[m1]
      form2 <- f[m2]
      f_dist <- normdist(form1,form2) # get the normalised lv distance between the two forms
      dists_df <- rbind(dists_df,data.frame("m1"=m1,"m2"=m2,"meaning1"=m[m1],"meaning1"=m[m2],"f1"=form1,"f2"=form2,"m_dist"=m_dist,"f_dist"=f_dist))
    }
  }
  print(dists_df) #uncomment if you want to see the distance matrix
  cor(dists_df$m_dist,dists_df$f_dist,use='complete.obs')
}

#create the slightly different meaning representation required
compositional.lang$Meaning <- paste(compositional.lang$Shape,compositional.lang$Fill,sep='')

structure_score(compositional.lang$Meaning,compositional.lang$Label)

structure_score(compositional.lang$Meaning,compositional.lang.missing$Label)


