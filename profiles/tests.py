from django.test import TestCase
from django.urls import reverse

from profiles.models import Profile
from django.contrib.auth.models import User


class IndexViewTestCase(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_title(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, '<title>Holiday Homes</title>')


class ProfileIndexViewTestCase(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_title(self):
        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertContains(response, '<title>Profiles</title>')


class LettingsDetailViewTestCase(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(
            username="Test",
            email="test@test.com",
            password="secretsecret"
        )
        self.new_profile = Profile.objects.create(
            user=self.new_user,
            favorite_city="Shanghai",
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f"/profiles/{self.new_profile.user.username}/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            reverse('profiles:profile', kwargs={
                'username': self.new_profile.user.username})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse('profiles:profile', kwargs={
                'username': self.new_profile.user.username})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_title(self):
        title = "<title>" + str(self.new_profile.user.username) + "</title>"
        response = self.client.get(
            reverse('profiles:profile',
                    kwargs={'username': self.new_profile.user.username}))
        self.assertContains(response, title)
