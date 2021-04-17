

class Cart():
    """
    A base Cart class for some default behaviour that can be overridden if necessary.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('s_key')
        if 's_key' not in request.session:
            cart = self.session['s_key'] = {}
        self.cart = cart

    def add(self, product, qty):
        """
        Adding and updating the users session data
        """
        product_id = product.id
        if product_id not in self.cart:
            self.cart[product_id] = {"price": str(product.price), "qty": int(qty)}

        self.session.modified = True   # tells django explicitly that the session has been modified

    def __len__(self):
        """
        Get basket data and count qty of items
        """
        return sum(item['qty'] for item in self.cart.values())
