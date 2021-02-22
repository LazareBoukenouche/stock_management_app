from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [

    path('', views.list_articles, name="list_articles"),
    path('articles/add', views.add_article, name="add_article"),
    path('articles/delete/<int:pk>', views.delete_article, name="delete_article"),
    path('articles/modify/<int:pk>', views.modify_article, name="modify_article"),

    path('supplier', views.list_supplier, name='list_supplier'),
    path('supplier/add', views.add_supplier, name="add_supplier"),
    path('supplier/delete/<int:pk>', views.delete_supplier, name="delete_supplier"),
    path('supplier/modify/<int:pk>', views.modify_supplier, name="modify_supplier"),

    path('order', views.list_order, name="list_order"),
    path('order/create', views.create_order, name="create_order"),
    path('order/create/add_items/<int:pk>', views.add_items_to_order, name="add_items_to_order"),
    path('order/delete/order_items/<int:pk>', views.delete_order_items, name="delete_order_items"),
    path('order/delete/<int:pk>', views.delete_order, name="delete_order"),
    path('order/modify/<int:pk>', views.modify_order, name="modify_order"),
    path('order/merge/', views.merge_order, name="merge_order"),
    path('order/delete_merged_order/<int:pk>', views.delete_merged_order, name="delete_merged_order"),
    path('order/modify_merged_order/<int:pk>', views.modify_merged_order, name="modify_merged_order"),

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

