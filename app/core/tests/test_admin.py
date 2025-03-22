"""
Test admin model and interface
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):
    """Test login and django admin features"""

    def setUp(self):
        """Set up user for testing"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='test@example.com',
            password='simple123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='Simple@123',
            name='Test User',
        )

    def test_users_list(self):
        """test user list"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user(self):
        """Test user editing"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_user_creation(self):
        """Test user creation page is accessible or not"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
