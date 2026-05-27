from faker import Faker
from .models import Product
import random

fake = Faker()

def generate():
    for _ in range(100):
        Product.objects.create(
            name=fake.name(),
            price=round(random.uniform(10, 1000), 2),
            description=fake.text(),
            quantity=random.randint(0, 100),
        )
