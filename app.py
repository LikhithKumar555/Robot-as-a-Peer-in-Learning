from flask import Flask, render_template, request, jsonify
import random
import csv
import os
from datetime import datetime

app = Flask(__name__)

# ---------- EUROPEAN FOOTBALL QUESTION SETS (same difficulty) ----------
SET_A = [
    {"q": "Which club has won the most UEFA Champions League titles?",
     "options": ["AC Milan", "Bayern Munich", "Real Madrid", "Liverpool"],
     "correct": "C",
     "clue": "They have won it 14 times, more than any other club."},
    {"q": "Who won the UEFA European Championship in 2016?",
     "options": ["France", "Portugal", "Germany", "Spain"],
     "correct": "B",
     "clue": "The winning goal was scored by Eder in extra time."},
    {"q": "Which country has the most FIFA World Cup titles?",
     "options": ["Brazil", "Germany", "Italy", "Argentina"],
     "correct": "A",
     "clue": "They have won 5 World Cups."},
    {"q": "Which player has won the most Ballon d'Or awards?",
     "options": ["Lionel Messi", "Cristiano Ronaldo", "Michel Platini", "Johan Cruyff"],
     "correct": "A",
     "clue": "He has won 8 Ballon d'Or trophies."},
    {"q": "Which English club won the Premier League in 2015-16?",
     "options": ["Leicester City", "Manchester City", "Arsenal", "Chelsea"],
     "correct": "A",
     "clue": "They were 5000-to-1 outsiders at the start of the season."},
    {"q": "Which stadium is the home of FC Barcelona?",
     "options": ["Santiago Bernabéu", "Camp Nou", "Wembley", "Allianz Arena"],
     "correct": "B",
     "clue": "It was built in 1957 and is one of the largest in Europe."},
    {"q": "Who is the all-time top scorer in the UEFA Champions League?",
     "options": ["Lionel Messi", "Cristiano Ronaldo", "Robert Lewandowski", "Raúl"],
     "correct": "B",
     "clue": "He has scored over 140 goals in the competition."},
    {"q": "Which country won the 2020 UEFA European Championship?",
     "options": ["England", "Italy", "Spain", "France"],
     "correct": "B",
     "clue": "They beat England in the final on penalties."},
    {"q": "Which club is known as 'The Red Devils'?",
     "options": ["Manchester United", "Liverpool", "Bayern Munich", "Juventus"],
     "correct": "A",
     "clue": "The nickname comes from the club's red shirts and a historical reference."},
    {"q": "Who was the top scorer in the 2022 FIFA World Cup?",
     "options": ["Kylian Mbappé", "Lionel Messi", "Neymar", "Julián Álvarez"],
     "correct": "A",
     "clue": "He scored 8 goals in the tournament, including a hat-trick in the final."},
]

SET_B = [
    {"q": "Which club has won the most English Premier League titles?",
     "options": ["Manchester United", "Liverpool", "Arsenal", "Manchester City"],
     "correct": "A",
     "clue": "They have won 20 top-division titles, the most in England."},
    {"q": "Who is the top scorer in UEFA European Championship history?",
     "options": ["Cristiano Ronaldo", "Michel Platini", "Alan Shearer", "Antoine Griezmann"],
     "correct": "A",
     "clue": "He has scored 14 goals across five editions."},
    {"q": "Which country has the most UEFA Champions League titles?",
     "options": ["Spain", "England", "Italy", "Germany"],
     "correct": "A",
     "clue": "Spanish clubs have won the trophy more than any other nation."},
    {"q": "Which German club won the Bundesliga in 2022-23?",
     "options": ["Borussia Dortmund", "Bayern Munich", "RB Leipzig", "Union Berlin"],
     "correct": "B",
     "clue": "They won it on the final day after a dramatic comeback."},
    {"q": "Who was the captain of the French team that won the 1998 World Cup?",
     "options": ["Zinedine Zidane", "Didier Deschamps", "Thierry Henry", "Laurent Blanc"],
     "correct": "B",
     "clue": "He later went on to manage the national team to a World Cup win in 2018."},
    {"q": "Which Italian club has the most Serie A titles?",
     "options": ["Juventus", "AC Milan", "Inter Milan", "Roma"],
     "correct": "A",
     "clue": "They have won 36 league championships."},
    {"q": "Who is the youngest player to score in a FIFA World Cup final?",
     "options": ["Pelé", "Kylian Mbappé", "Lionel Messi", "Diego Maradona"],
     "correct": "A",
     "clue": "He was 17 years old when he scored in the 1958 final."},
    {"q": "Which country hosted the 2022 FIFA World Cup?",
     "options": ["Qatar", "Russia", "Brazil", "Germany"],
     "correct": "A",
     "clue": "It was the first World Cup held in the Middle East."},
    {"q": "Which club won the 2021 UEFA Champions League?",
     "options": ["Chelsea", "Manchester City", "Real Madrid", "Liverpool"],
     "correct": "A",
     "clue": "They defeated Manchester City 1-0 in the final in Porto."},
    {"q": "Who is the all-time top scorer for the German national team?",
     "options": ["Gerd Müller", "Miroslav Klose", "Lukas Podolski", "Thomas Müller"],
     "correct": "B",
     "clue": "He scored 71 goals in 137 appearances and won the 2014 World Cup."},
]

# Mode mapping (tutor_mode, peer_mode) – unchanged
MODE_MAP = [
    ("voice", "voice"),
    ("voice", "voice"),
    ("voice", "voice"),
    ("voice", "voice"),
    ("voice", "typing"),
    ("voice", "typing"),
    ("typing", "typing"),
    ("typing", "typing"),
    ("typing", "typing"),
    ("typing", "typing"),
]

@app.route('/')
def index():
    question_set = random.choice(['A', 'B'])
    questions = SET_A if question_set == 'A' else SET_B
    participant_id = random.randint(1000, 9999)
    return render_template('index.html',
                           participant_id=participant_id,
                           questions=questions,
                           mode_map=MODE_MAP,
                           question_set=question_set)

@app.route('/save', methods=['POST'])
def save_data():
    data = request.json
    data['timestamp'] = datetime.now().isoformat()
    file_exists = os.path.isfile('experiment_data.csv')
    with open('experiment_data.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)
    return jsonify({"status": "ok"}), 200

@app.route('/log_help', methods=['POST'])
def log_help():
    data = request.json
    data['timestamp'] = datetime.now().isoformat()
    file_exists = os.path.isfile('help_log.csv')
    with open('help_log.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['participant_id', 'condition', 'question_index', 'question_text', 'hint_given', 'timestamp'])
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'participant_id': data.get('participant_id'),
            'condition': data.get('condition'),
            'question_index': data.get('question_index'),
            'question_text': data.get('question_text'),
            'hint_given': data.get('hint'),
            'timestamp': data['timestamp']
        })
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)