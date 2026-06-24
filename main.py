from flask import  render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///new-books-collection.db"
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str]=mapped_column(nullable=False)
    rating: Mapped[float]=mapped_column(nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books=db.session.execute(db.select(Book).order_by(Book.id)).scalars().all()
    return render_template('index.html',allbooks=all_books)


@app.route("/add",methods=['POST','GET'])
def add():
    if request.method == 'POST':
        newbook=Book(
                title=request.form["bookname"],
                author= request.form["authorname"],
                rating= request.form["rating"]
                    )
        db.session.add(newbook)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')

@app.route("/edit/<bookid>", methods=['POST','GET'])
def edit(bookid):
    book_to_update = db.session.execute(db.select(Book).where(Book.id == bookid)).scalar()

    if request.method=="POST":
        book_to_update.rating=float(request.form["change_rating"])
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('EditRating.html',title=book_to_update.title,crating=book_to_update.rating,id=bookid)


if __name__ == "__main__":
    app.run(debug=True)

