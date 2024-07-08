from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from werkzeug.security import generate_password_hash
from typing import List


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(255))
    email: Mapped[str] = mapped_column(db.String(255))
    password: Mapped[str] = mapped_column(db.String(255))
    posts: Mapped[List['Post']] = db.relationship(back_populates='author')

    def __init__(self, **kwargs):
        # Call the parent __init__ so everything still works as intended
        super().__init__(**kwargs)
        # Set the password field to be the hashed version of the keyword password
        self.password = generate_password_hash(kwargs['password'])
        # Add the new instance to the database
        db.session.add(self)
        # Commit to the database
        db.session.commit()

    def __repr__(self):
        return f"<User {self.id}|{self.username}>"


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(255))
    body: Mapped[str] = mapped_column(db.String(255))
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), nullable=False)
    author: Mapped['User'] = db.relationship(back_populates='posts')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"
