class Cart_service:
    def __init__(self, request):

        if 'user_cart' not in request.session:
            request.session['user_cart'] = {}

        self.cart = request.session.get('user_cart')

    def save_cart(self, request):
        request.session['user_cart'] = self.cart

    def add(self, product_id, request):
        product_id = str(product_id)  # Convertir en chaîne

        if product_id not in self.cart.keys() :
            self.cart[product_id] = 1
        else :
            self.cart[product_id] += 1
        self.save_cart(request)
    def get_quantity(self,product_id):
        product_id = str(product_id)  # Convertir en chaîne
        return self.cart[product_id]

    def get_cart(self):
        return self.cart
    def remove_one_of_product(self , product_id,request):
        product_id = str(product_id)  # Convertir en chaîne

        if product_id  in self.cart.keys() :
            self.cart[product_id] -= 1
            self.save_cart(request)
            print(self.cart)
            if self.cart[product_id] == 0:
                del self.cart[product_id]
                self.save_cart(request)
                return 0
            else :
                return self.cart[product_id]
    def remove_product(self , product_id,request):
        product_id = str(product_id)  # Convertir en chaîne

        if product_id  in self.cart.keys() :
            del self.cart[product_id]
        self.save_cart(request)
    def remove_products(self ,request):
        self.cart = {}
        self.save_cart(request)