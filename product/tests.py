from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from product.models import Category, Product
from product.serializers import CategorySerializer, ProductSerializer


class CategorySerializerTest(TestCase):

    def test_category_serializer_fields(self):
        category = Category.objects.create(
            title='Livros',
            slug='livros',
            description='Categoria de livros',
            active=True
        )

        serializer = CategorySerializer(category)

        self.assertEqual(
            set(serializer.data.keys()),
            {'title', 'slug', 'description', 'active'}
        )


class ProductSerializerTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            title='Tecnologia',
            slug='tecnologia',
            active=True
        )

        self.product = Product.objects.create(
            title='Livro Django',
            description='Livro sobre Django',
            price=100,
            active=True
        )

        self.product.category.add(self.category)

    def test_product_serializer_fields(self):
        serializer = ProductSerializer(self.product)

        self.assertEqual(
            set(serializer.data.keys()),
            {'title', 'description', 'price', 'active', 'category'}
        )

    def test_product_contains_category(self):
        serializer = ProductSerializer(self.product)

        self.assertEqual(
            serializer.data['category'][0]['title'],
            'Tecnologia'
        )
