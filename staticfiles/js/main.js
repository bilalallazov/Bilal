// Функция для обновления количества товаров в корзине
function updateCartItemQuantity(itemId, quantity) {
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = `/cart/update/${itemId}/`;

    const csrfInput = document.createElement('input');
    csrfInput.type = 'hidden';
    csrfInput.name = 'csrfmiddlewaretoken';
    csrfInput.value = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const quantityInput = document.createElement('input');
    quantityInput.type = 'hidden';
    quantityInput.name = 'quantity';
    quantityInput.value = quantity;

    form.appendChild(csrfInput);
    form.appendChild(quantityInput);
    document.body.appendChild(form);
    form.submit();
}

// Функция для удаления товара из корзины
function removeCartItem(itemId) {
    if (confirm('Вы уверены, что хотите удалить этот товар из корзины?')) {
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = `/cart/remove/${itemId}/`;

        const csrfInput = document.createElement('input');
        csrfInput.type = 'hidden';
        csrfInput.name = 'csrfmiddlewaretoken';
        csrfInput.value = document.querySelector('[name=csrfmiddlewaretoken]').value;

        form.appendChild(csrfInput);
        document.body.appendChild(form);
        form.submit();
    }
} 