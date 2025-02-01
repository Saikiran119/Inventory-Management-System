# inventory/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


app_name = 'inventory'

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('delete-sale/<int:sale_id>/', views.delete_sale, name='delete_sale'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('low-stock/', views.low_stock_alerts, name='low_stock_alerts'),
    path('sales-summary/', views.sales_summary, name='sales_summary'),
    # path('product-list/', views.product_list, name='product_list'),
    path('add-sale/<int:product_id>/', views.add_sale, name='add_sale'),
    path('products/', views.inventory_list, name='inventory_list'),
    path('product-list/', views.product_list, name='product_list'),
    path('reports/', views.reports_view, name='reports'),
    path('export-low-stock-excel/', views.export_low_stock_excel, name='export_low_stock_excel'),
    path('export-sales-summary-excel/', views.export_sales_summary_excel, name='export_sales_summary_excel'),
    path('export-low-stock-csv/', views.export_low_stock_csv, name='export_low_stock_csv'),
    path('export-sales-summary-csv/', views.export_sales_summary_csv, name='export_sales_summary_csv'),
    path('place_order/<int:product_id>/', views.place_order, name='place_order'),
    path('order_success/<int:order_id>/', views.order_success, name='order_success'),
    path('order_failed/<int:order_id>/', views.order_failed, name='order_failed'),
    path('inventory/', views.inventory_view, name='inventory_view'),
    path('order_history/', views.order_history, name='order_history'),  # URL without product_id (all orders)
    path('order_history/<int:product_id>/', views.order_history, name='order_history_for_product'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('login/', views.login_view, name='login'),  # Login page
    path('signup/', views.signup_view, name='signup'),  # Sign-up page (you need to define it)
    path('logout/', LogoutView.as_view(), name='logout'),
    path('order/confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('order/history/<int:product_id>/', views.order_history, name='order_history_filtered'),
    path('order/history/', views.order_history, name='order_history'),

]
