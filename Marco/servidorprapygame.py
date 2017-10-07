from flask import Flask, render_template, request
import usermaker as u

app = Flask('SiteFinal')
# posts = []
# stats = []

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/sobre<username>.html')
def profile(username):
	return render_template('sobre' + username + '.html')

@app.route('/<username>area<i>.html')
def areas(username,i):
	return render_template(username + "area" + i + '.html')

@app.route('/<username><aok>.html')
def areas_especificas(username,aok):
	return render_template(username + aok + '.html')

@app.route('/signup.html')
def my_form():
    return render_template("signup.html")

@app.route('/pagesetup', methods=['POST'])
def my_form_post():
    text = dict(request.form)
    for item in text:
    	text[item] = text[item][0]
    u.usermaker(text)
    import new_power_page
    return render_template('homepage.html')

app.run(host= '0.0.0.0',debug=True)