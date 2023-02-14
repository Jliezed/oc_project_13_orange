from django.test import TestCase
from django.urls import reverse

from lettings.models import Letting, Address


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
        self.new_address = Address.objects.create(
            number=1,
            street="success street",
            city="dream",
            state="big",
            zip_code=00000,
            country_iso_code="UV",
        )
        self.new_letting = Letting.objects.create(
            title="test",
            address=self.new_address,
        )

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
