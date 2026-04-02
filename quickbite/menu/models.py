from mongoengine import Document, StringField, FloatField, IntField, BooleanField, DateTimeField
import datetime

class MenuItem(Document):
    restaurant_name = StringField(required=True)
    menu_name = StringField(required=True)
    category = StringField(required=True)
    price = FloatField(required=True)
    spicy_level = IntField(min_value=1, max_value=5)
    is_available = BooleanField(default=True)
    description = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow)

    meta = {"collection": "menu_items"}