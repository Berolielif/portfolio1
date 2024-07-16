
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  # Burayı kendi veritabanı yolunuza göre değiştirin

db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Feedback {self.id}>"

# Veritabanı tablolarını oluşturma
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')

    return render_template('index.html', 
                           button_python=button_python,
                           button_discord=button_discord,
                           button_html=button_html)

if __name__ == '__main__':
    app.run(debug=True)
