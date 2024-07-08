from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from werkzeug.security import generate_password_hash


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(255))
    email: Mapped[str] = mapped_column(db.String(255))
    password: Mapped[str] = mapped_column(db.String(255))

    def __init__(self, **kwargs):
        # Call the parent __init__ so everything still works as intended
        super().__init__(**kwargs)
        # Set the password field to be the hashed version of the keyword password
        self.password = generate_password_hash(kwargs['password'])
        # Add the new instance to the database
        db.session.add(self)
        # Commit to the database
        db.session.commit()
