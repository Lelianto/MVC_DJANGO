from django.shortcuts import render
from django.http import HttpResponse
from .models import Mentor, Mentee, Blog


# Create your views here.
def home(request):
    return render(request, 'web_alterra/home.html', {})
def blog(request):
    blogs = Blog.objects.all()

    for blog in blogs:
        blog.text_content = blog.text_content[0:500]

    return render(request, 'web_alterra/blog.html', {'blogs':blogs})
def mentee(request):
    mentees = Mentee.objects.all()
    return render(request, 'web_alterra/mentee.html', {'mentees': mentees,})
def mentor(request):
    mentors = Mentor.objects.all()
    return render(request, 'web_alterra/mentor.html', {'mentors': mentors,})
def author(request):
    return render(request, 'web_alterra/author.html', {})
def content_blog(request):
    return render(request, 'web_alterra/content_blog.html', {})

def save_new_content(request):
    img_blog_url = request.POST['img_blog_url']
    title = request.POST['title']
    text_content = request.POST['text_content']

    b = Blog(img_blog_url=img_blog_url,title=title, text_content=text_content)
    b.save()

    blogs = Blog.objects.all()
    return render(request,'web_alterra/blog.html', {'blogs': blogs}) 

def readmore(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)

    return render(request, 'web_alterra/complete_blog.html', {'blog':blog})


    



