from django.test import TestCase
from blog.models import Blog

class TestBlogModel(TestCase):
    def setUp(self):
        Blog.objects.create(title="New Tea", author="Joe Blogs", 
                            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris nisi est, rhoncus vitae dui vel, ullamcorper maximus tortor.")
        Blog.objects.create(title="News from Supplier", author="John Smith", 
                            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                            image_url="https://res.cloudinary.com/chronologic12/image/upload/v1656321094/tippy/images/pexels-pixabay-39347_cgz72p.jpg")

    def test_object_created(self):
        blog_one = Blog.objects.get(title="New Tea")
        blog_two = Blog.objects.get(title="News from Supplier")
        self.assertEqual(blog_one.author, "Joe Blogs")
        self.assertEqual(blog_one.image_url, "")
        self.assertEqual(blog_one.content, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris nisi est, rhoncus vitae dui vel, ullamcorper maximus tortor.")
        self.assertIsNotNone(blog_one.date)
        self.assertEqual(blog_two.author, "John Smith")
        self.assertEqual(blog_two.image_url, "https://res.cloudinary.com/chronologic12/image/upload/v1656321094/tippy/images/pexels-pixabay-39347_cgz72p.jpg")
        self.assertEqual(blog_two.content, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        self.assertIsNotNone(blog_two.date)
