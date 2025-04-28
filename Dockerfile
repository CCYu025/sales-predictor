# 使用官方 Python 基礎映像檔
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 複製所有專案檔案到容器
COPY . /app

# 升級 pip & 安裝所有必要套件
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 用 gunicorn 啟動 Django
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]