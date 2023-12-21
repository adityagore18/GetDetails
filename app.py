from flask import Flask, request, redirect, url_for, render_template, session, send_file
import io

app = Flask(__name__)
@app.route('/')
def main():
   return render_template('index.html')

@app.route('/getDetails' , methods=['POST'])
def getDetails():
   name = request.form['name1']
   address = request.form['address']
   gender = request.form['gender']
   education=request.form['education']
   college_name = request.form['college_name']
   branch = request.form['branch']
   feature_enabled = request.form.get('c')


   if feature_enabled:

      c = "C/C++"
   else:

      c=""
   feature_enabled1 = request.form.get('Java')


   if feature_enabled1:

      java="Java"
   else:

      java=""
   feature_enabled3 = request.form.get('c')


   if feature_enabled3:

      python="Python"
   else:

      python=""


   email=request.form['email']
   mobno = request.form['mobno']
   return render_template('getDetails.html',name=name,address=address,gender=gender,education=education,college_name=college_name,branch=branch,c=c,java=java,python=python,email=email,mobno=mobno)


