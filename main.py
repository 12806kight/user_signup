from flask import Flask, request, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/", methods=['POST'])
def validate():

    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']

    username_error = ''
    password_error = ''
    password2_error=''
    email_error = ''

    if len(username) < 3 or len(username) > 20:
      username_error = 'Username should be inbetween 2 to 30 letters'
      username = ''

    if len(password) < 3 or len(password) > 20:
      password_error = 'Password Error'
      password = ''

    if password2 != password:
      password2_error = 'Passwords must match'
      password2_error = ''
    
    if len(email) < 3 or len(email) > 20:
      email_error = 'Not a valid email'
      email = ''
    if '@' not in email or '.' not in email or ' ' in email:
      email_error = 'Not a valid email'
    
    if not username_error and not password_error and not password2_error and not email_error:
      return render_template('welcome.html',username=username) 
    else: 
      return render_template('home.html', username_error=username_error, password_error=password_error, username=username, password=password, password2=password2, password2_error=password2_error, email=email, email_error=email_error)
app.run()