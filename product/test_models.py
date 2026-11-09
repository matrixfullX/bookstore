from django.test import TestCase
from product.models import Category, Product


class CategoryModelTests(TestCase):
    def test_category_is_created_with_active_default(self):
        category = Category.objects.create(
            title="Ficção",
            slug="ficcao",
        )

        self.assertEqual(category.title, "Ficção")
        self.assertTrue(category.active)
        self.assertIsNone(category.description)


class ProductModelTests(TestCase):
    def test_product_is_created_with_active_default(self):
        product = Product.objects.create(
            title="Livro de teste",
            price=5000,
        )

        self.assertEqual(product.title, "Livro de teste")
        self.assertTrue(product.active)
        self.assertIsNone(product.description)

    def test_product_can_have_categories(self):
        category = Category.objects.create(
            title="Ficção",
            slug="ficcao",
        )
        product = Product.objects.create(
            title="Livro de teste",
            price=5000,
        )

        product.categories.add(category)

        self.assertIn(category, product.categories.all())