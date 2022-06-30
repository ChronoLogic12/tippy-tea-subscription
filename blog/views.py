from datetime import date
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import BlogForm

from .models import Blog

def all_blogs(request):
    """ A view to show all blog posts """

    if request.method == "GET":
        blogs = Blog.objects.all()
        blogs.order_by("date")

        context = {
            'blogs': blogs,
        }

        return render(request, 'blog/blog.html', context, status=200)


@login_required
def add_blog(request):
    """ Add a blog to the database """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only accessible by site owners.")
        return redirect(reverse("home"))
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added new blog post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = BlogForm()
        
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Remove blog from the database """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only accessible by site owners.")
        return redirect(reverse("blog"))
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('blog'))