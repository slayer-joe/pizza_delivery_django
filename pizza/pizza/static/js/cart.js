// var isItCatalog = document.querySelector('.catalog-container');

var addToCartList = document.querySelectorAll('button.add');
let quantity = document.querySelector('.quantity');
if(!localStorage.getItem('cart')) {
    localStorage.setItem('cart', JSON.stringify([]));
}
let cartArray = JSON.parse(localStorage.getItem('cart'));
quantity.innerText = cartArray.length;

let createPizzaObject = (context) => {
    let pizzaCard = context.parentElement;
    let pizza = {}
    let pizzaTitle = pizzaCard.querySelector('.pizza-title').textContent;
    let pizzaImgSrc = pizzaCard.querySelector('.pizza-img').src;
    let pizzaPrice = pizzaCard.querySelector('.price').textContent.replace(/[^0-9,.]/g, '').trim();;
    pizza['title'] = pizzaTitle;
    pizza['imageSrc'] = pizzaImgSrc;
    pizza['price'] = pizzaPrice;

    return pizza;
}

addToCartList.forEach((item) => {
    item.addEventListener('click', function(e) {
        cartArray.push(createPizzaObject(this));
        localStorage.setItem('cart', JSON.stringify(cartArray));
        quantity.innerText = cartArray.length;
    })
})
