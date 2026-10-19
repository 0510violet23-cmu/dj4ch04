from django.shortcuts import render
from phone.models import Product, PPhoto


def phone_list(request):
    products = Product.objects.all()
    return render(request, 'phone_list.html', locals())


def phone_detail(request, id):
    try:
        product = Product.objects.get(id=id)
        images = PPhoto.objects.filter(product=product)
    except Product.DoesNotExist:
        product = None
        images = []

    return render(request, 'phone_detail.html', locals())