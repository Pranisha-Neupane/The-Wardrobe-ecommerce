{/* <script>
    function addToCart(itemId, itemName, itemPrice) {
        let cart = JSON.parse(localStorage.getItem('cart')) || [];

        const existingItem = cart.find(item => item.id === itemId);

        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cart.push({ id: itemId, name: itemName, price: itemPrice, quantity: 1 });
        }

        localStorage.setItem('cart', JSON.stringify(cart));

        alert(`${itemName} has been added to your cart!`);
    }
</script> */}

function addToCart(itemId, itemName, itemPrice) {
    const data = {
        id: itemId,
        name: itemName,
        price: itemPrice
    };

    fetch(`/add-to-cart/${itemId}/`, {  // Update the URL to match your URL pattern
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Include CSRF token for Django
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to add item to cart');
        }
        return response.json();
    })
    .then(data => {
        // Update cart item count
        updateCartCount(data.cartItemCount);
        alert(`${itemName} has been added to your cart!`);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error adding the item to the cart. Please try again later.');
    });
}
