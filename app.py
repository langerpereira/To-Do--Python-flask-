from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow) 

    def __repe__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/')
def hello_world():
    todo = Todo(title= "first_ToDo", desc="start investing in stock market")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')
    # return 'Hello, World!'

@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allToDo)
    return 'this is product'    

if __name__ == "__main__":
    app.run(debug=True,port=8000)    