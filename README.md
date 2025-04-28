# Sales Predictor

一個基於 Django + 機器學習模型的小型銷售量預測網站。

本專案可以根據商品的自然銷售量與行銷活動數據，預測最終銷售量。

---

## 🔥 功能特色

- 網頁介面輸入 `Organic`、`A Campaign`、`B Campaign` 數據
- 後端使用 Django REST Framework 建立 API
- 預測模型為 Scikit-learn 線性迴歸（LinearRegression）
- 已部署到 Render 免費雲端平台
- 支援前端自適應，直接操作預測

---

## 🚀 線上體驗

👉 [前往使用](https://sales-predictor-mb8q.onrender.com/api/)

---

## 🛠️ 技術細節

- Python 3.11
- Django 5.2
- Django REST Framework
- Scikit-learn 1.6
- Gunicorn (Production WSGI Server)
- Render 雲端部署
- HTML + CSS + JavaScript 前端表單互動

---

## 📦 安裝與執行

本地開發測試：

```bash
# 1. 下載專案
git clone https://github.com/CCYu025/sales-predictor.git

# 2. 進入資料夾
cd sales-predictor

# 3. 建立虛擬環境
python -m venv .venv
source .venv/bin/activate   # (Mac/Linux)
# 或
.venv\Scripts\activate      # (Windows)

# 4. 安裝必要套件
pip install -r requirements.txt

# 5. 啟動本地伺服器
python manage.py runserver
開啟瀏覽器輸入： http://127.0.0.1:8000/api/

🧩 API 文件
預測 API
URL：POST /api/predict/

Content-Type：application/json

參數：


參數	類型	說明
organic	float	自然銷售量
a_campaign	float	A活動銷售量
b_campaign	float	B活動銷售量
回應範例：

json
複製
{
  "success": true,
  "input": {
    "organic": 120,
    "a_campaign": 50,
    "b_campaign": 30
  },
  "predicted_sales": 171.88,
  "model_info": {
    "r_squared": 0.92
  }
}
🙌 License
本專案僅作為個人練習用途，無商業授權。