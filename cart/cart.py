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


def cart_context(request):
    return {'cart': Cart(request)}
