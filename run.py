#7/24/2019
from fortunesite import app


#If run from the command line with python script.py, this will run flask to stand up a temp dev webserver
#Run this application in debug mode so changes are visible without restarting the www server
if __name__ == '__main__':
    app.run(debug=True)
