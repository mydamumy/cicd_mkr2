from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Image
from django.core.files.uploadedfile import SimpleUploadedFile

class GalleryViewsTest(TestCase):

    def setUp(self):
        self.image_file = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")

        self.recent_image = Image.objects.create(
            title="Recent",
            image=self.image_file,
            created_date=timezone.now(),
            age_limit=18
        )
        self.old_image = Image.objects.create(
            title="Old",
            image=self.image_file,
            created_date=timezone.now() - timedelta(days=60),
            age_limit=18
        )

    def test_gallery_view_shows_only_recent_images(self):
        response = self.client.get(reverse('gallery'))
        self.assertContains(response, self.recent_image.title)
        self.assertNotContains(response, self.old_image.title)

    def test_image_detail_view_displays_image(self):
        response = self.client.get(reverse('image_detail', args=[self.recent_image.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recent_image.title)

class ImageModelTest(TestCase):

    def test_image_str(self):
        image = Image(title='Test Image', age_limit=18)  # теж додайте значення
        self.assertEqual(str(image), 'Test Image')
