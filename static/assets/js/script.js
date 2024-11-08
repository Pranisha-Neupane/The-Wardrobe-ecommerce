// to count the number of items in the cart

function addToCart(itemId, itemName, itemPrice) {
    let cart = JSON.parse(sessionStorage.getItem('cart')) || [];
    cart.push({ id: itemId, name: itemName, price: itemPrice });
    sessionStorage.setItem('cart', JSON.stringify(cart));

    // Update cart count dynamically
    updateCartCount();
}

function updateCartCount() {
    let cart = JSON.parse(sessionStorage.getItem('cart')) || [];
    let cartCount = cart.length;
    document.getElementById('cart-count').textContent = cartCount;
}








// new code 

    // function addToCart(productId, productName, productPrice) {
    //     const quantity = 1;  // You can dynamically get this value from an input field if needed
    //     const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;  // CSRF token for security

    //     fetch("{% url 'add_to_cart' %}", {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/json',
    //             'X-CSRFToken': csrfToken,
    //         },
    //         body: JSON.stringify({
    //             'product_id': productId,
    //             'quantity': quantity,
    //         }),
    //     })
    //     .then(response => response.json())
    //     .then(data => {
    //         if (data.success) {
    //             // Successfully added to cart
    //             alert('Item added to cart!');
    //             // Update cart count if needed
    //             document.getElementById('cart-count').textContent = data.cart_count;
    //         } else {
    //             alert('Failed to add item to cart!');
    //         }
    //     })
    //     .catch(error => {
    //         console.error('Error:', error);
    //     });
    // }

