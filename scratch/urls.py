from django.urls import path

from .views import (
    customer,
    #contacts,
    workorder_create_view,
    custom_workorder_create,
)



app_name='scratch'
urlpatterns = [
    path("dynamic/", customer, name='dynamic'),
    #path("contact/", contacts, name='contact'),
    path("create/", workorder_create_view, name='create'),
    path("custom/", custom_workorder_create, name='custom')
]