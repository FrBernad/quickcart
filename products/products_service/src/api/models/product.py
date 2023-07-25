from src.api.persistence.db import db
from sqlalchemy.sql import func

product_tag = db.Table(
    "product_tag",
    db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
)


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    score = db.Column(db.Float, nullable=False, default=0)
    tags = db.relationship("Tag", secondary=product_tag)
    creation_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    # ownwer
