from tkinter import *
import pandas as pd
import random, time
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- Random Word, CSV Data ------------------------------- #

try:
    data = pd.read_csv("data/french_words.csv")
    df = data.to_dict(orient="records")
except FileNotFoundError:
    print("The file was not found.")
    df = []
except pd.errors.EmptyDataError:
    print("The file is empty.")
    df = []
def random_words():

    #Getting both an English and a French word
    random_word = random.choice(df)
    random_french_word = random_word["French"]
    random_english_word = random_word["English"]

    #Showing French Word
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=random_french_word)

    # Flip the card after 3 seconds
    window.after(3000, flip_card, random_english_word)

    # For Testing
    print(f"{random_french_word} -- {random_english_word}")

def flip_card(random_english_word):
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=random_english_word)

# ---------------------------- Button Functionality ------------------------------- #
def right():
    random_word = random.choice(df)
    df.remove(random_word)
    random_words()

def wrong():
    random_words()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Creating the canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

title_text = canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400,263, text="Word", font=("Ariel", 60, "bold"))

#Creating the "X" button
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(command = wrong, bg=BACKGROUND_COLOR, highlightthickness=0, image=wrong_button_image)
wrong_button.grid(column=0, row=1)

#Creating the Checkmark button
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(command = right, bg=BACKGROUND_COLOR, highlightthickness=0, image=right_button_image)
right_button.grid(column=1, row=1)


window.mainloop()