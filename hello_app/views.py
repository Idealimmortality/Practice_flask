from hello_app import app
from flask import render_template,flash,redirect


# index view function suppressed for brevity
@app.route('/index')
def index():
    messege = []

    return render_template('index.html',
                           title = 'Home',
                           messege = messege)

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    from .form import LoginForm
    form  = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        print(form.remember_me.__module__)
        return redirect('/index')
    title = "Sign in test"
    return render_template('login.html',
                           title = title,
                           form= form,
                           providers = app.config["OPENID_PROVIDERS"])



@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

