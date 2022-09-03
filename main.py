import tkinter
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
my_dict = data.to_dict(orient="records")
random_dictionary = {}

def next_item():
    global random_dictionary, finish
    window.after_cancel(finish)
    random_dictionary = random.choice(my_dict)
    word = random_dictionary["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=word, fill="black")
    canvas.itemconfig(image_container, image=front_img)
    finish = window.after(3000, func=flip_card)


def flip_card():
    new_word = random_dictionary["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=new_word, fill="white")
    canvas.itemconfig(image_container, image=back_img)


def is_known():
    my_dict.remove(random_dictionary)
    print(len(my_dict))
    new_data = pandas.DataFrame(my_dict)
    next_item()


window = tkinter.Tk()
window.title("Flashy App")



finish = window.after(3000, func=flip_card)

window.resizable(False, False)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_img = tkinter.PhotoImage(file="images/card_back.png")
front_img = tkinter.PhotoImage(file="images/card_front.png")
image_container = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="TITLE", font=("Arial", 40, "italic"))
card_text = canvas.create_text(400, 263, text="WORD", font=("Arial", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Buttons
red_img = tkinter.PhotoImage(file="images/wrong.png")
red_button = tkinter.Button(image=red_img, command=next_item)
red_button.grid(column=0, row=1)

green_img = tkinter.PhotoImage(file="images/right.png")
green_button = tkinter.Button(image=green_img, command=is_known)
green_button.grid(column=1, row=1)
next_item()


window.mainloop()

