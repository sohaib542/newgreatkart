from django.shortcuts import render , get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.

def store(request,category_slug=None):
    category=None
    product=None
    if category_slug != None:
        category = get_object_or_404(Category,slug=category_slug)
        product = Product.objects.filter(category=category)
    else:

        product=Product.objects.all()

    context={'product':product , 'category':category}
    return render(request,'store/store.html',context)

def product_detail(request,category_slug,product_slug):
    try:
        detail=get_object_or_404(Product ,category__slug=category_slug,slug=product_slug)
    except Exception as e:
        return e
    context={'detail':detail}

    return render(request, 'store/product_detail.html',context)