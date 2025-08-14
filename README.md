# Violence Detection System

A machine learning-based violence detection system that uses AI to detect violent actions in video footage with real-time alerts via Telegram.

## 🚀 Quick Deploy

### Option 1: Streamlit Cloud (Recommended)
1. **Fork this repository** to your GitHub account
2. **Go to [share.streamlit.io](https://share.streamlit.io)**
3. **Connect your GitHub account**
4. **Select this repository**
5. **Set main file path**: `app.py`
6. **Click Deploy**

### Option 2: Railway
1. **Fork this repository**
2. **Go to [railway.app](https://railway.app)**
3. **Connect GitHub**
4. **Select this repository**
5. **Auto-deploy**

### Option 3: Render
1. **Fork this repository**
2. **Go to [render.com](https://render.com)**
3. **Create new Web Service**
4. **Connect GitHub repository**
5. **Set build command**: `pip install -r requirements.txt`
6. **Set start command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

## 🛠️ Local Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

## 📱 Telegram Bot Setup

1. **Create a Telegram bot** via @BotFather
2. **Get your bot token**
3. **Update the token** in `app.py`:
   ```python
   TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN'
   TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID'
   ```

## 🎯 Features

- **Real-time Violence Detection**
- **Face Detection & Extraction**
- **Telegram Alerts**
- **Image Enhancement**
- **Clean Web Interface**

## 📁 Project Structure

```
├── app.py                 # Main application
├── requirements.txt       # Dependencies
├── README.md             # This file
├── videos/               # Sample videos
├── static/               # Static assets
└── .streamlit/           # Streamlit config
```

## 🔧 Configuration

Update these settings in `app.py`:
- `TELEGRAM_BOT_TOKEN`: Your bot token
- `TELEGRAM_CHAT_ID`: Your chat/group ID
- Location settings for alerts

## 📄 License

For educational and research purposes only. 