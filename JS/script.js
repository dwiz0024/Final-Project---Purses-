// Array to hold cart items
let cart = [];

// Function to add product to cart
function addToCart(productName, price) {
    cart.push({ productName, price });
    updateCartTotal();
    alert(`${productName} has been added to the cart.`);
}

// Function to update the cart total
function updateCartTotal() {
    const total = cart.reduce((sum, item) => sum + item.price, 0);
    document.getElementById('cart-total').innerText = `Total: $${total.toFixed(2)}`;
}

// Function to render cart items
function renderCart() {
    const cartList = document.getElementById('cart-list');
    cartList.innerHTML = '';
    cart.forEach(item => {
        const li = document.createElement('li');
        li.innerText = `${item.productName} - $${item.price.toFixed(2)}`;
        cartList.appendChild(li);
    });
}
