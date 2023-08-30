from decimal import Decimal
from store.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('SESSION_KEY')
        if 'SESSION_KEY' not in self.session:
            cart = self.session['SESSION_KEY'] = {}
        self.cart = cart

    def add_to_cart(self, product, quantity):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id] = {'price': str(product.price), 'quantity': quantity}
        self.session.modified = True

    def get_cart_quantity(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys() # Ids of products added to cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'][1:])
            item['total'] = f"£{str(item['price'] * item['quantity'])}"
            yield item


def cart_context(request):
    return {'cart': Cart(request)}
