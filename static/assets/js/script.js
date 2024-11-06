

// function addToCart(itemId, itemName, itemPrice) {
//     // You can use fetch or XMLHttpRequest to send data to the server
//     fetch('/add_to_cart/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': '{{ csrf_token }}' // Ensure CSRF token is included
//         },
//         body: JSON.stringify({ 'item_id': itemId, 'name': itemName, 'price': itemPrice })
//     })
//     .then(response => {
//         if (response.ok) {
//             alert("Item added to cart!");
//         } else {
//             alert("Failed to add item to cart.");
//         }
//     })
//     .catch(error => {
//         console.error("Error adding item to cart:", error);
//     });
// }
