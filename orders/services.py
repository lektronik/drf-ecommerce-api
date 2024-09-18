import stripe
from django.conf import settings

class StripeService:
    def __init__(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY

    def create_payment_intent(self, amount, currency='usd'):
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
        )
        return intent

    def retrieve_payment_intent(self, payment_intent_id):
        intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        return intent
