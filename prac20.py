import tkinter as tk
from tkinter import messagebox

# クイズのデータ
questions = [
    {
        "question": "新型コロナウイルスが流行したのはいつ？",
        "choices": ["2018年", "2019年", "2020年", "2021年"],
        "answer": "2020年"
    },
    {
        "question": "atomicの意味はなに？",
        "choices": ["核", "原子", "アトミック", "不可分の"],
        "answer": "原子"
    },
    {
        "question": "日本の人気な都道府県は?",
        "choices": ["東京", "愛知県", "大阪", "北海道"],
        "answer": "北海道"
    },
    {
        "question": "世界にはいくつの国があるでしょうか？",
        "choices": ["153個", "185個", "196個", "205個"],
        "answer": "196個"
    },
  
    {
        "question": "第一次世界大戦が始まった年と月日はなに？",
        "choices": ["1914年7月28日", "1920年6月18日", "1910年8月7日","1915年9月1日"],
        "answer": "1914年7月28日"
    }
    ,{
        "question": "光彦の名字は？",
        "choices": ["鈴木", "高橋", "円谷", "田中"],
        "answer": "円谷"
    }
    ,{
        "question": "powerの意味は？",
        "choices": ["強い", "力", "筋肉", ""],
        "answer": "北海道"
    }
    ,{
        "question": "日本の人気な都道府県は?",
        "choices": ["東京", "愛知県", "大阪", "北海道"],
        "answer": "北海道"
    }
    ,{
        "question": "日本の人気な都道府県は?",
        "choices": ["東京", "愛知県", "大阪", "北海道"],
        "answer": "北海道"
    }
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=400, justify="center", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.var = tk.StringVar(value="-1")
        self.choices_frame = tk.Frame(root)
        self.choices_frame.pack(pady=20)

        self.choices_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.choices_frame, text="", variable=self.var, value=f"{i}", font=("Arial", 14))
            rb.pack(anchor="w", padx=20, pady=5)
            self.choices_buttons.append(rb)
            
        
        

        self.submit_button = tk.Button(root, text="Submit Answer", command=self.submit_answer, font=("Arial", 14))
        self.submit_button.pack(pady=20)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 14))
        self.feedback_label.pack(pady=20)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question, font=("Arial", 14))
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self): # 1
        question_data = questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        self.var.set(None)

        for idx, choice in enumerate(question_data["choices"]):
            self.choices_buttons[idx].config(text=choice, value=choice)

    def submit_answer(self):
        selected_answer = self.var.get()
        if not selected_answer:
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        question_data = questions[self.current_question]
        if selected_answer == question_data["answer"]:
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Wrong! The correct answer is {question_data['answer']}", fg="red")

        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(questions):
            self.show_question()
            self.feedback_label.config(text="")
            self.submit_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Quiz Complete", f"You completed the quiz! Your score: {self.score}/{len(questions)}")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk() # rootというwindowを作成した。
    quiz_game = QuizGame(root)
    root.mainloop()