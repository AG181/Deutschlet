import sys
import random
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFrame, QProgressBar, QTabWidget
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon

VERBS = [
    ("kämpfen", "драться"),
    ("beleidigen", "оскорблять"),
    ("verlangen", "требовать"),
    ("verbringen", "проводить время"),
    ("gabbern", "танцевать gabber / слушать gabber"),
    ("enden", "заканчиваться"),
    ("passieren", "происходить"),
    ("ermüden", "утомлять"),
    ("bevorzugen", "предпочитать"),
    ("ausgeben", "тратить"),
    ("stören", "беспокоить"),
    ("tanzen", "танцевать"),
    ("beleidigt werden", "быть оскорблённым"),
    ("ausrasten", "выходить из себя"),
    ("abhängen", "тусоваться"),
    ("konsumieren", "употреблять"),
    ("vermeiden", "избегать"),
    ("machen", "делать"),
    ("sagen", "говорить"),
    ("gehen", "идти"),
    ("kommen", "приходить"),
    ("sehen", "видеть"),
    ("wissen", "знать"),
    ("können", "мочь"),
    ("müssen", "должен"),
    ("wollen", "хотеть"),
    ("sollen", "следует"),
    ("dürfen", "разрешаться"),
    ("bleiben", "оставаться"),
    ("geben", "давать"),
    ("nehmen", "брать"),
    ("finden", "находить"),
    ("denken", "думать"),
    ("glauben", "верить"),
    ("arbeiten", "работать"),
    ("lernen", "учить"),
    ("studieren", "учиться (в вузе)"),
    ("lesen", "читать"),
    ("schreiben", "писать"),
    ("sprechen", "говорить"),
    ("hören", "слышать"),
    ("fragen", "спрашивать"),
    ("antworten", "отвечать"),
    ("verstehen", "понимать"),
    ("erklären", "объяснять"),
    ("zeigen", "показывать"),
    ("bringen", "приносить"),
    ("kaufen", "покупать"),
    ("verkaufen", "продавать"),
    ("bezahlen", "платить"),
    ("öffnen", "открывать"),
    ("schließen", "закрывать"),
    ("anfangen", "начинать"),
    ("aufhören", "заканчивать"),
    ("warten", "ждать"),
    ("suchen", "искать"),
    ("benutzen", "использовать"),
    ("brauchen", "нуждаться"),
    ("helfen", "помогать"),
    ("treffen", "встречать"),
    ("besuchen", "посещать"),
    ("wohnen", "жить"),
    ("leben", "жить"),
    ("reisen", "путешествовать"),
    ("fahren", "ехать"),
    ("fliegen", "лететь"),
    ("steigen", "подниматься"),
    ("fallen", "падать"),
    ("laufen", "бегать"),
    ("schwimmen", "плавать"),
    ("springen", "прыгать"),
    ("sitzen", "сидеть"),
    ("stehen", "стоять"),
    ("legen", "класть"),
    ("stellen", "ставить"),
    ("tragen", "носить"),
    ("ziehen", "тянуть"),
    ("bauen", "строить"),
    ("ändern", "менять"),
    ("verbessern", "улучшать"),
    ("verlieren", "терять"),
    ("gewinnen", "выигрывать"),
    ("erinnern", "помнить"),
    ("vergessen", "забывать"),
    ("entscheiden", "решать"),
    ("unterstützen", "поддерживать"),
    ("teilnehmen", "участвовать"),
    ("vergleichen", "сравнивать"),
    ("entwickeln", "развивать"),
    ("verursachen", "вызывать"),
    ("erscheinen", "появляться"),
    ("gehören", "принадлежать"),
    ("interessieren", "интересовать"),
    ("fühlen", "чувствовать"),
    ("lieben", "любить"),
    ("hassen", "ненавидеть"),
    ("lachen", "смеяться"),
    ("weinen", "плакать"),
    ("schlafen", "спать"),
    ("aufstehen", "вставать"),
    ("ankommen", "прибывать"),
    ("abfahren", "отправляться"),
    ("beginnen", "начинать"),
    ("regnen", "идти (о дожде)"),
    ("schneien", "идти (о снеге)"),
    ("scheinen", "светить"),
    ("wachsen", "расти"),
    ("drehen", "вращать"),
    ("drücken", "нажимать")
]

