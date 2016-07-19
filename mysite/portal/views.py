from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Product, Category


def index(request):
    category_list = Category.objects.order_by('-category_type')[:5]
    template = loader.get_template('portal/index.html')
    context = {
        'category_list': category_list,
    }
    return HttpResponse(template.render(context, request))


def result(request):
    try:
        product = ""

        category_list = Category.objects.order_by('-category_type')[:5]
        template = loader.get_template('portal/result.html')
        context = {
            'category_list': category_list,
        }

    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    return HttpResponse(template.render(context, request))
    #return render(request, 'portal/result.html', {'product': product})


def form(request):
    try:
        product = ""

        category_list = Category.objects.order_by('-category_type')[:5]
        template = loader.get_template('portal/form.html')
        context = {
            'category_list': category_list,
        }

    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    return HttpResponse(template.render(context, request))
    #return render(request, 'portal/form.html', {'product': product})
