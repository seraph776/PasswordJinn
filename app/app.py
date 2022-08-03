#!/usr/bin/env python3
"""
created: 2022-07-29 12:32:10
@author: seraph★776
contact: seraph776@gmail.com
project: Password JINN
license: MIT
metadoc: A strong random password generator. The password will always have all unique characters!
"""

import tkinter
import pyperclip
import secrets
import random
import string

# Initialize window ----------------------------------------------------------------------------------------------------
root = tkinter.Tk()
root.geometry("300x400")
root.resizable(None, None)
root.title("PASSWORD GENERATOR")

# Application logo (top left)
logo = tkinter.PhotoImage(file="../assets/logo.png")

# Application logo displayed on app
image = tkinter.PhotoImage(file="../assets/logo_dark.png")
root.iconphoto(True, logo)
root.config(background="#282c34")

# Labels -----------------------------------------------------------------------------------------------------
tkinter.Label(root, text=f'PASSWORD JINN الجن {chr(169)}',
              font=('ariel', 15, 'bold'),
              background="#282c34",
              fg="#fff",
              padx=5,
              pady=15,
              image=image,
              compound='bottom').pack()

# Sub-title page
tkinter.Label(root,
              background="#282c34",
              fg="#fff",
              text=f'{chr(128273)} Strong Random Password Generator {chr(128274)}').pack()

# Footer Credits:
tkinter.Label(root, text=f'\nDesign by ~ Seraph {chr(22825)}',
              font=('ariel', 8, 'normal'),
              padx=5,
              pady=10,
              background="#282c34",
              fg="#fff").pack(side=tkinter.BOTTOM)

# select password length:
tkinter.Label(root, text='Select Password Length (8-32):',
              font=('ariel', 12, 'normal'),
              background="#282c34",
              fg="#fff",
              padx=5,
              pady=10,
              ).pack()

pass_len = tkinter.IntVar()
pass_str = tkinter.StringVar()

tkinter.Spinbox(root, from_=8, to=32,
                textvariable=pass_len,
                width=8).pack(pady=10)


# Define functions -----------------------------------------------------------------------------------------------------
def shuffle_string(s: str) -> str:
    """This function shuffle a string 10 times."""
    s = list(s)
    random.shuffle(s)
    return ''.join(s)


def generate_password():
    """This function generates the password!"""

    password = ''

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    symbols = string.punctuation
    numbers = string.digits

    # Get 1 sample from each character set (4 total characters), and remove the
    # Sample from the pool to ensure no repeats.
    sample_lowercase = secrets.choice(lowercase)
    password += sample_lowercase
    lowercase = lowercase.replace(sample_lowercase, '')
    uppercase = uppercase.replace(sample_lowercase.upper(), '')

    sample_uppercase = secrets.choice(uppercase)
    password += sample_uppercase
    uppercase = uppercase.replace(sample_uppercase, '')
    lowercase = lowercase.replace(sample_uppercase.lower(), '')

    sample_punctuation = secrets.choice(symbols)
    password += sample_punctuation
    symbols = symbols.replace(sample_punctuation, '')

    sample_digits = secrets.choice(numbers)
    password += sample_digits
    numbers = numbers.replace(sample_digits, '')

    # This represents the new sample_character_set, with the samples collected for the password removed.
    sample_character_set: str = shuffle_string(''.join([lowercase + uppercase + symbols + numbers]))

    while True:
        if len(password) == pass_len.get():
            break

        sample_char = secrets.choice(sample_character_set)
        password += sample_char
        if sample_char.isalpha():
            sample_character_set = sample_character_set.replace(sample_char.lower(), '').replace(
                sample_char.upper(), '')
        else:
            sample_character_set = sample_character_set.replace(sample_char, '')

    pass_str.set(password)


def Copy_password():
    pyperclip.copy(pass_str.get())


def temp_text(e):
    textbox.delete(0, "end")


# Buttons --------------------------------------------------------------------------------------------------------------
tkinter.Button(root, text="GENERATE PASSWORD", padx=10, pady=10, width=24,
               command=generate_password).pack(padx=10, pady=5)

textbox = tkinter.Entry(root, textvariable=pass_str, width=32, fg="#4169E1")
textbox.insert(0, "Select Generate Password Button...")
textbox.pack(padx=10, pady=5)
textbox.bind("<FocusIn>", temp_text)
tkinter.Button(root, text='COPY TO CLIPBOARD', padx=10, pady=10, width=24,
               command=Copy_password).pack(padx=15, pady=5)

# Loop to run program
root.mainloop()
