from flask import Flask, render_template, request, send_file,redirect,url_for, Response, redirect
import sys
import os
import base64

app = Flask(__name__,static_folder="static", template_folder="templates")




@app.route('/', methods=['GET','POST'])

def Menu_func():

    PASS_TO_APP = os.environ['PASS_TO_APP'] 
    
    #encoded = base64.b64encode(b'data to be encoded')
    #print(encoded)

    #decoded = base64.b64decode(PASS_TO_APP)
    #login = decoded.decode("utf-8")


    return render_template('Frontpage.html' ,decoded_value = PASS_TO_APP)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8800)

