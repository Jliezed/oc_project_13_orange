from django.test import TestCase
from django.urls import reverse

from .models import Letting, Address


class LettingsIndexViewTestCase(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/lettings/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('lettings:lettings_index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('lettings:lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_title(self):
        response = self.client.get(reverse('lettings:lettings_index'))
        self.assertContains(response, '<title>Lettings</title>')


class LettingsDetailViewTestCase(TestCase):
    def setUp(self):
        # Create an address
        self.new_address = Address()
        self.new_address.number = 1
        self.new_address.street = "success street"
        self.new_address.city = "dream"
        self.new_address.state = "big"
        self.new_address.zip_code = 00000
        self.new_address.country_iso_code = "UV"
        self.new_address.save()

        self.new_letting = Letting()
        self.new_letting.title = "test"
        self.new_letting.address = self.new_address
        self.new_letting.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f"/lettings/{self.new_letting.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            reverse('lettings:letting', kwargs={'letting_id': self.new_letting.pk}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse('lettings:letting', kwargs={'letting_id': self.new_letting.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_title(self):
        title = "<title>" + str(self.new_letting.title) + "</title>"
        response = self.client.get(
            reverse('lettings:letting', kwargs={'letting_id': self.new_letting.pk}))
        self.assertContains(response, title)
