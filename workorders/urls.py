from django.urls import path

from .views import (
    workorder_list_view,
    workorder_create_view,
    workorder_detail_view,
    workorder_detail_hx_view,
    workorder_update_view,
    workorder_inventory_update_hx_view,
    workorder_noninventory_update_hx_view,
    workorder_service_update_hx_view,
    customer,
    contacts,
    custom_workorder_create,
    
)

app_name='workorders'
urlpatterns = [
    path("", workorder_list_view, name='list'),
    #path("dynamic/", customer, name='dynamic'),
    #path("contact/", contacts, name='contact'),

    path("dynamic/", customer, name='dynamic'),
    #path("contact/", contacts, name='contact'),
    path("custom/", custom_workorder_create, name='custom'),
    path('contacts/', contacts, name='contacts'),

    path("create/", workorder_create_view, name='create'),
    path("hx/<str:parent_id>/inventory/", workorder_inventory_update_hx_view, name='hx-inventory-create'),
    path("hx/<str:parent_id>/inventory/<int:id>/", workorder_inventory_update_hx_view, name='hx-workorder-inventory-detail'),
    path("hx/<str:parent_id>/noninventory/", workorder_noninventory_update_hx_view, name='hx-noninventory-create'),
    path("hx/<str:parent_id>/noninventory/<int:id>/", workorder_noninventory_update_hx_view, name='hx-workorder-noninventory-detail'),
    path("hx/<str:parent_id>/service/", workorder_service_update_hx_view, name='hx-service-create'),
    path("hx/<str:parent_id>/service/<int:id>/", workorder_service_update_hx_view, name='hx-workorder-service-detail'),
    path("hx/<str:id>/", workorder_detail_hx_view, name='hx-detail'),
    path("<str:id>/edit", workorder_update_view, name='update'),
    path("<str:id>/", workorder_detail_view, name='detail'),

    
]