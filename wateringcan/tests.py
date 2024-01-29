from django.db.utils import IntegrityError
from django.test import TestCase
from django.urls import reverse

from .models import Page


class PageModelTest(TestCase):
    def test_slug_cannot_be_non_unique(self):
        page1 = Page(title="title", content="content", slug="title", order=0)
        page2 = Page(title="title", content="content", slug="title", order=10)
        page1.save()
        self.assertRaises(IntegrityError, page2.save)
        self.assertIsNotNone(page1.id)
        self.assertIsNone(page2.id)

    def test_order_cannot_be_non_unique(self):
        page1 = Page(title="title1", content="content1", slug="title1", order=10)
        page2 = Page(title="title2", content="content2", slug="title2", order=10)
        page1.save()
        self.assertRaises(IntegrityError, page2.save)
        self.assertIsNotNone(page1.id)
        self.assertIsNone(page2.id)

    def test_new_page_is_created_with_created_at_and_updated_at(self):
        page = Page(title="title", content="content", slug="title", order=0)
        page.save()
        self.assertIsNotNone(page.created_at)
        self.assertIsNotNone(page.updated_at)

    def test_updated_page_does_not_update_created_at(self):
        page = Page(title="title", content="content", slug="title", order=0)
        page.save()
        created_at = page.created_at
        page.title = "updated title"
        page.save()
        self.assertEqual(created_at, page.created_at)

    def test_updated_page_updates_updated_at(self):
        page = Page(title="title", content="content", slug="title", order=0)
        page.save()
        updated_at = page.updated_at
        page.title = "updated title"
        page.save()
        self.assertNotEqual(updated_at, page.updated_at)


class PageViewTests(TestCase):
    def test_get_index_returns_right_page(self):
        page1 = Page(title="title1", content="# content1", slug="title1", order=0)
        page2 = Page(title="title2", content="# content2", slug="title2", order=10)
        page1.save()
        page2.save()
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["content_md"], "<h1>content1</h1>")

    def test_get_page_by_slug(self):
        page = Page(title="title", content="# content", slug="title", order=0)
        page.save()
        response = self.client.get(reverse("detail_slug", args=(page.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["content_md"], "<h1>content</h1>")

    def test_get_page_by_id(self):
        page = Page(title="title", content="# content", slug="test", order=0)
        page.save()
        response = self.client.get(reverse("detail", args=(page.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["content_md"], "<h1>content</h1>")
