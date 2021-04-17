from shop.models import Product
from decimal import Decimal


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

    def __iter__(self):
        """"
        Collect the product_id in the session, query the database and return products
        """
        product_ids = self.cart.keys()
        products = Product.products.filter(id__in=product_ids)
        cart = self.cart.copy()

        # extend the cart data from the session to add product information (picture, description and so on)
        for product in products:
            cart[str(product.id)]['product'] = product

        # loop trough the session data product and capture price and quantity data, add to product information
        for item in cart.values():
            item['price'] = Decimal(item['price'])  # change data type to decimal
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        Get basket data and count qty of items
        """
        return sum(item['qty'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
