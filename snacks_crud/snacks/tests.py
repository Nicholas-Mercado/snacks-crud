from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from unittest import skip
from .models import Snack


class ThingTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title="pickle", purchaser=self.user,
        )
    # @skip("Don't want to test")
    def test_string_representation(self):
        self.assertEqual(str(self.snack), "pickle")

    # @skip("Don't want to test")
    def test_thing_content(self):
        self.assertEqual(f"{self.snack.title}", "pickle")
        self.assertEqual(f"{self.snack.purchaser}", "tester")

    # @skip("Don't want to test")
    def test_thing_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
        self.assertTemplateUsed(response, "snack_list.html")
        
    # @skip("Don't want to test")
    def test_thing_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "snack_detail.html")
        
    # @skip("Don't want to test")
    def test_snack_list_status(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    # @skip("Don't want to test")
    def test_snack_list_templates_home(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')
        
    # @skip("Don't want to test")
    def test_thing_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "Rake",
                "description": "A rake",
                "purchaser": self.user.id,
            }, follow=True
        )
        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "A rake")


    # @skip("Don't want to test")
    def test_thing_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "Updated name","description": "A rake2", "purchaser":self.user.id}
        )
        self.assertRedirects(response, reverse("snack_detail", args="1"))
        
    # @skip("Don't want to test")
    def test_thing_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)
