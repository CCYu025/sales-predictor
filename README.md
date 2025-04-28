# Sales Predictor - 銷售預測小工具

這是一個使用 Django + 機器學習 + Render 雲端部署完成的銷售預測專案。  
可以根據自然銷售量與行銷活動數據，預測最終銷售量。

---

## 📈 專案功能

- 使用者可以在網頁上輸入 `Organic`、`A Campaign`、`B Campaign`
- 後端透過 Django REST Framework 提供 API
- 使用訓練好的 Scikit-learn 線性回歸模型 (`model.pkl`) 進行預測
- 支援前端網頁直接連線 API
- 成功部署到 Render，線上可即時使用

---

## 🚀 線上體驗網址

👉 [https://sales-predictor-mb8q.onrender.com/api/](https://sales-predictor-mb8q.onrender.com/api/)

> （註：首頁 `/` 會自動跳轉到 `/api/`）

---

## ⚙️ 使用技術

- Python 3.11
- Django 5.2
- Django REST Framework
- Scikit-learn 1.6
- Gunicorn (Production Server)
- Render 雲端部署
- Docker 打包（本地測試）
- HTML + CSS + JavaScript （前端表單）

---

## 🛠️ 本地安裝與執行

```bash
# 1. 下載專案
git clone https://github.com/CCYu025/sales-predictor.git

# 2. 進入資料夾
cd sales-predictor

# 3. 建立虛擬環境
python -m venv .venv
source .venv/bin/activate   # Windows 請用 .venv\Scripts\activate

# 4. 安裝必要套件
pip install -r requirements.txt

# 5. 啟動開發伺服器
python manage.py runserver
瀏覽器開啟：http://127.0.0.1:8000/api/

🧩 API 說明
POST /api/predict/

Request:

json
複製
{
  "organic": 120,
  "a_campaign": 50,
  "b_campaign": 30
}
Response:

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
## 🐛 開發過程中遇到的問題紀錄

| 問題描述 | 解決方式 |
|:---|:---|
| 部署後首頁出現 404 Page Not Found | 原本首頁 `/` 沒有對應的 view，導致直接訪問主網域時出現 404。<br>**解法：** 在 `views.py` 新增一個 `home` 函式，使用 `redirect('/api/')` 讓首頁自動跳轉到 `/api/`。並在 `urls.py` 設定 `path('', home, name='home')`。 |
| Render ALLOWED_HOSTS 錯誤 | 在 settings.py 裡補上 Render 網域名稱，解決 DisallowedHost 錯誤。 |
| 502 Bad Gateway 部署錯誤 | 因為 .gitignore 忽略掉了 model.pkl，導致模型遺失，補上模型後重新部署成功。 |
| API 路徑錯誤導致前端連不到資料 | 確認前端 Fetch 使用正確的 `/api/predict/` 路徑，且在本地、Render上都一致。 |
| Sklearn 警告：版本不一致 | 本地與 Render Sklearn 版本不同，產生警告，實測不影響功能，暫時保留警告。 |

🏆 專案成果
成功完成後端API建置

成功串接前端網頁

成功上傳 GitHub、撰寫 README

成功部署至 Render 雲端平台

🙌 聯絡方式
如果你對這個小專案有任何建議，或希望交流，可以透過 GitHub Issue 聯絡我！