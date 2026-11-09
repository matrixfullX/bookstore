import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from order.factory import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory


class TestOrderViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title='technology')
        self.product = ProductFactory(title='mouse', price=100, categories=[self.category])
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
        response = self.client.get(
            reverse('order-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)[0]
        self.assertEqual(order_data['product'][0]['title'], self.product.title)
        self.assertEqual(order_data['product'][0]['price'], self.product.price)
        self.assertEqual(order_data['product'][0]['active'], self.product.active)
        self.assertEqual(order_data['product'][0]['categories'][0]['title'], self.category.title)

    def teste_create_order(self):
        user = UserFactory()
        book_product = ProductFactory()
        data = json.dumps({
            "product_id": [book_product.id],
            "user": user.id,
        })

        response = self.client.post(
            reverse('order-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_order = Order.objects.get(user=user)