NOUNS = [
    ("der Späti", "круглосуточный магазин (сокр. Spätkauf)"),
    ("Berlin", "Берлин"),
    ("der Dude", "чувак"),
    ("der Schweinhund", "свинья, подлая собака (оскорбление)"),
    ("das Schwein", "свинья"),
    ("die Nacht", "ночь"),
    ("die Namen", "имена"),
    ("die Sache", "вещь, дело"),
    ("der Niederländer", "голландец"),
    ("die Niederlande", "Нидерланды"),
    ("die Party", "вечеринка"),
    ("das Ende", "конец"),
    ("die Drogen", "наркотики"),
    ("das Zuhause", "дом"),
    ("das Handy / das Telefon", "телефон"),
    ("der Thunderdome", "Thunderdome (рейв-событие)"),
    ("das Techno", "техно"),
    ("der Streit", "ссора, драка"),
    ("der Abend", "вечер"),
    ("der Vorteil", "преимущество"),
    ("der Nachteil", "недостаток"),
    ("die Entscheidung", "решение"),
    ("die Entwicklung", "развитие"),
    ("die Beziehung", "отношения"),
    ("die Erfahrung", "опыт"),
    ("die Möglichkeit", "возможность"),
    ("die Schwierigkeit", "трудность"),
    ("die Verantwortung", "ответственность"),
    ("die Gesellschaft", "общество"),
    ("die Regierung", "правительство"),
    ("die Bildung", "образование"),
    ("die Gesundheit", "здоровье"),
    ("die Umwelt", "окружающая среда"),
    ("die Arbeit", "работа"),
    ("der Beruf", "профессия"),
    ("die Karriere", "карьера"),
    ("das Unternehmen", "компания"),
    ("die Wirtschaft", "экономика"),
    ("der Markt", "рынок"),
    ("der Kunde", "клиент"),
    ("der Mitarbeiter", "сотрудник"),
    ("die Firma", "фирма"),
    ("das Produkt", "продукт"),
    ("die Lösung", "решение"),
    ("das Problem", "проблема"),
    ("die Situation", "ситуация"),
    ("die Meinung", "мнение"),
    ("die Information", "информация"),
    ("die Nachricht", "новость"),
    ("das Ergebnis", "результат"),
    ("die Forschung", "исследование"),
    ("die Technik", "техника"),
    ("die Technologie", "технология"),
    ("das System", "система"),
    ("die Idee", "идея"),
    ("die Frage", "вопрос"),
    ("die Antwort", "ответ"),
    ("die Sprache", "язык"),
    ("die Kultur", "культура"),
    ("die Geschichte", "история"),
    ("die Zukunft", "будущее"),
    ("die Vergangenheit", "прошлое"),
    ("die Gegenwart", "настоящее"),
    ("der Plan", "план"),
    ("das Ziel", "цель"),
    ("die Aufgabe", "задача"),
    ("der Erfolg", "успех"),
    ("der Fehler", "ошибка"),
    ("die Ursache", "причина"),
    ("die Wirkung", "влияние"),
    ("die Freiheit", "свобода"),
    ("die Sicherheit", "безопасность"),
    ("die Gefahr", "опасность"),
    ("der Krieg", "война"),
    ("der Frieden", "мир"),
    ("das Gesetz", "закон"),
    ("die Politik", "политика"),
    ("die Wahl", "выборы"),
    ("die Partei", "партия"),
    ("der Staat", "государство"),
    ("die Stadt", "город"),
    ("das Land", "страна"),
    ("das Dorf", "деревня"),
    ("die Straße", "улица"),
    ("der Weg", "путь"),
    ("das Gebäude", "здание"),
    ("die Wohnung", "квартира"),
    ("das Zimmer", "комната"),
    ("die Küche", "кухня"),
    ("das Badezimmer", "ванная"),
    ("das Bett", "кровать"),
    ("der Tisch", "стол"),
    ("der Stuhl", "стул"),
    ("das Fenster", "окно"),
    ("die Tür", "дверь"),
    ("das Auto", "машина"),
    ("der Zug", "поезд"),
    ("das Flugzeug", "самолёт"),
    ("das Fahrrad", "велосипед"),
    ("die Reise", "путешествие"),
    ("der Urlaub", "отпуск"),
    ("das Wetter", "погода"),
    ("der Regen", "дождь"),
    ("der Schnee", "снег"),
    ("die Sonne", "солнце"),
    ("der Wind", "ветер"),
    ("der Monat", "месяц"),
    ("das Jahr", "год"),
    ("die Woche", "неделя"),
    ("der Tag", "день"),
    ("die Stunde", "час"),
    ("die Minute", "минута"),
    ("die Sekunde", "секунда"),
    ("der Körper", "тело"),
    ("das Herz", "серце"),
    ("der Kopf", "голова"),
    ("die Hand", "рука"),
    ("das Auge", "глаз"),
    ("das Leben", "жизнь")
]

