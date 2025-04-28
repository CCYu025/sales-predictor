# 余振中 (Yu Chen Chung)
from rest_framework import routers
from django.urls import  path, include
from api01 import views

from .views import PredictView, index

urlpatterns = [
    path('', index, name='index'),               # 網站首頁 ➔ 顯示網頁
    path('predict/', PredictView.as_view(), name='predict'),  # API 路徑
]

# 建立 路由器
router = routers.DefaultRouter()
# 註冊 網址 對硬 視圖
# 127.0.0.1:8000/api 由 myproject/urls.py 負責設定
# 127.0.0.1:8000/api/products
# router.register(r'products', views.ProductViewSet)

# /api/product
# api 第一層路徑
# 建立列表 路徑 對映 網址 , path(路徑 , 網址)
# 不能打錯字 urlpatterns
# urlpatterns = [
#     path('', include(router.urls)),
#     path('user/<str:username>/orders/', UserOrderListView.as_view(),name='user_orders'),
# ]

