<script>
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
</script>
