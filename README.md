# 🤖 Robot-Assisted Quiz – Study on Peer vs Tutor Roles

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

**A web-based experiment investigating how robot roles (peer vs. tutor) affect help-seeking behaviour and comfort in learning tasks.**

---

## 📖 Study Overview

This project is part of a user study in interactive intelligent systems at **Bielefeld University**. Based on the theoretical framework of Belpaeme et al. (2018) on social robots in education, we examine:

- **H1**: Students working with a **robot peer** will ask for help more often than those with a **robot tutor**.
- **H2**: Students in the peer condition will report **higher comfort** and **lower stress** than those in the tutor condition.

### Robot Roles

| Role | Behaviour | Help Type |
|------|-----------|-----------|
| **Peer** | Collaborative, "I'm learning with you" | Removes a wrong option (hint) |
| **Tutor** | Authoritative, "I know the answer" | Gives a clue toward the correct answer |

---

## 🧪 Experiment Design

| Aspect | Details |
|--------|---------|
| **Participants** | 6 university students (3 per condition) |
| **Design** | Between-subjects (participant chooses role) |
| **Quiz** | 10 multiple-choice questions (European football theme) |
| **Modes** | Voice-based (speech recognition) and typing-based questions |
| **Duration** | ~10-15 minutes per participant |

### Data Collected

| Variable | Measurement |
|----------|-------------|
| DV1 – Help requests | Count during task; logged automatically |
| DV2 – Comfort rating | 1–7 scale; post-task questionnaire |
| DV3 – Task score | Percentage correct; logged automatically |
| Manipulation check | "Did the robot act like a classmate or teacher?" |
| Demographics | Age, Gender |

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3.8+ / Flask |
| **Frontend** | HTML5, CSS3, Vanilla JS |
| **Speech** | Web Speech API (SpeechSynthesis + SpeechRecognition) |
| **Deployment** | Render / ngrok / Local server |
| **Data** | CSV (experiment_data.csv + help_log.csv) |

---

## 📁 Project Structure

```
robot-quiz/
├── app.py                    # Flask backend
├── requirements.txt          # Python dependencies
├── Procfile                  # For deployment (Render/Heroku)
├── templates/
│   └── index.html            # Main quiz interface
├── experiment_data.csv       # Created during runtime (auto-generated)
├── help_log.csv              # Peer help requests log (auto-generated)
└── README.md                 # This file
```

---

## 🚀 Local Development

### Prerequisites
- Python 3.8+
- A modern browser (Chrome, Edge, or Safari)
- (Optional) A microphone for voice-based questions

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/robot-quiz.git
   cd robot-quiz
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have `requirements.txt`, create it with:
   ```bash
   pip install flask
   pip freeze > requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 🌐 Deployment Options

### Option 1: ngrok (Quick testing with remote participants)

1. **Sign up** at [ngrok.com](https://ngrok.com) and get your authtoken.
2. **Authenticate**:
   ```bash
   ngrok config add-authtoken YOUR_AUTHTOKEN
   ```
3. **Run Flask** in Terminal 1:
   ```bash
   python app.py
   ```
4. **Expose with ngrok** in Terminal 2:
   ```bash
   ngrok http 5000
   ```
5. **Share** the `https://xxxx.ngrok-free.app` URL with participants.

> ⚠️ **Note**: Free ngrok sessions last ~2 hours and your laptop must stay on.

---

### Option 2: Render.com (Permanent hosting)

1. **Push your code to GitHub**.
2. **Create a new Web Service** on [Render.com](https://render.com).
3. **Connect** your GitHub repository.
4. **Settings**:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
5. **Deploy** – your app is live at `https://your-app.onrender.com`.

> ✅ **Benefits**: Always online, no laptop needed, permanent URL.

---

### Option 3: PythonAnywhere (Free alternative)

1. **Sign up** at [pythonanywhere.com](https://pythonanywhere.com).
2. **Upload** your `app.py` and `templates/` folder.
3. **Set up** a Flask web app with Python 3.10.
4. **Your URL**: `https://yourusername.pythonanywhere.com`.

---

## 📊 Data Collection

### experiment_data.csv

| Field | Description |
|-------|-------------|
| `participant_id` | Anonymous participant ID |
| `condition` | 'peer' or 'tutor' |
| `question_set` | 'A' or 'B' (parallel question sets) |
| `score` | Number of correct answers (0-10) |
| `help_count` | Total help requests |
| `comfort` | Rating 1-7 |
| `manipulation_check` | 'classmate' or 'teacher' |
| `age` | Participant's age |
| `gender` | Participant's gender |
| `timestamp` | Date and time of completion |

### help_log.csv (Peer condition only)

| Field | Description |
|-------|-------------|
| `participant_id` | Anonymous participant ID |
| `condition` | Always 'peer' |
| `question_index` | Question number (0-9) |
| `question_text` | Full question text |
| `hint_given` | The hint provided to the participant |
| `timestamp` | Date and time of help request |

---

## 📝 Post-Task Questionnaire

After completing the quiz, participants fill out:

1. **Comfort rating** (1-7): *"How comfortable did you feel during the task?"*
2. **Manipulation check**: *"Did the robot act more like a classmate or more like a teacher?"*
3. **Age**: [free text input]
4. **Gender**: [free text input]

> **Note**: Participants who fail the manipulation check are excluded from analysis.

---

## 🎯 Analysis Plan

| Variable | Test | Purpose |
|----------|------|---------|
| DV1 – Help requests | Independent-samples t-test | Main test for H1 |
| DV2 – Comfort rating | Independent-samples t-test | Main test for H2 |
| DV3 – Task score | Independent-samples t-test | Control check |

**Significance level**: `p < .05`

---

## 📚 References

Belpaeme, T., Kennedy, J., Ramachandran, A., Scassellati, B., & Tanaka, F. (2018). Social robots for education: A review. *Science Robotics, 3*(21), eaat5954.  
https://doi.org/10.1126/scirobotics.aat5954

---

## 👤 Author

Likhith Kumar
Sai Sura
Indra Karan
Bielefeld University  
Course: User Studies in Intelligent Systems  
Bielefeld

