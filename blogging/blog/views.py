from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from slugify import slugify
import json
from django.http import JsonResponse
from django.db.models import Q

def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {'posts':posts})


@csrf_exempt
def write(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            updatedData=json.loads(request.body.decode('UTF-8'))
            title = updatedData['title']
            caption = updatedData['caption']
            post = updatedData['post_html']
            post_json = updatedData['post_json']
            thumbnail = updatedData['thumbnail']
            po = Post.objects.create(title=title, caption=caption, post=post, post_json=post_json, thumbnail=thumbnail)
            po.save()
            return JsonResponse({'status':'success'})

        return render(request, "write.html")

    else:
        return redirect("/")

def post(request, title, post_id):
    po = get_object_or_404(Post, id=post_id)
    posts = Post.objects.all()
    if not slugify(po.title) == title:
        return redirect("post", title=slugify(po.title), post_id=po.id)

    po.visitors += 1
    po.save()
    return render(request, "post.html", {'po':po, 'posts':posts})


def search(request):
    if request.GET.get('q'):
        query = request.GET.get('q')
        posts = Post.objects.filter(Q(title__icontains=query) | Q(post__icontains=query))
        return render(request, "search.html", {'posts':posts, 'query': query})

    else:
        return redirect("/")