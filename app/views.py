from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products_list = Product.objects.filter(category=category)

    paginator = Paginator(products_list, 5)  # 5 товаров на странице
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'category_detail.html', {
        'category': category,
        'page_obj': page_obj,
        'products': page_obj.object_list
    })