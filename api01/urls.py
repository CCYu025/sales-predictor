# 余振中 (Yu Chen Chung)
from django.urls import path
from .views import PredictView, index

urlpatterns = [
    path('', index, name='index'),                      # 首頁 ➔ 顯示 HTML 頁面
    path('predict/', PredictView.as_view(), name='predict'),  # API ➔ 預測功能
]