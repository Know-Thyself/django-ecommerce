class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('SESSION_KEY')
        if 'SESSION_KEY' not in self.session:
            cart = self.session['SESSION_KEY'] = {}
        self.cart = cart


def cart_context(request):
    return {'cart': Cart(request)}