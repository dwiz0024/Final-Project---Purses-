async function addToCart(productId) {
    const response = await fetch("/add-to-cart", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ productId }),
    });
    const data = await response.json();
    document.getElementById("Cart-Total").innerText = data.total;
}