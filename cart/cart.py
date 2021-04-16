

class Cart():
    """
    A base Cart class for some default behaviour that can be overridden if necessary.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('s_key')
        if 's_key' not in request.session:
            cart = self.session['s_key'] = {'number': 23516}
        self.cart = cart
