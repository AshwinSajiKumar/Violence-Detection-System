# 🚨 Violence Detection System

A real-time AI-powered violence detection system that analyzes video content to identify violent activities and automatically sends alerts via Telegram.

## 🌟 Features

- **Real-time Video Analysis**: Upload and analyze MP4 videos for violence detection
- **AI-Powered Detection**: Uses LRCN (Long-term Recurrent Convolutional Network) model for action recognition
- **Face Detection**: Automatically detects and captures faces from violence frames using MTCNN
- **Telegram Integration**: Instant alerts with images sent to Telegram when violence is detected
- **Web Interface**: Clean, user-friendly Streamlit web application
- **Multi-class Detection**: Detects Punch, Kick, and Walking actions with confidence scores

## 🤖 Telegram Bot Integration

The system includes a fully integrated Telegram bot that provides real-time alerts:

### **Alert Features:**
- **Instant Notifications**: Sends alerts immediately when violence is detected
- **Location Tracking**: Includes location information (Jail Block 2)
- **Timestamp**: Precise time of detection
- **Face Count**: Number of faces detected in the frame
- **Image Attachments**: Sends both violence frame and detected faces

### **Alert Format:**
```
🚨 VIOLENCE ALERT!!
📍 LOCATION: Jail Block 2
⏰ TIME: [Timestamp]
👥 FACES DETECTED: [Number]
```

### **Images Sent:**
1. **Violence Frame**: The exact frame where violence was detected
2. **Faces Detected**: Cropped images of all detected faces

## 🎯 How to Use

### **1. Access the Application**
Visit the live application: [Violence Detection System](https://violence-detection-system-production-5415.up.railway.app/)

### **2. Upload Video**
- Click on the file uploader
- Select an MP4 video file
- The video will be displayed for preview

### **3. Analyze Video**
- Click the **"🔍 Analyze Video"** button
- The system will process the video frame by frame
- Wait for the analysis to complete

### **4. View Results**
- **Violence Detected**: Red alert with Telegram notification sent
- **No Violence**: Green success message
- **Action Details**: Shows detected action and confidence score

### **5. Telegram Alerts**
When violence is detected:
- ✅ Automatic Telegram alert sent
- ✅ Violence frame image attached
- ✅ Face detection results included
- ✅ Location and timestamp provided

## 🔧 Technical Details

### **AI Model**
- **Architecture**: LRCN (Long-term Recurrent Convolutional Network)
- **Classes**: Punch, Kick, Walking
- **Input**: 64x64 pixel frames
- **Output**: Action classification with confidence scores

### **Face Detection**
- **Model**: MTCNN (Multi-task Cascaded Convolutional Networks)
- **Features**: Real-time face detection and cropping
- **Output**: Individual face images for identification

### **Video Processing**
- **Format**: MP4 files
- **Processing**: Frame-by-frame analysis
- **Temporary Storage**: Automatic cleanup after processing

## 📱 Telegram Bot Setup

The system includes a fully integrated Telegram bot that provides real-time alerts. To set up your own Telegram bot:

### **Step 1: Create Telegram Bot**
1. **Open Telegram** and search for **@BotFather**
2. **Start a chat** with BotFather
3. **Send `/newbot`** command
4. **Choose a name** for your bot (e.g., "Violence Detection Alert")
5. **Choose a username** ending with 'bot' (e.g., "violence_detection_bot")
6. **Copy the bot token** provided by BotFather

### **Step 2: Get Chat ID**
1. **Add your bot** to a group or start a private chat
2. **Send a message** to the bot
3. **Visit**: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
4. **Find your chat ID** in the response

### **Step 3: Update Configuration**
In `app.py`, replace the bot configuration:
```python
TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID_HERE'
```

### **Bot Features:**
When violence is detected, the bot automatically:
1. **Sends Text Alert** with location and timestamp
2. **Attaches Violence Frame** image
3. **Sends Face Images** if faces are detected
4. **Provides Error Handling** if face detection fails

### **Message Format:**
- **HTML-formatted** alerts with emojis
- **Automatic image compression** and sending
- **Location tracking** and precise timestamps

## 🎨 User Interface

### **Clean Design**
- **Minimal Interface**: Focus on core functionality
- **Responsive Layout**: Works on desktop and mobile
- **Real-time Feedback**: Progress indicators and status messages
- **Professional Styling**: Modern, clean appearance

### **Interactive Elements**
- **File Upload**: Drag-and-drop or click to upload
- **Video Preview**: Instant video playback
- **Analysis Button**: Prominent call-to-action
- **Results Display**: Clear success/error messages

## ⚡ Performance

- **Fast Processing**: Optimized for quick video analysis
- **Memory Efficient**: Automatic cleanup of temporary files
- **Scalable**: Handles various video sizes and formats
- **Reliable**: Robust error handling and recovery

## 🔒 Privacy & Security

- **Local Processing**: Video analysis happens on the server
- **Temporary Storage**: Files are automatically deleted after processing
- **Secure Alerts**: Telegram messages are encrypted
- **No Data Retention**: No permanent storage of uploaded videos

## 🚀 Live Demo

**Try it now**: [https://violence-detection-system-production-5415.up.railway.app/](https://violence-detection-system-production-5415.up.railway.app/)

Upload a video and experience real-time violence detection with instant Telegram alerts!

---

**Built with ❤️ using Streamlit, TensorFlow, and OpenCV** 
