from src import create_app
from src import db

app = create_app()

with app.app_context():
    from src.api.models.purchase_orders import PurchaseOrders
    from src.api.models.purchase_products import ProductsPurchased
    db.create_all()