ADJECTIVES = [
    ("deutsch", "немецкий"),
    ("gut", "хороший"),
    ("real", "настоящий"),
    ("sick", "«крутой», «жёсткий», сленг"),
    ("tired", "уставший"),
    ("required", "требуемый"),
    ("alone", "одинокий"),
    ("filthy", "грязный"),
    ("German", "немецкий"),
    ("real good", "очень хороший"),
    ("no good", "плохой / нежелательный"),
]

CATEGORIES = {
    "Глаголы": VERBS,
    "Существительные": NOUNS,
    "Прилагательные": ADJECTIVES,
}

ACCENT = {
    "Глаголы": "#4f8ef7",
    "Существительные": "#a78bfa",
    "Прилагательные": "#34d399",
}


class FlashCard(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 300)
        self.flipped = False
        self.front_text = ""
        self.back_text = ""
        self.accent = "#4f8ef7"
        self.setStyleSheet(self._card_style())
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.badge = QLabel("DE")
        self.badge.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.badge.setFixedHeight(24)
        badge_font = QFont("Roboto", 10, QFont.Weight.Bold)
        self.badge.setFont(badge_font)
        layout.addWidget(self.badge, 0, Qt.AlignmentFlag.AlignHCenter)
        self.word_label = QLabel()
        self.word_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word_label.setWordWrap(True)
        word_font = QFont("Roboto", 28, QFont.Weight.Bold)
        self.word_label.setFont(word_font)
        layout.addWidget(self.word_label)
        self.hint_label = QLabel("нажмите, чтобы перевернуть")
        self.hint_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hint_font = QFont("Roboto", 10)
        self.hint_label.setFont(hint_font)
        layout.addWidget(self.hint_label)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def _card_style(self):
        return f"""
            QFrame {{
                background: #1e1e2e;
                border-radius: 20px;
                border: 2px solid {self.accent}44;
            }}
            QLabel {{
                color: #cdd6f4;
                background: transparent;
                border: none;
            }}
        """

    def set_accent(self, color):
        self.accent = color
        self.setStyleSheet(self._card_style())
        self.badge.setStyleSheet(f"color: {color}")
        self.hint_label.setStyleSheet("color: #585b70;")

    def load(self, front, back):
        self.front_text = front
        self.back_text = back
        self.flipped = False
        self.word_label.setText(front)
        self.badge.setText("DE")
        self.hint_label.setText("нажмите, чтобы перевернуть")
        self.hint_label.setStyleSheet("color: #585b70;")

    def mousePressEvent(self, event):
        self.flip()

    def flip(self):
        self.flipped = not self.flipped
        if self.flipped:
            self.word_label.setText(self.back_text)
            self.badge.setText("RU")
            self.hint_label.setText("перевёрнуто")
        else:
            self.word_label.setText(self.front_text)
            self.badge.setText("DE")
            self.hint_label.setText("нажмите, чтобы перевернуть")


