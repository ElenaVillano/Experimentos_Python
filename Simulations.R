#Document to see how is super or sub additivity in data. 
rm(list = ls())



data_tiempo <- read.csv('~/Documents/Experimentos_Python/sujeto_adju_tiempo2.csv')

choices <- data_tiempo$choices
acuta <- array(dim=c(1,nrow(data_tiempo)))
for(i in 1:nrow(data_tiempo)){
 if(choices[i]=='A'){
  acuta[i] <- 0
 }
 else{
  acuta[i] <- 1
  }
}


t_s <- seq(1,140,7)
t_l <- seq(7,140,7)



plot(0,type='n',xlim=c(1,10),ylim=c(0,400))
for(o in 1:10){
set4 <- data_tiempo$smaller_money[t_s[o]:t_l[o]]
ele <- acuta[t_s[o]:t_l[o]]

for(j in 1:7){
 if(ele[j]==0){
  points(o,set4[j],pch='_',col='blue')
 }
 if(ele[j]==1){
  points(o,set4[j],pch='_',col='red')
 }
}
}

plot(0,type='n',xlim=c(11,20),ylim=c(0,4000))
for(o in 11:20){
 set4 <- data_tiempo$smaller_money[t_s[o]:t_l[o]]
 ele <- acuta[t_s[o]:t_l[o]]
 
 for(j in 1:7){
  if(ele[j]==0){
   points(o,set4[j],pch='_',col='blue')
  }
  if(ele[j]==1){
   points(o,set4[j],pch='_',col='red')
  }
 }
}

