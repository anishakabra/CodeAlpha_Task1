import tkinter as tk
import random

# --- Game Setup ---
words = ["apple", "banana", "grape", "mango", "peach"]
word = random.choice(words)
guessed_letters = set()
incorrect_guesses = 0
max_guesses = 6

# --- GUI Functions ---
def get_display_word():
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def make_guess():
    global incorrect_guesses

    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if not guess or len(guess) != 1 or not guess.isalpha():
        result_label.config(text="Enter a single letter.")
        return

    if guess in guessed_letters:
        result_label.config(text="Already guessed.")
    elif guess in word:
        guessed_letters.add(guess)
        result_label.config(text="Correct!")
    else:
        incorrect_guesses += 1
        guessed_letters.add(guess)
        result_label.config(text=f"Wrong! {max_guesses - incorrect_guesses} left.")
        draw_hangman(incorrect_guesses)

    update_display()

    if all(letter in guessed_letters for letter in word):
        result_label.config(text=f"You Win! The word was '{word}' 🎉")
        entry.config(state='disabled')
        guess_button.config(state='disabled')
    elif incorrect_guesses >= max_guesses:
        result_label.config(text=f"You Lose! The word was '{word}' 💀")
        entry.config(state='disabled')
        guess_button.config(state='disabled')

def update_display():
    word_label.config(text=get_display_word())
    guesses_label.config(text=f"Incorrect: {incorrect_guesses} / {max_guesses}")

# --- Drawing Hangman ---
def draw_hangman(stage):
    if stage == 1:  # Head
        canvas.create_oval(70, 50, 110, 90, width=2)
    elif stage == 2:  # Body
        canvas.create_line(90, 90, 90, 150, width=2)
    elif stage == 3:  # Left arm
        canvas.create_line(90, 100, 60, 130, width=2)
    elif stage == 4:  # Right arm
        canvas.create_line(90, 100, 120, 130, width=2)
    elif stage == 5:  # Left leg
        canvas.create_line(90, 150, 60, 190, width=2)
    elif stage == 6:  # Right leg
        canvas.create_line(90, 150, 120, 190, width=2)

# --- GUI Layout ---
root = tk.Tk()
root.title("Hangman Game with Drawing")
root.geometry("500x400")

word_label = tk.Label(root, text=get_display_word(), font=("Helvetica", 24))
word_label.pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack()

guess_button = tk.Button(root, text="Guess", command=make_guess)
guess_button.pack(pady=10)

guesses_label = tk.Label(root, text=f"Incorrect: 0 / {max_guesses}", font=("Helvetica", 12))
guesses_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="blue")
result_label.pack(pady=10)

# --- Hangman Drawing Canvas ---
canvas = tk.Canvas(root, width=200, height=250, bg="white")
canvas.pack(pady=10)

# Hangman base and gallows
canvas.create_line(20, 230, 180, 230, width=2)  # Base
canvas.create_line(50, 230, 50, 30, width=2)    # Vertical post
canvas.create_line(50, 30, 90, 30, width=2)     # Top bar
canvas.create_line(90, 30, 90, 50, width=2)     # Rope

root.mainloop()
