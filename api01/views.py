# 載入 Python 庫
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import pickle
import numpy as np
import os


# 載入模型
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# 手動設定 R²，這個是你訓練時算出來的，自己填上
MODEL_R2 = 0.92  # <--- 這個可以改成你自己模型的 R²值

# 加這個：負責顯示網頁
def index(request):
    contact_info = {
        "name": "CCYu",
        "title": "Freelancer",
        "email": "kenjo0530@yahoo.com.tw",
        "phone": "+886-912-345-678",
        "skills": [
            "Python",
            "Django REST API",
            "Data Analysis",
            "Machine Learning",
            "Project Management"
        ],
        "link": {
            "LinkedIn": "https://www.linkedin.com/in/ccyu",
            "Portfolio": "https://your-portfolio-site.com",
            "GitHub": "https://github.com/ccyu-dev"
        }
    }
    return render(request, 'predictor/index.html', {'skills': contact_info['skills'], 'link': contact_info['link'], 'name': contact_info['name'], 'title': contact_info['title'], 'email': contact_info['email'], 'phone': contact_info['phone']})


class PredictView(APIView):
    def post(self, request):
        data = request.data

        organic = data.get('organic')
        a_campaign = data.get('a_campaign')
        b_campaign = data.get('b_campaign')

        if organic is None or a_campaign is None or b_campaign is None:
            return Response({
                "success": False,
                "error": "Missing required fields: organic, a_campaign, b_campaign."
            }, status=400)

        try:
            X_input = np.array([[float(organic), float(a_campaign), float(b_campaign)]])
            prediction = model.predict(X_input)
            predicted_sales = round(prediction[0], 2)  # 四捨五入到小數點兩位

            return Response({
                "success": True,
                "input": {
                    "organic": organic,
                    "a_campaign": a_campaign,
                    "b_campaign": b_campaign
                },
                "predicted_sales": predicted_sales,
                "model_info": {
                    "r_squared": MODEL_R2
                }
            })

        except Exception as e:
            return Response({
                "success": False,
                "error": str(e)
            }, status=500)