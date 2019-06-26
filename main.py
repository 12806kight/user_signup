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

        <br><br>





        <input type="submit" value="Submit">
           
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return user_form.format(username='', username_error='', password='', password_error='')

@app.route("/", methods=['POST'])
def validate():

    username = request.form['username']
    password = request.form['password']

    username_error = ''
    password_error = ''

    if len(username) < 3 or len(username) > 30:
      username_error = 'Username should be inbetween 2 to 30 letters'
      username = ''

    if len(password) < 3 or len(password) > 30:
      password_error = 'Password Error'
      password = ''

    if not username_error and not password_error:
      return "Welcome, {{username}}"
    else: 
      return user_form.format(username_error=username_error, password_error=password_error, username=username, password=password)
app.run()