# 🤖💪 AI-Powered BMI Calculator & Health Assistant


![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3.0-000000?style=flat-square&logo=flask&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_AI-Gemini-4285F4?style=flat-square&logo=google&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-4EA94B?style=flat-square&logo=mongodb&logoColor=white)
![PyMongo](https://img.shields.io/badge/PyMongo-4.5.0-green?style=flat-square)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Generative AI](https://img.shields.io/badge/Generative_AI-FF6B6B?style=flat-square)



## 🎯 Overview

AI-Powered BMI Calculator is an intelligent health assistant that combines traditional BMI calculation with advanced AI capabilities using Google Gemini. The application not only calculates your Body Mass Index but also provides personalized diet plans and workout routines tailored to your specific health goals.

## 🎥 Demo




https://github.com/user-attachments/assets/ba6b4c72-0550-40e8-9dab-8881a4dfbf1d




## Mongo Db Storage

<img width="1916" height="1079" alt="image" src="https://github.com/user-attachments/assets/7d238e9e-17e8-4e69-827a-b155d585fb3a" />


<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/1ad9e1f5-02a3-42eb-820d-5e9278eacf0b" />

## Mongosh Shell Retrive Data

<img width="1693" height="702" alt="image" src="https://github.com/user-attachments/assets/3c6ec6af-7034-40d2-9326-fa1e81cb3d0a" />


## ✨ Features

<div align="center">

| 🎯 Feature | 📝 Description |
|------------|----------------|
| **🧮 Smart BMI Calculation** | Accurate BMI computation with health categorization |
| **🤖 AI-Powered Insights** | Google Gemini integration for intelligent recommendations |
| **🥗 Custom Diet Plans** | Personalized nutrition recommendations based on BMI |
| **💪 Workout Routines** | AI-generated exercise plans tailored to fitness goals |
| **📊 Data Persistence** | MongoDB storage for user progress tracking |
| **🌐 Web Interface** | Clean, responsive HTML/CSS frontend |
| **⚡ REST API** | Flask-based API for seamless integration |
| **📱 Mobile Friendly** | Responsive design for all devices |

</div>

---

## 🧠 AI Integration

Our application leverages **Google Gemini AI** to provide intelligent health recommendations:

```mermaid
graph TD
    A[User Input] --> B[BMI Calculation]
    B --> C[Google Gemini AI]
    C --> D[Health Analysis]
    D --> E[Diet Plan Generation]
    D --> F[Workout Plan Creation]
    E --> G[Personalized Recommendations]
    F --> G
    G --> H[MongoDB Storage]
    G --> I[User Dashboard]
```

### 🎯 AI Capabilities

- **📊 Health Assessment**: Comprehensive BMI analysis with health insights
- **🥗 Nutrition Planning**: Custom diet plans based on BMI category and goals  
- **💪 Fitness Coaching**: Personalized workout routines for different fitness levels
- **📈 Progress Tracking**: AI-driven recommendations for continuous improvement
- **🎯 Goal Setting**: Smart goal recommendations based on current health status

---



## 📡 API Endpoints

<details>
<summary><b>🔌 API Documentation</b></summary>

### 🧮 Calculate BMI

**POST** `/api/calculate-bmi`

**Request Body:**
```json
{
  "name": "John Doe",
  "weight": 75,
  "height": 175
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "name": "John Doe",
    "bmi": 24.49,
    "category": "Normal weight",
    "diet_plan": {
      "breakfast": "Oatmeal with fruits and nuts",
      "lunch": "Grilled chicken salad with mixed vegetables",
      "dinner": "Baked salmon with quinoa and steamed broccoli",
      "snacks": ["Greek yogurt", "Mixed nuts", "Fresh fruit"]
    },
    "workout_plan": {
      "cardio": "30 minutes moderate-intensity cardio, 3-4 times per week",
      "strength": "2-3 strength training sessions per week",
      "flexibility": "Daily stretching or yoga for 10-15 minutes"
    },
    "health_tips": [
      "Maintain current weight through balanced diet",
      "Stay hydrated with 8-10 glasses of water daily",
      "Get 7-9 hours of quality sleep"
    ]
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### 📊 Get All BMI Records

**GET** `/api/all-records`

**Response:**
```json
{
  "success": true,
  "count": 25,
  "records": [
    {
      "name": "John Doe",
      "bmi": 24.49,
      "category": "Normal weight",
      "timestamp": "2024-01-15T10:30:00Z"
    }
  ]
}
```

### 🔍 Get User Records

**GET** `/api/user/{name}`

**Response:**
```json
{
  "success": true,
  "user": "John Doe",
  "records": [
    {
      "bmi": 24.49,
      "weight": 75,
      "height": 175,
      "timestamp": "2024-01-15T10:30:00Z"
    }
  ]
}
```

</details>

---

## 🏗️ Project Structure

```
├── .gitignore
├── All_BMIS.html
├── BMI_Program.py
├── BMI_Service.py
└── Web_Interface.html
```

### 🗂️ File Descriptions

| File | Purpose | Key Functions |
|------|---------|---------------|
| `BMI_Program.py` | Main Flask app | Route handling, API endpoints |
| `BMI_Service.py` | Core logic | BMI calculation, AI integration, DB operations |
| `Web_Interface.html` | User interface | Input form, responsive design |
| `All_BMIS.html` | Records display | Show all BMI calculations |

---

## 🛠️ Technologies

<div align="center">


</div>

---

## 📊 Data Storage

### MongoDB Schema

```javascript
    {
        "name": "John Wick",
        "weight": 72.0,
        "height": 1.9,
        "bmi": 19.94,
        "bmi_status": "Underweight",
        "diet_suggestion": "Increase calorie intake with nutrient-rich foods.",
        "workout_suggestion": "Focus on strength training to build muscle mass."
    }
```

### 🏷️ BMI Categories

| BMI Range | Category | Health Status | Color Code |
|-----------|----------|---------------|------------|
| < 18.5 | Underweight | ⚠️ Below normal | 🔵 Blue |
| 18.5 - 24.9 | Normal | ✅ Healthy | 🟢 Green |
| 25.0 - 29.9 | Overweight | ⚠️ Above normal | 🟡 Yellow |
| ≥ 30.0 | Obese | ⚠️ High risk | 🔴 Red |

---

## 🐛 Issues & Support

Need help or found a bug?

- **🐛 Report Bugs**: [Create Issue](https://github.com/ARONAGENT/ai-bmi-calculator/issues/new?template=bug_report.md)
- **💡 Feature Requests**: [Request Feature](https://github.com/ARONAGENT/ai-bmi-calculator/issues/new?template=feature_request.md)
- **❓ Questions**: [GitHub Discussions](https://github.com/ARONAGENT/ai-bmi-calculator/discussions)
- **📧 Direct Contact**: [rohanuke1@gmail.com](mailto:rohanuke1@gmail.com)

---

## 📈 Roadmap

<details>
<summary><b>🗺️ Future Development Plans</b></summary>

### Version 2.0 (Coming Soon)

- [ ] **🔐 User Authentication**: Secure login and personalized dashboards
- [ ] **📊 Advanced Analytics**: Detailed health trend analysis
- [ ] **🍎 Nutrition Tracking**: Calorie and macro tracking integration
- [ ] **🏃‍♂️ Activity Monitoring**: Fitness tracker integration
- [ ] **🩺 Health Metrics**: Blood pressure, heart rate monitoring
- [ ] **👥 Social Features**: Share progress with friends and family

### Version 3.0 (Future)

- [ ] **🤖 Advanced AI**: Multiple AI model integration
- [ ] **📱 Mobile App**: Native iOS and Android applications
- [ ] **🌍 Multi-language**: Support for 10+ languages
- [ ] **🩺 Medical Integration**: Healthcare provider connectivity
- [ ] **🎯 AI Coach**: 24/7 personalized health coaching

</details>

---

## 📄 License
```
Copyright (c) 2024 ARONAGENT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software")...
```

---

## 🙏 Acknowledgments

- **🤖 Google AI Team**: For the amazing Gemini API
- **🍃 MongoDB Team**: For robust database solutions
- **🌶️ Flask Community**: For the lightweight web framework
- **👥 Contributors**: All developers who helped improve this project
- **🩺 Health Experts**: For guidance on safe BMI calculations

### 🎯 **"Your AI-Powered Path to Better Health"**

**Built with ❤️ by [ARONAGENT](https://github.com/ARONAGENT)**

