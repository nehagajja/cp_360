
from celery import shared_task
from faker import Faker
from .models import Product, Category
import random


@shared_task
def generate_dummy_data( num_products=1000):
    fake = Faker()

    # Create Products
    for _ in range(num_products):
        Product.objects.create(
            name=fake.word(),
            description=fake.text(),
            price=fake.random_number(digits=2),
            created_at=fake.date(),
            expiry_date=fake.date(),
            uploaded_by=fake.text(),
            category=fake.text()

        )

    return f"{num_products} products created."
