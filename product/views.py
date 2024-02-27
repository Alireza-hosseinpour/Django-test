from django.shortcuts import render, get_object_or_404

from product.models import Product


# Create your views here.

def index(request):
    return render(request, 'art/index.html', {})


def list_of_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/list_of_products.html', context)


def favourites(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.favourites.filter(id=request.user.id).exist():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)

    # return render(request, 'favourites/product_favourite_list.html')


def product_favourite_list(request):
    user = request.user
    favourite_products = user.favourites.all()

    context = {
        'favourite_products': favourite_products
    }

    return render(request, 'favourites/product_favourite_list.html', context)
