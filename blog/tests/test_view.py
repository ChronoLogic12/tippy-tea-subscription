from django.test import TestCase
from django.urls import reverse
from django.utils.crypto import get_random_string

from blog.models import Blog

from django.contrib.auth.models import User
from django.test.client import Client


class TestAllBlogsView(TestCase):

    def test_url_exists_at_desired_location(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')


class TestEditBlogView(TestCase):
    def create_user(self, superuser):
        self.username = "test_user"
        self.password = User.objects.make_random_password()
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = superuser
        user.is_active = True
        user.save()
        self.user = user
        
    def setUp(self):
        Blog.objects.create(title="New Tea", author="Joe Blogs", 
                        content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris nisi est, rhoncus vitae dui vel, ullamcorper maximus tortor.")
                        
        Blog.objects.create(title="News from Supplier", author="John Smith", 
                            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                            image_url="https://res.cloudinary.com/chronologic12/image/upload/v1656321094/tippy/images/pexels-pixabay-39347_cgz72p.jpg")

    def test_edit_title_returns_correct_data(self):
        self.create_user(True)
        self.client.login(username=self.username, password=self.password)
        string = get_random_string(20)
        blog1 = Blog.objects.get(title="New Tea")

        response = self.client.post(
            reverse('edit_blog', kwargs={'blog_id': blog1.id}), 
            {'title': blog1.title + string, 'author': blog1.author,  'date': blog1.date, 'content': blog1.content, 'image_url': blog1.image_url })

        updated_blog = Blog.objects.get(pk=blog1.id)

        self.assertRedirects(response, '/blog/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)
        self.assertEqual(updated_blog.title, (blog1.title + string))

    
    def test_edit_blog_redirects_non_superuser(self):
        self.create_user(False)
        self.client.login(username=self.username, password=self.password)
        string = get_random_string(20)
        blog1 = Blog.objects.get(title="New Tea")

        response = self.client.post(
            reverse('edit_blog', kwargs={'blog_id': blog1.id}), 
            {'title': blog1.title + string, 'author': blog1.author,  'date': blog1.date, 'content': blog1.content, 'image_url': blog1.image_url })

        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)


    def test_edit_blog_redirects_if_not_logged_in(self):
        string = get_random_string(20)
        blog1 = Blog.objects.get(title="New Tea")

        response = self.client.post(
            reverse('edit_blog', kwargs={'blog_id': blog1.id}), 
            {'title': blog1.title + string, 'author': blog1.author,  'date': blog1.date, 'content': blog1.content, 'image_url': blog1.image_url })

        self.assertRedirects(response, '/accounts/login/?next=/blog/edit/1/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)


class TestDeleteBlogView(TestCase):
    def create_user(self, superuser):
        self.username = "test_admin"
        self.password = User.objects.make_random_password()
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = superuser
        user.is_active = True
        user.save()
        self.user = user

    def setUp(self):
        self.create_user(True)
        self.client.login(username=self.username, password=self.password)
        Blog.objects.create(title="New Tea", author="Joe Blogs", 
                        content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris nisi est, rhoncus vitae dui vel, ullamcorper maximus tortor.")
        Blog.objects.create(title="News from Supplier", author="John Smith", 
                            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                            image_url="https://res.cloudinary.com/chronologic12/image/upload/v1656321094/tippy/images/pexels-pixabay-39347_cgz72p.jpg")

    def test_delete_blog_returns_correct_status_code(self):
        self.assertEqual(len(Blog.objects.all()), 2)
        blog1 = Blog.objects.get(title="New Tea")

        response = self.client.delete(
            reverse('delete_blog', kwargs={'blog_id': blog1.id}))

        self.assertRedirects(response, '/blog/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)
        self.assertEqual(len(Blog.objects.all()), 1)


    def test_delete_blog_redirects_non_superuser(self):
        self.create_user(False)
        self.client.login(username=self.username, password=self.password)
        blog1 = Blog.objects.get(title="New Tea")

        response = self.client.delete(
            reverse('delete_blog', kwargs={'blog_id': blog1.id}))

        self.assertRedirects(response, '/blog/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)


    def test_delete_blog_redirects_if_not_logged_in(self):
        self.client.logout()
        blog1 = Blog.objects.get(title="New Tea")

        response = self.client.delete(
            reverse('delete_blog', kwargs={'blog_id': blog1.id}))

        self.assertRedirects(response, '/accounts/login/?next=/blog/delete/1/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)


