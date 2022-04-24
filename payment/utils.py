def rupee_to_paisa(rupee):
    return rupee * 100


def cart_total(cart):
    cart_total=0
        
    for c in cart:
        cart_total += c.total

    return cart_total    