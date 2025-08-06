from django.urls import include, path

from apps.payments.views import OrderCreateAPIView

app_name = "payments"


urlpatterns = [
    path("order/create/", OrderCreateAPIView.as_view(), name="create-order"),
    # Payment Provider callbacks
    path("paylov/", include("apps.payments.paylov.urls", namespace="paylov")),
]
