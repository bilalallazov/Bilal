from .models import Cart, CartItem

def cart(request):
    """Добавляет корзину в контекст шаблона"""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items_count = CartItem.objects.filter(cart=cart).count()
    else:
        cart_items_count = 0
    return {'cart_items_count': cart_items_count} 