class QuizWidget(QWidget):
    def __init__(self, data, accent):
        super().__init__()
        self.data = data
        self.accent = accent
        self.questions = []
        self.index = 0
        self.score = 0
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.setSpacing(30)
        self.word_label = QLabel()
        self.word_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word_label.setFont(QFont("Roboto", 28, QFont.Weight.Bold))
        self.word_label.setStyleSheet("color: #cdd6f4;")
        self.trans_label = QLabel()
        self.trans_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trans_label.setFont(QFont("Roboto", 20))
        self.trans_label.setStyleSheet("color: #a6adc8;")
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setFont(QFont("Roboto", 24, QFont.Weight.Bold))
        self.result_label.setStyleSheet(f"color: {self.accent};")
        self.result_label.hide()
        self.layout.addWidget(self.word_label)
        self.layout.addWidget(self.trans_label)
        self.layout.addWidget(self.result_label)
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(20)
        self.btn_true = QPushButton("Верно")
        self.btn_false = QPushButton("Неверно")
        self.btn_restart = QPushButton("Пройти заново")
        self.btn_restart.hide()
        btn_style = f"""
            QPushButton {{
                background: #1e1e2e;
                color: #cdd6f4;
                border: 2px solid {self.accent};
                border-radius: 10px;
                font-family: 'Roboto';
                font-size: 16px;
                padding: 15px 40px;
            }}
            QPushButton:hover {{
                background: {self.accent};
                color: #11111b;
            }}
        """
        self.btn_true.setStyleSheet(btn_style)
        self.btn_false.setStyleSheet(btn_style)
        self.btn_restart.setStyleSheet(btn_style)
        self.btn_true.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_false.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_restart.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_true.clicked.connect(lambda: self.check_answer(True))
        self.btn_false.clicked.connect(lambda: self.check_answer(False))
        self.btn_restart.clicked.connect(self.start_quiz)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_true)
        btn_layout.addWidget(self.btn_false)
        btn_layout.addStretch()
        self.layout.addLayout(btn_layout)
        self.layout.addWidget(
            self.btn_restart,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.start_quiz()

    def start_quiz(self):
        self.index = 0
        self.score = 0
        self.questions = []
        ru_options = [item[1] for item in self.data]
        for de, ru in self.data:
            if random.choice([True, False]):
                self.questions.append((de, ru, True))
            else:
                wrong_ru = random.choice([r for r in ru_options if r != ru])
                self.questions.append((de, wrong_ru, False))
        random.shuffle(self.questions)
        self.result_label.hide()
        self.btn_restart.hide()
        self.word_label.show()
        self.trans_label.show()
        self.btn_true.show()
        self.btn_false.show()
        self.show_question()

    def show_question(self):
        if self.index < len(self.questions):
            de, ru, _ = self.questions[self.index]
            self.word_label.setText(de)
            self.trans_label.setText(ru)
        else:
            self.show_results()

    def check_answer(self, user_answer):
        _, _, is_correct = self.questions[self.index]
        if user_answer == is_correct:
            self.score += 1
        self.index += 1
        self.show_question()

    def show_results(self):
        self.word_label.hide()
        self.trans_label.hide()
        self.btn_true.hide()
        self.btn_false.hide()
        self.result_label.setText(
            f"Результат: {self.score} из {len(self.questions)}"
        )
        self.result_label.show()
        self.btn_restart.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Deutschlet")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setMinimumSize(800, 600)
        self.setStyleSheet("background: #11111b;")
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane { border: none; }
            QTabBar::tab {
                background: #1e1e2e;
                color: #585b70;
                padding: 10px 20px;
                margin: 4px;
                border-radius: 6px;
                font-family: 'Roboto';
                font-size: 14px;
            }
            QTabBar::tab:selected {
                background: #313244;
                color: #cdd6f4;
            }
        """)
        self.setCentralWidget(self.tabs)
        self.init_flashcards_tab()
        self.tabs.addTab(self.flashcards_widget, "Карточки")
        self.tabs.addTab(
            QuizWidget(VERBS, ACCENT["Глаголы"]),
            "Тест: Глаголы"
        )
        self.tabs.addTab(
            QuizWidget(NOUNS, ACCENT["Существительные"]),
            "Тест: Существительные"
        )
        self.tabs.addTab(
            QuizWidget(ADJECTIVES, ACCENT["Прилагательные"]),
            "Тест: Прилагательные"
        )

    def init_flashcards_tab(self):
        self.current_category = "Глаголы"
        self.cards = []
        self.index = 0
        self.shuffled = False
        self.flashcards_widget = QWidget()
        main = QVBoxLayout(self.flashcards_widget)
        main.setContentsMargins(40, 30, 40, 30)
        main.setSpacing(20)
        title = QLabel("Deutschlet")
        title_font = QFont("Roboto", 20, QFont.Weight.Bold)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #cdd6f4;")
        main.addWidget(title)
        cat_row = QHBoxLayout()
        cat_row.setSpacing(10)
        self.cat_buttons = {}
        for name in CATEGORIES:
            btn = QPushButton(name)
            btn.setCheckable(True)
            btn.setFixedHeight(36)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda _, n=name: self.switch_category(n))
            cat_row.addWidget(btn)
            self.cat_buttons[name] = btn
        main.addLayout(cat_row)
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(6)
        self.progress_bar.setTextVisible(False)
        main.addWidget(self.progress_bar)
        self.counter_label = QLabel()
        self.counter_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        counter_font = QFont("Roboto", 11)
        self.counter_label.setFont(counter_font)
        self.counter_label.setStyleSheet("color: #585b70;")
        main.addWidget(self.counter_label)
        card_container = QHBoxLayout()
        card_container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.card = FlashCard()
        card_container.addWidget(self.card)
        main.addLayout(card_container)
        main.addStretch()
        nav_row = QHBoxLayout()
        nav_row.setSpacing(12)
        self.prev_btn = QPushButton("<- Назад")
        self.prev_btn.setFixedHeight(42)
        self.prev_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.prev_btn.clicked.connect(self.prev_card)
        self.flip_btn = QPushButton("Перевернуть")
        self.flip_btn.setFixedHeight(42)
        self.flip_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.flip_btn.clicked.connect(self.card.flip)
        self.next_btn = QPushButton("Вперёд ->")
        self.next_btn.setFixedHeight(42)
        self.next_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.next_btn.clicked.connect(self.next_card)
        nav_row.addWidget(self.prev_btn)
        nav_row.addWidget(self.flip_btn)
        nav_row.addWidget(self.next_btn)
        main.addLayout(nav_row)
        extra_row = QHBoxLayout()
        extra_row.setSpacing(12)
        self.shuffle_btn = QPushButton("Перемешать")
        self.shuffle_btn.setFixedHeight(36)
        self.shuffle_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.shuffle_btn.clicked.connect(self.toggle_shuffle)
        self.reset_btn = QPushButton("Сначала")
        self.reset_btn.setFixedHeight(36)
        self.reset_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.reset_btn.clicked.connect(self.reset)
        extra_row.addWidget(self.shuffle_btn)
        extra_row.addWidget(self.reset_btn)
        main.addLayout(extra_row)
        self.switch_category("Глаголы")

    def _apply_styles(self):
        accent = ACCENT[self.current_category]
        nav_btn_style = f"""
            QPushButton {{
                background: #1e1e2e;
                color: #cdd6f4;
                border: 1px solid #313244;
                border-radius: 10px;
                font-family: 'Roboto';
                font-size: 14px;
                padding: 0 16px;
            }}
            QPushButton:hover {{
                background: #313244;
                border-color: {accent};
                color: {accent};
            }}
            QPushButton:pressed {{
                background: #45475a;
            }}
        """
        flip_style = f"""
            QPushButton {{
                background: {accent};
                color: #11111b;
                border: none;
                border-radius: 10px;
                font-family: 'Roboto';
                font-size: 15px;
                font-weight: bold;
                padding: 0 20px;
            }}
            QPushButton:hover {{ background: {accent}cc; }}
            QPushButton:pressed {{ background: {accent}99; }}
        """
        small_btn_style = f"""
            QPushButton {{
                background: #181825;
                color: #585b70;
                border: 1px solid #313244;
                border-radius: 8px;
                font-family: 'Roboto';
                font-size: 12px;
                padding: 0 12px;
            }}
            QPushButton:hover {{
                color: {accent};
                border-color: {accent}88;
            }}
        """
        cat_style_active = f"""
            QPushButton {{
                background: {accent};
                color: #11111b;
                border: none;
                border-radius: 8px;
                font-family: 'Roboto';
                font-size: 13px;
                font-weight: bold;
                padding: 0 14px;
            }}
        """
        cat_style_inactive = f"""
            QPushButton {{
                background: #1e1e2e;
                color: #585b70;
                border: 1px solid #313244;
                border-radius: 8px;
                font-family: 'Roboto';
                font-size: 13px;
                padding: 0 14px;
            }}
            QPushButton:hover {{
                color: {accent};
                border-color: {accent}88;
            }}
        """
        self.prev_btn.setStyleSheet(nav_btn_style)
        self.next_btn.setStyleSheet(nav_btn_style)
        self.flip_btn.setStyleSheet(flip_style)
        self.shuffle_btn.setStyleSheet(small_btn_style)
        self.reset_btn.setStyleSheet(small_btn_style)
        for name, btn in self.cat_buttons.items():
            if name == self.current_category:
                btn.setStyleSheet(cat_style_active)
            else:
                btn.setStyleSheet(cat_style_inactive)
        pb_style = f"""
            QProgressBar {{
                background: #313244;
                border-radius: 3px;
                border: none;
            }}
            QProgressBar::chunk {{
                background: {accent};
                border-radius: 3px;
            }}
        """
        self.progress_bar.setStyleSheet(pb_style)
        self.card.set_accent(accent)

    def switch_category(self, name):
        self.current_category = name
        self.cards = list(CATEGORIES[name])
        self.index = 0
        self.shuffled = False
        self._apply_styles()
        self._show_current()

    def _show_current(self):
        total = len(self.cards)
        front, back = self.cards[self.index]
        self.card.load(front, back)
        self.counter_label.setText(f"{self.index + 1} / {total}")
        self.progress_bar.setMaximum(total)
        self.progress_bar.setValue(self.index + 1)

    def next_card(self):
        if self.index < len(self.cards) - 1:
            self.index += 1
            self._show_current()

    def prev_card(self):
        if self.index > 0:
            self.index -= 1
            self._show_current()

    def toggle_shuffle(self):
        self.shuffled = not self.shuffled
        if self.shuffled:
            random.shuffle(self.cards)
            self.shuffle_btn.setText("Перемешано")
        else:
            self.cards = list(CATEGORIES[self.current_category])
            self.shuffle_btn.setText("Перемешать")
        self.index = 0
        self._show_current()

    def reset(self):
        self.cards = list(CATEGORIES[self.current_category])
        self.shuffled = False
        self.shuffle_btn.setText("Перемешать")
        self.index = 0
        self._show_current()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
