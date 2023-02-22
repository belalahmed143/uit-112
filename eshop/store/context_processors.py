from .models import Category

def category(request):
    categories = Category.objects.filter(parent_category=None)

    context ={
        'categories':categories
    }
    return context