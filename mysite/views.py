from django.shortcuts import redirect, render
from django.http import Http404
from datetime import datetime
from mysite.models import Post, Product


def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())


def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def about(request):
    return render(request, 'about.html', locals())


def listing(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())


def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')

    return render(request, 'disp.html', locals())