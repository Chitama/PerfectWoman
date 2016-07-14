
from django.contrib import admin

from .models import Question, Product, Category

admin.site.register(Question)
admin.site.register(Product)
admin.site.register(Category)