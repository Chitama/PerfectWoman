from django.http import HttpResponse
from django.template import loader

from .models import Question, Product, Category


def index(request):
    category_list = Category.objects.order_by('-category_type')[:5]
    template = loader.get_template('portal/index.html')
    context = {
        'category_list': category_list,
    }
    return HttpResponse(template.render(context, request))