
function addToCart(itemId, itemName, itemPrice) {
    // Add item to cart using AJAX or update session storage
    // Example of using sessionStorage to store cart items
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
