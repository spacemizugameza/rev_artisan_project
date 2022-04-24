from .models import Cart
def cart_total_item(user):
    cart = Cart.objects.filter(user=user)
    total = 0
    for item in cart:
        total += item.quantity

    return total