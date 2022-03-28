let productListContainer = document.querySelector('.product-cart-list');

class ProductCartList {
    constructor() {
        this.cart = JSON.parse(localStorage.getItem('cart'));
        this.show();
        this.addEvents();
    }

    addEvents () {
        let delButtonsList = document.querySelectorAll('.delete-button');
        delButtonsList.forEach((del, ind)=>{
            del.addEventListener('click', ()=> {
                this.deleteItem(ind);
                this.show();
            })
        })

    }

    deleteItem(id) {

        let quantity = document.querySelector('.quantity');
        let filteredArray = this.cart.filter((prod, i) => i !== id );
        this.cart = filteredArray;
        localStorage.setItem('cart', JSON.stringify(filteredArray));
        let total = 0;
        this.cart.forEach(item => {
            total += item.price;
            localStorage.setItem('total', JSON.stringify(total));
        })
        quantity.innerText = this.cart.length;
        console.log('deleted');
    }

    show() {
        let list = '';
        let total = 0;
        this.cart.forEach(element => {
            list += `<div class="product-item">
                <div class="left-side">
                    <img src="${element.imageSrc}" alt="product image"/>
                    <p class="product-title">${element.title}</p>
                </div>
                <div class="right-side">
                    <p class="product-price">Цена: ${element.price} р.</p>
                    <button class="delete-button">Убрать из списка</button>
                </div>
           
            </div>`;
            total += +element.price;
        });
        list += `<div class="result">
            <div class="total-price">Сумма: ${total} р.</div>
            <a href="thankyoupage/">Заказать</a>
        </div>`;
        localStorage.setItem('totalPrice', JSON.stringify(total));
        productListContainer.innerHTML = this.cart.length > 0 ? list : '<h3 class="message">Корзина пуста</h3>';
        this.addEvents();
    }
}

let cartList = new ProductCartList();
