from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

# This is a simple Flask application that serves an index page.
# It uses the Flask framework to create a web server and render HTML templates.

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        found_user = user.query.filter_by(email=email, password=password).first()
        
        if found_user:
            return render_template('success.html', email=email)
        else:
            return "Invalid Credentials"
        
    return render_template('index.html', title='Login')

  

@app.route('/register', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = user(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('index'))
    # This function handles user registration.
    return render_template('signup.html', title='Register')  

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # This creates the database tables if they do not exist.
        
    app.run(debug=True)
# To run the application, use the command: python app.py