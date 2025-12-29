from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category, Order

class DashboardTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            quantity=10
        )

    def test_index_view(self):
        response = self.client.get(reverse('dashboard:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/index.html')

    def test_products_view(self):
        response = self.client.get(reverse('dashboard:products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/products.html')

    def test_product_add_view(self):
        response = self.client.post(reverse('dashboard:product_add'), {
            'name': 'New Product',
            'category': self.category.id,
            'quantity': 20,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(name='New Product').exists())

    def test_product_edit_view(self):
        response = self.client.post(reverse('dashboard:product_edit', args=[self.product.pk]), {
            'name': 'Updated Product',
            'category': self.category.id,
            'quantity': 30,
        })
        self.assertEqual(response.status_code, 302)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')

    def test_product_delete_view(self):
        response = self.client.post(reverse('dashboard:product_delete', args=[self.product.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())

    def test_categories_view(self):
        response = self.client.get(reverse('dashboard:categories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/categories.html')

    def test_category_add_view(self):
        response = self.client.post(reverse('dashboard:category_add'), {
            'name': 'New Category',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name='New Category').exists())

    def test_category_edit_view(self):
        response = self.client.post(reverse('dashboard:category_edit', args=[self.category.pk]), {
            'name': 'Updated Category',
        })
        self.assertEqual(response.status_code, 302)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, 'Updated Category')

    def test_category_delete_view(self):
        response = self.client.post(reverse('dashboard:category_delete', args=[self.category.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Category.objects.filter(pk=self.category.pk).exists())

    def test_orders_view(self):
        response = self.client.get(reverse('dashboard:orders'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/orders.html')

    def test_order_add_view(self):
        response = self.client.post(reverse('dashboard:order_add'), {
            'product': self.product.id,
            'order_quantity': 5,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Order.objects.filter(product=self.product).exists())
