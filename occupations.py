'''
Chloe Delfau
SoftDev1 pd8>
HW03 -- ...and Now Enjoy its Contents
2016-09-25
'''

#import flask, the template reader, and random
from flask import Flask, render_template
import random

#create an app
app = Flask(__name__)

#open the csv file
list = open("occupations.csv").read();
#in the list created, separate each element in the csv file by line
list = list.split('\n')
lineZero = occL[0]
#remove the title from the list
del list[0]
#separate the last line (empty) from the rest of thelist
lineLast = list[len(list)-1]
#remove the title from the list
del list[len(list)-1]

#create a dictionary
Dict = {}
#create a list for each percentage upper bound
upperBoundL = []
#know which upper bound you are currently in
currentUpperBound = 0
#create a list
list2 = []

#for each line in the csv as a list
for line in list:
    #add to the new list all the elements from the csv separated by commas
    list2.append(line.rsplit(",",1))
    #save each line
    occS = line.rsplit(",",1)[0]
    #add to the percentages to update the current upperbound
    currentUpperBound += float(line.rsplit(",",1)[1])
    #find the value for the key "current upper bound"
    Dict[currentUpperBound] = occS
    #add to the upper bound list each new upper bound
    upperBoundL.append(currentUpperBound)

#randomly pick an occupation
def pickOcc():
    #pick a random number between 0 and 99.8
    rand = random.random()*99.8
    #know your placement on the list
    passenger = 0
    #for each line in the list
    for line in list2:
        #determine your percentage
        percentage = float(line[1])
        #determine your placement on the list
        passenger+=percentage
        #if the random number is smaller than the "passenger"/your placement then return the first line
        if rand < passenger:
            return line[0]

#direct your app to the occupations folder
@app.route("/occupations")
#create a table with the list of occupations, their percentage 
def occTable():
    return render_template("occTable.html",occList=list2,occupation=pickOcc())

#this is just a tester/debugger
if __name__ == "__main__":
    app.debug = True
    app.run()
