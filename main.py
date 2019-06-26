from flask import Flask, request


app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <title>"User Signup"</title>
    </head>
    <body>
      <form method="POST">
        <label for="Username">Username:</label>
  		<input type="text" name="Username" id="Username" required>
        <br>
        <label for="Password">Password:</label>
  		<input type="password" name="Password" id="Password" required>
        <br>
        <label for="Verify">Verify:</label>
  		<input type="password" name="Verify" id="Verify" required>
        <br>
        <label for="email">Email(optional):</label>
  		<input type="text" name="email" id="email" >
        <br>



        
        <input type="submit" value="Submit">
           
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

app.run()