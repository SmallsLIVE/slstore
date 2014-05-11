from oscar.apps.checkout import app

import views


class CheckoutApplication(app.CheckoutApplication):
    payment_details_view = views.PaymentDetailsView


application = CheckoutApplication()
