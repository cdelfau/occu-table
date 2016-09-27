'''
Chloe Delfau
SoftDev1 pd8
HW03 -- ...and Now Enjoy its Contents
2016-09-27
'''

import random

#getting input from files (a csv file)
#opens and reads the csv
listList = open("csv/occupations.csv").read();
#list that splits csv file by line
occLlist = occL.split('\n')
#stores/save the last line 
lineZero = occLList[0]+",Test"
#delete line 0 from the list
del list[0]
#separate last line
lineLast = listList[len(listList)-1]+",100.00" #same for last line
#delete last line now that youve saved its content in a variable
del List[len(List)-1]

#create a dictionary
Dict = {}
#make a list of all the percentage upper bounds
upperBoundL = []
#determine your current upperbound
currentUpperBound = 0
#save your values in a second list
List2 = []

#for each line add the occupations, predicted percentage, and all values into the list
for line in List:
    #append [occupation,value,placeholder for test value
    List2.append([line.rsplit(",",1)[0],line.rsplit(",",1)[1],0])]
    #split each line by a comma
    occS = line.rsplit(",",1)[0]
    #update your current upperbound
    currentUpperBound += float(line.rsplit(",",1)[1])
    #add to the value of a particular upperbound dict key
    Dict[currentUpperBound] = occS
    #update the upperbound list
    upperBoundL.append(currentUpperBound)

#randomly pick an occupation
def pickOccupation():
    #create a random number
    rand = random.random()*99.8
    #determine ur position
    passenger = 0
    #for each line in list 2
    for line in List2:
        #grab the weighted percentage of said occupation
        percentage = float(line[1])
        #add the passenger to the position
        passenger+=percentage
        #if the random number is less than the pasenger, return the occupation
        if rand < passenger:
            #return that occupation
            return line[0]

#new dict to store how many times each occupation is picked
d = {}

#test function
def test():
    #for each line in list 2
    for line in List2: #creates each dict key, initializes each value to 0
    d[line[0]] = 0
    #run the function 10000 times and randomly pic one occ
    for num in range(10000):
        #save the chosen occupation
        chosenOne = pickOccupation()
        #add to the value of that occupaton's key
        buckets[chosenOne] += 1
        #make a new list that you will return
        rList = []

  #for each line in list 2
  for line in List2: #
      #print each occupation with weighted percentage 
      rList.append(str(d[line[0]]/1000.0))
  #return teh list to be returned
  return rList


#add and save another column that represents the actual values of the appearances certain occupations
def appendThirdColumn(o):
    #call the test function
    TestList = test()
    i = 0
    #append the test value in the new, third column
    while (i < len(List2)):
        List2[i][2] = TestList[i]
        o.append(list[i])
        i+=1

#end of the code, will helpyou test your fucncctions
def finalList():
    occTestList = [lineZero.split(",")]
    appendThirdColumn(occTestList)
    occTestList.append(lineLast.split(","))
    return occTestList
