from django.contrib.auth.models import User
from django.test import TestCase

from order.models import Order
from product.models import Product


class OrderModelTests(TestCase):
    def test_order_is_created_for_a_user(self):
        user = User.objects.create_user(
            username="leitor",
            password="senha-de-teste",
        )
        order = Order.objects.create(user=user)

        self.assertEqual(order.user, user)

    def test_order_can_contain_products(self):
        user = User.objects.create_user(
            username="leitor",
            password="senha-de-teste",
        )
        product = Product.objects.create(
            title="Livro de teste",
            price=5000,
        )
        order = Order.objects.create(user=user)

        order.product.add(product)

        self.assertIn(product, order.product.all())