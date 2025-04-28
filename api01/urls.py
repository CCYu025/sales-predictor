# 余振中 (Yu Chen Chung)

from django.urls import path
from .views import PredictView, index

urlpatterns = [
    path('', index, name='index'),                # 這行要有，才能顯示首頁！
    path('predict/', PredictView.as_view(), name='predict'),
]