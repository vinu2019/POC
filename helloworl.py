from flask import Flask,request
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():

  if request.method=='POST':
    response=request.json
    return f'Hello {response["name"]}'
  return "Hello World"
