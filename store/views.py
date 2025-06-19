from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product, Cart, CartItem, Order, OrderItem
from .forms import UserRegistrationForm, OrderForm
from django.contrib.auth import login

def home(request):
    categories = Category.objects.all()
    featured_products = Product.objects.all().order_by('-created')[:8]
    return render(request, 'store/home.html', {
        'categories': categories,
        'featured_products': featured_products
    })

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    category_id = request.GET.get('category')
    search_query = request.GET.get('search')
    sort_by = request.GET.get('sort', 'name')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    elif category_id:
        category = Category.objects.filter(id=category_id).first()
        products = products.filter(category_id=category_id)

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    else:
        products = products.order_by('name')

    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
        'current_category': category_id or (category.id if category else None),
        'current_sort': sort_by,
        'search_query': search_query,
        'category': category,
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product_id)[:4]
    return render(request, 'store/product_detail.html', {
        'product': product,
        'related_products': related_products
    })

@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'store/cart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f'Товар {product.name} добавлен в корзину')
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, 'Товар удален из корзины')
    return redirect('cart')

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart')

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.total_price
            order.save()
            
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
            
            cart.delete()
            messages.success(request, 'Заказ успешно оформлен!')
            return redirect('profile')
    else:
        form = OrderForm(initial={
            'shipping_address': request.user.profile.address if hasattr(request.user, 'profile') else '',
            'phone': request.user.profile.phone if hasattr(request.user, 'profile') else ''
        })
    
    return render(request, 'store/checkout.html', {
        'cart': cart,
        'form': form
    })

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна!')
            return redirect('store:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/profile.html', {
        'form': form,
        'orders': orders
    }) 