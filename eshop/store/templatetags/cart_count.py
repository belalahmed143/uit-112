from django import template 
from store.models import Order,WhishLIst

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user,ordered=False)
        if qs.exists():
            return qs[0].products.count()
        return 0


@register.filter
def wish_list_product_count(user):
    if user.is_authenticated:
       return WhishLIst.objects.filter(user=user).count()
    return 0