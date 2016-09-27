#Chloe Delfau
#SoftDev1 pd8
#HW02 -- Fill Your Flask
#2016-09-20  

pip install flask
virtualenv chloe
cd..
. chloe/bin/activate
pip install flask

@app.route("/") #Makes hello_world show up when the root folder ("/") of the server is accessed by a user
def hello_world():
    return "hello"

def goodbye_world():
    return "goodbye"

def hey():
    return "hey"

@app.route("/127.0.0.1:5000/hello") #app route for hello
@app.route("/127.0.0.1:5000/goodbye") #app route for goodbye
@app.route("/127.0.0.1:5000/hey") #app route for hey

deactivate
