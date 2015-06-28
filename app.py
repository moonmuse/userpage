from flask import Flask, render_template,json, request
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash


mysql=MySQL()
app = Flask(__name__)


mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '510613'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('index.html')

      
@app.route('/signUp',methods=['POST','GET'])
def signUp():
  if request.method=='POST':
    _name = request.form['user']
    _email = request.form['email']
    _password = request.form['pwd']
    
    if _name and _email and _password:
       conn=mysql.connect()
       cursor=conn.cursor()
       cursor.execute("INSERT into tbl_user(user_name,user_username,user_password)VALUES('" + _name + "','"+_email+"','"+_password+"')")
       conn.commit()
       return "Create User Successfully!"
    else:
       return "Please fill all the fields"
  else:
    return 0

@app.route('/login', methods=['POST','GET'])
def register():
    if request.method=='POST':
       _name = request.form['user']
       _pwd=request.form['pwd']

       if _name and _pwd:
          conn=mysql.connect()
          cursor=conn.cursor()
          cursor.execute("SELECT * from tbl_user where user_name='"+_name+"'and user_password='"+_pwd+"'")
          data=cursor.fetchone()
          if data is None:
                return "Username or Password is wrong"
          else:
                return "You are logged in"
       else:
          return "Please fill all the fileds"
    else:
       return 0

@app.route('/showSignUp/',methods=['POST','GET'])
def showSignUp():
    return render_template('signup.html')

@app.route('/showSignIn/', methods=['POST','GET'])
def showSignIn():
    return render_template('signin.html')


@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from tbl_user where user_name='" + username + "' and user_password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"

    
if __name__ == "__main__":    
     app.run()
