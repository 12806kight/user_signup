from flask import Flask, request


app = Flask(__name__)
app.config['DEBUG'] = True


user_form = """
<!DOCTYPE html>

<html>
    <head>
        <title>"User Signup"</title>
    </head>
    <body>
      <form method="POST">
        <label>Username:
          <input name="username" type="text" value='{username}' required>
        </label>
        <p>{username_error}</p>
        <br><br>
        <label>Password:
          <input name="password" type="text" value='{password}' required>
        </label>
        <p>{password_error}</p>
        <br><br>
        <label>Password2:
          <input name="password2" type="text" value='{password2}' required>
        </label>
        <p>{password2_error}</p>
        <br><br>
        <label>Email(optional):
          <input name="email" type="text" value='{email}'>
        </label>
        <p>{email_error}</p>
        <br><br>

        <input type="submit" value="Submit">
           
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return user_form.format(username='', username_error='', password='', password_error='', password2='', password2_error='', email='', email_error='')

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
    if '@' not in email:
      email_error = 'Not a valid email'
    if '.' not in email:
      email_error = 'Not a valid email'
    if ' ' in email:
      email_error = 'Not a valid email'      
     
    
    if not username_error and not password_error and not password2_error and not email_error:
      return "Success"
    else: 
      return user_form.format(username_error=username_error, password_error=password_error, username=username, password=password, password2=password2, password2_error=password2_error, email=email, email_error=email_error)
app.run()