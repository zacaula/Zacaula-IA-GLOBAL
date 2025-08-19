from django.http import HttpResponse
from paypalrestsdk import Payment
import requests
def crear_pedido(request):
    payment = Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "transactions": [{
            "amount": {
                "total": "10.00",
                "currency": "USD"
            },
            "description": "Prueba de pago
