from django.contrib.auth.models import User
from django.test import TestCase

from order.models import Order
from order.serializers import OrderSerializer
from product.models import Product


class OrderSerializerTest(TestCase):

  def setUp(self):
    self.user = User.objects.create_user(
      username='teste',
      password='123456'
    )

    self.product1 = Product.objects.create(
      title='Produto 1',
      price=50,
      active=True
    )

    self.product2 = Product.objects.create(
      title='Produto 2',
      price=100,
      active=True
    )

    self.order = Order.objects.create(user=self.user)
    self.order.product.add(self.product1, self.product2)

  def test_order_serializer_fields(self):
    serializer = OrderSerializer(self.order)

    self.assertEqual(
      set(serializer.data.keys()),
      {'product', 'total', 'user'}
    )

  def test_order_total(self):
    serializer = OrderSerializer(self.order)

    self.assertEqual(serializer.data['total'], 150)




