from flask import Flask, render_template ,request
from db_function import get_item, add_item
from name_function import add_student, get_student
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/add', methods = ['POST', 'GET'])
def add():
   name=request.form['fname']
   item = get_student()
   student =[]
   for i in item:
      for j in i:
         student.append(j)
   if name not in student:
      add_student(name)
   return render_template('success.html',name=name)

@app.route('/attendance',)
def attendance():
   item = get_item()
   return render_template('attendance.html',item=item)

if __name__ == '__main__':
   app.run(debug = True)      