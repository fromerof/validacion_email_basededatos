from flask_app.models.email import Email
from flask import render_template,request,redirect
from flask_app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    return render_template("success.html",emails=Email.get_all())