import face_recognition
import cv2
import numpy as np
from flask import Flask, render_template ,request
from db_function import get, add_item
app = Flask(__name__)




@app.route('/')
def index():
   return render_template('index.html')

@app.route('/add', methods = ['POST', 'GET'])
def add():
    name=request.form['fname']
    return render_template('success.html',name=name)

@app.route('/attendance',)
def attendance():
   item = get()
   return render_template('attendance.html',item=item)

if __name__ == '__main__':
   app.run(debug = True)      