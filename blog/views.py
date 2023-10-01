from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User

def post_list2(requests):
    ls=Post.objects.all()
    s="<ul>"
    for item in ls:
        s+="<li>"+str(item)+"</li>"
    s+="</ul>"
    return HttpResponse(s)

def post_list(requests):
    ls=Post.objects.all()
    content = {"posts":ls}
    return render(requests,'blog/post_list.html',content)


def create100(requests):
    me = User.objects.get(username='admin')
    for i in range(100):
        p=Post.objects.create(author=me, title=f'fotball_omid{i}', text=f'fotball_omid dar barabar hongkong baxt {i}')

        p.publish()
    return HttpResponse("Done")