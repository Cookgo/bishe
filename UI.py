#! -*- coding:utf-8 -*-
from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template('home.html')
                  
@app.route('/', methods=['POST'])
def proc():
    IP=request.form['IP']
    print(IP)
    return IP





if __name__ == '__main__':
    app.run()