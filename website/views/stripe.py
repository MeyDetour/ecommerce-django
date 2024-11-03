import stripe
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ecommerce import settings
from website.models import Product, Order, ItemOrder
from website.services.cart_services import Cart_service


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,

                success_url=domain_url + 'success',
                cancel_url=domain_url + 'cancelled',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price_data': {
                            'currency': 'eur',
                            'product_data': {
                                'name': 'Chaise',
                            },
                            'unit_amount': 2000,  # Montant en centimes, donc ici 20,00 €
                        },
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})




def create_order(request):
    cart_service = Cart_service(request)
    cart_data = cart_service.get_cart()
    cart = []
    count = 0
    order = Order.objects.create(user=request.user, price=0)  # Créer la commande avec prix initial à 0

    for product_id, quantity in cart_data.items():
        product = Product.objects.get(id=product_id)
        cart.append({
            'product': product,
            'quantity': int(quantity)
        })
        order_item = ItemOrder.objects.create(
            product=product,
            quantity=int(quantity),
            order=order
        )
        count = int(quantity) * product.price

    order.price = count
    order.save()

    cart_service.remove_products(request)
    return Order


def cancelled(request):
    if not request.user.is_authenticated:
        return  HttpResponseRedirect('/login')
    return  render(request, 'website/client/user/cancelled.html')
def success(request):
    if not request.user.is_authenticated:
        return  HttpResponseRedirect('/login')
    create_order(request)
    return  render(request, 'website/client/user/success.html')
