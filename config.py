from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.String(80), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.methods == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new_user = user(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return render_template('index.html')
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)