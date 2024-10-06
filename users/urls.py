from users.apps import UsersConfig
from users.views import PaymentListAPIView, PaymentCreateAPIView
from django.urls import path

app_name = UsersConfig.name



urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payments_list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='create_payment'),
]