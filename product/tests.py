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

    def test_category_title_required(self):
        serializer = CategorySerializer(data={
            'slug': 'livros',
            'description': 'Categoria de livros',
            'active': True
        })

        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)


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

    def test_product_invalid_price(self):
        serializer = ProductSerializer(data={
            'title': 'Livro Django',
            'description': 'Livro sobre Django',
            'price': -10,
            'active': True,
            'category': [
                {
                    'title': 'Tecnologia',
                    'slug': 'tecnologia',
                    'description': 'Categoria de tecnologia',
                    'active': True
                }
            ]
        })

        self.assertFalse(serializer.is_valid())
        self.assertIn('price', serializer.errors)
