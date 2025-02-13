from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('form/', views.form, name='form'),
    path('profile/', views.profile, name='profile'),
    path('member/', views.member, name='member'),
    path('add_member', views.add_member, name='add_member'),
    path('edit_member/<int:member_id>/',views.edit_member, name='edit_member'),
    path('delete_member/<int:member_id>/',views.delete_member, name='delete_member'),
    path('detail_member/<int:member_id>/',views.detail_member, name='detail_member'),
    path('search_member/', views.search_member, name='search_member'),
    path('space/', views.space, name='space'),
    path('space_form/', views.space_form, name='space_form'),
    path('space_delete/<int:space_id>/', views.space_delete, name="space_delete"),
    path('space_detail/<int:space_id>/', views.space_detail, name="space_detail"),
    path('space_modif/<int:space_id>/', views.space_modif, name="space_modif"),
    path('appoint/', views.appoint_all, name='appoint'),
    path('appoint_detail/<int:appoint_id>/', views.appoint_detail, name='appoint_detail'),
    path('appoint_edit/<int:appoint_id>/', views.appoint_edit, name='appoint_edit'),
    path('property/', views.property, name='property'),
    path('property_form/', views.property_form, name='property_form'),
    path('property_detail/<int:property_id>/', views.property_detail, name='property_detail'),
    path('property_delete/<int:property_id>/', views.property_delete, name='property_delete'),
    path('property_modif/<int:property_id>/', views.property_modif, name='property_modif'),
    path('receipt/', views.receipt, name='receipt'),
    path('receipt_form/', views.receipt_form, name='receipt_form'),
    path('receipt_detail/<int:receipt_id>/', views.receipt_detail,name='receipt_detail'),
    path('receipt_delete/<int:receipt_id>/', views.receipt_delete,name='receipt_delete'),
    path('receipt_modif/<int:receipt_id>/', views.receipt_modif,name='receipt_modif'),
    path('search_receipt/',views.search_receipt,name='search_receipt'),


]