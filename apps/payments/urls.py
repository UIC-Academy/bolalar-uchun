from django.urls import include, path

from apps.payments.views import OrderCreateAPIView, AddUserCardAPIView

app_name = "payments"


urlpatterns = [
    path("order/create/", OrderCreateAPIView.as_view(), name="create-order"),
    path("usercard/add/", AddUserCardAPIView.as_view(), name="add-usercard"),
    # Payment Provider callbacks
    path("paylov/", include("apps.payments.paylov.urls", namespace="paylov")),
]
