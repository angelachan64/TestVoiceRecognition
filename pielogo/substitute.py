#-----------------------------------------------------
#   substuitute.py
#   This serves as the macro sustitution for the
#   regular expression of the outcome of Eliza
#-----------------------------------------------------

import string
import csv
import sys
import re

def TurnToList():
       reader = csv.reader(file('/Users/bambool/Documents/Eliza/regular.csv', 'rb'))
       NewList=[]
       for item in reader:
              NewList.append(item)
       NewList=NewList[0]
                           
       return NewList
'''
def substitute(dict):
       dd=[]
       NewDict=dictionary
       RevertDict={}
       time=""
       for k,v in NewDict.iteritems():
               RevertDict[v]=k
       count=1
       limit=0
       while (limit<50):
                     limit+=1
              
                     
                     item=NewDict.values()[count]
                     if count<(len(NewDict.values())-1):
                            count+=1
                     else :
                            count=1
                    
                     if re.match(r'\w*{\d*}',item):
                            times=filter(str.isdigit, item)
                            time="{"+times+"}"
                            character=filter(str.isalpha, item)
                            NewItem=NewDict[character]+time
                            NewDict[RevertDict[item]]=NewItem
                            print NewItem
                     if re.match(r'\w*and\w*',item):
                            dd=item.split('and')
                            NewItem=NewDict[dd[0]]+NewDict[dd[1]]
                            NewDict[RevertDict[item]]=NewItem
                            print NewItem
                     
                     if re.match(r'\w*[\+\-\*\\]\w*',item):
                            dd=re.split('\=|\+|\-|\*',item)
                            for kk in dd:
                                   if kk in NewDict.keys():
                                          item.replace(kk,NewDict[kk])
                                          

                            



       
                                   
                            
                     
       return NewDict
                            
                            
       
 '''

def substitute(list):
       i=-1
       for command in List:
              
              i+=1
#delete
              if re.search(r'delete last',command):
                     DNumber=int(filter(str.isdigit, command))
                     print len(List)

                     for n in range(i-DNumber,len(List)-DNumber-1):
                            List[n]=List[n+DNumber+1]
                            
                     for m in range(len(List)-DNumber-1,len(List)-1):
                            del List[m]
                     del List[-1]
                    
                                         
#repeat replacement
              if re.search(r'repeat',command):
                     key=""
                     key2=""
                     if re.search(r'\[\w*\]',command):
                            key=command[command.find("[")+1:command.find("]")]
                            key2="to "+key
                            for n in List:
                                   if re.search(key2,n):
                                          value=n.split(key2)[1].split("end")[0]
                                          List[i]=re.sub(key,value,List[i])
                     if command.find("]")==-1:
                            Total=""
                            for n in range(i,len(List)):
                                   if List[n]=="]":
                                          break
                            for m in range(n-i-1):
                                   Total=Total+List[m+1+i]+" "
                            List[i]=List[i]+Total+"]"
                            for s in range(i+1,len(List)-(n-i)):
                                   List[s]=List[s+(n-i)]
                            for s in range(i-n,0):
                                   del List[s]
                            
                                   
                            
                            
                                          
                            
                     
                     
#last replacement
              if re.search(r'last',command):
                     CNumber=int(filter(str.isdigit, command))
                     Total=""
                     for n in range(CNumber):
                             Total=Total+List[i-CNumber+n]+" "
                     List[i]=re.sub(r'last\d*',Total,List[i])
                     
#follow replacement
              if re.search(r'follow',command):
                     CNumber=int(filter(str.isdigit, command))
                     Total=""
                     for n in range(CNumber):
                             Total=Total+" "+List[i+n]
                     List[i]=re.sub(r'follow\d*',Total,List[i])

#



       return List
                     
'''                    
#definition
              if re.search(r':',command):
                     key=command.split(":")[0]
                     value=command.split(":")[1]
                     for i in List:
                             if re.search(r':',i):
                                    if re.search(i.split(":")[0],value):
                                           command.replace(i.split(":")[0],i.split(":")[1])
                                          

'''            


       
                                           
                                           
                                           
                                           
                                   
                     
                     
                     
       

       
       
if __name__ == "__main__":
       
      List=TurnToList()
      print List
      New=substitute(List)
      
       

       
       
       


       


              


       


       

       
              
       


