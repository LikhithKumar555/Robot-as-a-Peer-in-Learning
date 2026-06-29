# 🤖 Robot-Assisted Quiz – Study on Peer vs Tutor Roles

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A web-based experiment investigating how robot roles (peer vs. tutor) affect help-seeking behaviour and comfort in learning tasks.

**Live Demo:** (https://antonym-perfectly-favoring.ngrok-free.dev/) *(if deployed)*

---

## 📖 Study Overview

This project is part of a user study in interactive intelligent systems. Based on the theoretical framework of Belpaeme et al. (2018) on social robots in education, we examine:

- **H1**: Students working with a **robot peer** will ask for help more often than those with a **robot tutor**.
- **H2**: Students in the peer condition will report **higher comfort** and **lower stress** than those in the tutor condition.

### Robot Roles

| Role | Behaviour | Help Type |
|------|-----------|-----------|
| **Peer** | Collaborative, "I'm learning with you" | Removes a wrong option (hint) |
| **Tutor** | Authoritative, "I know the answer" | Gives a clue toward the correct answer |

---

## 🧪 Experiment Design

- **Participants**: 6 university students (3 per condition)
- **Design**: Between-subjects (participant chooses role)
- **Quiz**: 10 multiple-choice questions (European football theme)
- **Modes**: Voice-based (speech recognition) and typing-based questions
- **Data collected**:
  - Number of help requests
  - Comfort rating (1-7)
  - Task score (% correct)
  - Manipulation check
  - Demographics (age, gender)

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3.8+ / Flask |
| **Frontend** | HTML5, CSS3, Vanilla JS |
| **Speech** | Web Speech API (SpeechSynthesis + SpeechRecognition) |
| **Deployment** | Render / Heroku / PythonAnywhere |
| **Data** | CSV (experiment_data.csv + help_log.csv) |

---

## 📁 Project Structure
