from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import request_payment_and_send_conf, confirm_token, get_message_id

urlpatterns = [
    path('twizo/confirm/<int:user_id>', request_payment_and_send_conf),
    path('twizo/check/<slug:messageID>/<int:token>', confirm_token),
    path('twizo/messageId/<int:user_id>', get_message_id),
]

urlpatterns = format_suffix_patterns(urlpatterns)
