from django.shortcuts import render
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt # 關閉 CSRF 保護，方便測試
def get_weather(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            city = data['city']
            latitude = data['latitude']
            longitude = data['longitude']
            # latitude = 121
            # longitude = 22

            # 不使用
            cities = {
                "台北": {"latitude": 25.0478, "longitude": 121.5319},
                "高雄": {"latitude": 22.6273, "longitude": 120.3014},
                "台中": {"latitude": 24.1477, "longitude": 120.6736},
                "台南": {"latitude": 22.9999, "longitude": 120.2270},
            }

            url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=relative_humidity_2m'
            response = requests.get(url)
            weather_data = response.json()
            print(weather_data)

            # 提取天氣數據
            temp_c = weather_data["current_weather"]["temperature"]  # 溫度 (°C)
            wind_kph = weather_data["current_weather"]["windspeed"]  # 風速 (km/h)
            weather_code = weather_data["current_weather"]["weathercode"]  # 天氣代碼
            humidity = weather_data["hourly"]["relative_humidity_2m"][0]  # 濕度 (%)

            # 天氣代碼對應的描述（簡單對應）
            weather_dict = {
                0: "晴天", 1: "主要晴朗", 2: "部分多雲", 3: "多雲",
                45: "霧", 48: "霧凍",
                51: "小毛毛雨", 53: "中毛毛雨", 55: "大毛毛雨",
                61: "小雨", 63: "中雨", 65: "大雨",
                80: "小陣雨", 81: "中陣雨", 82: "大陣雨",
            }
            weather_condition = weather_dict.get(weather_code, "未知天氣")

            # 顯示結果
            print("\n==============================")
            print(f"📍 城市: {city}")
            print(f"🌡 溫度: {temp_c}°C")
            print(f"☁ 天氣狀況: {weather_condition}")
            print(f"💧 濕度: {humidity}%")
            print(f"🌬 風速: {wind_kph} km/h")
            print("==============================\n")

            response_data = {
                '城市': city,
                '天氣狀況': weather_condition,
                '溫度': temp_c,
                '濕度': humidity,
                '風速': wind_kph,
            }
            print(response_data)

            return JsonResponse(response_data)


            # return JsonResponse(weather_data)


        # 伺服器會返回錯誤碼 格式錯誤 400
        except json.JSONDecodeError:

            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        # 伺服器會返回錯誤碼 缺少必要的參數 400
        except KeyError:

            return JsonResponse({'error': 'Missing latitude or longitude'}, status=400)

        # 伺服器會返回錯誤碼 其他類型的異常 400
        except Exception as e:

            print(e)

            return JsonResponse({'error': str(e)}, status=400)

    # 伺服器會返回錯誤碼 請求的方法不是 POST 405
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



