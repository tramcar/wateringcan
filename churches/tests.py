import pprint
from django.db.utils import IntegrityError
from django.test import TestCase
from django.urls import reverse

from .models import Page


class PageModelTest(TestCase):
    def test_slug_cannot_be_non_unique(self):
        page1 = Page(title="title", content="content", slug="title")
        page2 = Page(title="title", content="content", slug="title")
        page1.save()
        self.assertRaises(IntegrityError, page2.save)
        self.assertIsNotNone(page1.id)
        self.assertIsNone(page2.id)

    def test_new_page_is_created_with_created_at_and_updated_at(self):
        page = Page(title="title", content="content", slug="title")
        page.save()
        self.assertIsNotNone(page.created_at)
        self.assertIsNotNone(page.updated_at)

    def test_updated_page_does_not_update_created_at(self):
        page = Page(title="title", content="content", slug="title")
        page.save()
        created_at = page.created_at
        page.title = "updated title"
        page.save()
        self.assertEqual(created_at, page.created_at)

    def test_updated_page_updates_updated_at(self):
        page = Page(title="title", content="content", slug="title")
        page.save()
        updated_at = page.updated_at
        page.title = "updated title"
        page.save()
        self.assertNotEqual(updated_at, page.updated_at)

class PageViewTests(TestCase):
    def test_get_page_by_slug(self):
        page = Page(title="title", content="# content", slug="title")
        page.save()
        response = self.client.get(reverse("detail_slug", args=(page.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["content_md"], "<h1>content</h1>")

    def test_get_page_by_id(self):
        page = Page(title="title", content="# content", slug="test")
        page.save()
        response = self.client.get(reverse("detail", args=(page.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["content_md"], "<h1>content</h1>")