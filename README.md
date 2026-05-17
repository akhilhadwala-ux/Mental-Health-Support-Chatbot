Here is the complete `README.md` file for your project:

# Mental Health Support Chatbot

A compassionate AI-powered mental health support chatbot built using Streamlit and Google Gemini API.

This chatbot provides emotional support, coping suggestions, and empathetic conversations while maintaining safe AI boundaries through both input and output validation.

---

# Features

* 💬 Conversational mental health support
* 🤖 Powered by Gemini 2.5 Flash Lite
* ✅ Input validation using Pydantic
* 🛡️ Output validation for safer responses
* 🧠 Session-based chat memory using Streamlit
* 🔐 Environment variable support with `.env`
* ☁️ Deployed on AWS EC2
* ⚡ Fast and lightweight UI with Streamlit

---

# Project Structure

```bash
project/
│
├── app.py              # Main Streamlit application
├── .env                # API key storage
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---

# Technologies Used

* Python
* Streamlit
* Google Gemini API
* Pydantic
* python-dotenv
* AWS EC2

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/mental-health-chatbot.git
cd mental-health-chatbot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```txt
streamlit
google-genai
python-dotenv
pydantic
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
gemini_key=YOUR_GEMINI_API_KEY
```

Get your Gemini API key from:

[Google AI Studio](https://aistudio.google.com?utm_source=chatgpt.com)

---

# Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at:

```bash
http://localhost:8501
```

---

# Input Validation

The chatbot validates user input before sending it to Gemini.

### Validation Checks

* Empty input prevention
* Minimum word count validation
* Numeric-only input restriction

Example:

```python
if len(value.split()) < 5:
    raise ValueError("Input must contain at least 5 words")
```

---

# Output Validation

The chatbot validates AI-generated responses before displaying them.

### Validation Checks

* Empty response prevention
* Very short response filtering
* Maximum response length restriction

Example:

```python
if len(value.split()) > 120:
    raise ValueError("Response too long")
```

---

# Deployment on AWS EC2

This application is deployed on an AWS EC2 instance using Streamlit.

---

## EC2 Deployment Steps

### 1. Launch EC2 Instance

Recommended configuration:

* Ubuntu Server 26.04 LTS (HVM), SSD Volume Type
* t3.micro (Free Tier eligible)
---

### 2. Connect to EC2

```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

---

### 3. Update System Packages

```bash
sudo apt update && sudo apt upgrade -y
```

---

### 4. Install Python & Git

```bash
sudo apt install python3-pip python3-venv git -y
```

---

### 5. Clone Repository

```bash
git clone https://github.com/your-username/mental-health-chatbot.git
cd mental-health-chatbot
```

---

### 6. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 7. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 8. Configure Environment Variables

Create a `.env` file:

```bash
nano .env
```

Add:

```env
gemini_key=YOUR_GEMINI_API_KEY
```

---

### 9. Run Streamlit Application

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```
---

# ⚠️ Disclaimer

This project is designed for emotional support and educational purposes only.

It is **NOT**:

* A licensed therapist
* A medical professional
* A replacement for professional mental health care

If someone is in crisis or immediate danger, contact local emergency services or a mental health professional immediately.

---
---

# 🔮 Future Improvements

* Crisis detection system
* Sentiment analysis
* Chat history export
* Multi-language support
* Voice interaction
* Authentication system
* Database integration

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed with ❤️ using Streamlit, Gemini AI, and AWS EC2.
