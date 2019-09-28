from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)

#creates String of 26 random characters
app.secret_key = os.urandom(26)

#session['username'] = "user1"

#initial login page will render form if not logged in already, and will render a greeting otherwise
@app.route("/")
def root():
    if in_session():
        return render_template("index.html")
    return render_template("notloggedin.html")

@app.route("/authenticate", methods=["GET", "POST"])
def auth():
    print(len(request.form))
    if in_session():
        return render_template("index.html")
    if len(request.form) < 2:
        return render_template("index.html")
    print("adding to session")
    session['username'] = request.form.get('inputEmail')
    session['password'] = request.form.get('inputPassword')
    print(session.keys())
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    #initializes username
    username = ""
    #"username" is the key that would be in the session dictionary if the user is logged in after inputting data into the form
    if in_session():
        #username = session["username"]
        #return the greeting page if the user is logged in
        return render_template("greet.html", username= "John")
    #return the login page if thet are not
    return render_template("login.html") #, username = username)

#woo will check to see the inputted username and password combination match the one on record
@app.route("/woo", methods=["GET","POST"])
def logged():
    #print(len(request.form))
    #if someone is currently in session, it logs them out after the form is filled
    if in_session():
        session.pop("username")
    username = request.form["username"]
    password = request.form["password"]

    #poo is our account username, and pee is the respective password
    if(username == "poo" and password == "pee"):
        session["username"] = username
        #if both username and password match, show them the greet page
        return render_template("greet.html", username= username)
    #tell user their username is wrong if it does not match
    if(username != "poo"):
        return "Your <b>username</b> is incorrect. You entered <i>" + username + "</i>, but we do not have this account on record. <a href='/'>Try again</a>.<br>Remember, usernames are case-sensitive."
    #tell user their password is wrong if it does not match
    if(password != "pee"):
        return "Your <b>password</b> is incorrect. <a href='/'>Try again</a>.<br>Remember, passwords are case-sensitive."

#Removes user from the session (if they were in it to begin with), and then tells them
@app.route("/loggedout", methods=["GET","POST"])
def loggedput():
    #removes the username saved from the session
    if in_session():
        session.pop("username")
        return "You have been successfully logged out. Go <a href='/'>back</a>"
    return "You were never logged in. Try signing in  <a href='/'>here</a>"

@app.route("/reportissue", methods=["GET","POST"])
def reportissue():
    if in_session():
        return render_template("ReportIssue.html")
    return render_template("notloggedin.html")

@app.route("/issuereported", methods=["GET","POST"])
def issuereported():
    if in_session():
        return render_template("ReportIssueSubmissionSuccess.html")
    return render_template("notloggedin.html")


def in_session():
    bool = 'username' in session
    print("In session: " + str(bool))
    return bool

#necessary to run the app
if __name__ == "__main__":
    app.debug = True
    app.run()