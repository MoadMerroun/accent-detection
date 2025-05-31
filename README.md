---
title: Accent Detection
emoji: 🚀
colorFrom: red
colorTo: red
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: Streamlit template space
---

## 🚀 How to Use
👉 [Click here to open the app](https://huggingface.co/spaces/MoadMerroun/accent-detection)

1. Paste a public video URL (e.g., Google Drive MP4 link)
2. Click "Analyze"
3. See results: accent + confidence score

> ⚠️ Only works with publicly accessible video links (not password-protected).


## ⚙️ Local Setup

```bash
# Clone repo
git clone https://huggingface.co/spaces/MoadMerroun/english-accent-detection
cd accent-detector

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run .\src\streamlit_app.py
```
