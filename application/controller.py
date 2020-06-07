from flask import Flask
import s3clienthelper as s3helper

# create instance of Flask
app = Flask(__name__)

bucketname = 'testBucket'
@app.route("/createbucket")
def createbucket():
    '''
    Create bucket if it does not exist
    '''
    return s3helper.createBucket('bucketname')

@app.route("/")
def index():
    '''
    Create bucket if it does not exist
    '''
    return 'Flask Application started'
