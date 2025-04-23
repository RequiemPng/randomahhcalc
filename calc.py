import tkinter
from tkinter.constants import *

firstNumber = ""
secondNumber = ""
operator = ""
thirdNumber = ""
operator2 = ""

def makequestion():
    entry_text.set(firstNumber + operator + secondNumber + operator2 + thirdNumber)

def clear_all():
    global firstNumber, secondNumber, thirdNumber, operator, operator2
    firstNumber = ""
    secondNumber = ""
    thirdNumber = ""
    operator = ""
    operator2 = ""
    makequestion()

root = tkinter.Tk()
root.title("Calculator")

frame = tkinter.Frame(root, relief=RIDGE, borderwidth=7)
frame.pack(fill=BOTH, expand=1)

output_text = tkinter.StringVar()
entry_text = tkinter.StringVar()
input_field = tkinter.Entry(frame, textvariable=entry_text, state="disabled", font=("Arial", 16))
input_field.grid(row=0, column=0, columnspan=4)
output_field = tkinter.Entry(frame, textvariable=output_text, state="disabled", font=("Arial", 16))
output_field.grid(row=1, column=0, columnspan=4)

def on_button_click(number):
    global firstNumber, secondNumber, thirdNumber

    if operator == "":
        firstNumber += str(number)
    elif operator2 == "":
        secondNumber += str(number)
    else:
        thirdNumber += str(number)

    makequestion()

for i in range(1, 10):
    row, col = divmod(i - 1, 3)
    button = tkinter.Button(frame, text=str(i), width=5, height=2, font=("Arial", 14),
                            command=lambda num=i: on_button_click(num))
    button.grid(row=row + 2, column=col)

button0 = tkinter.Button(frame, text="0", width=5, height=2, font=("Arial", 14),
                         command=lambda: on_button_click(0))
button0.grid(row=5, column=1)

def on_operator_click(op):
    global operator, operator2

    if operator == "":
        operator = op
    else:
        operator2 = op

    makequestion()

operator_symbols = ["+", "-", "×", "÷"]
for index, symbol in enumerate(operator_symbols):
    button = tkinter.Button(frame, text=symbol, width=5, height=2, font=("Arial", 14),
                            command=lambda op=symbol: on_operator_click(op))
    button.grid(row=index + 2, column=3)

buttonclr = tkinter.Button(frame, text="CLR", width=5, height=2, font=("Arial", 14), command=clear_all)
buttonclr.grid(row=5, column=0)

def equals():
    global firstNumber, secondNumber, thirdNumber, operator, operator2

    try:
        if thirdNumber:
            num1 = float(firstNumber)
            num2 = float(secondNumber)
            num3 = float(thirdNumber)

            if operator == "×":
                result = num1 * num2 * num3
            elif operator == "+":
                result = num1 + num2 + num3
            elif operator == "-":
                result = num1 - num2 - num3
            elif operator == "÷":
                if num2 == 0 or num3 == 0:
                    result = "Error"
                else:
                    result = num1 / num2 / num3

        elif secondNumber:
            num1 = float(firstNumber)
            num2 = float(secondNumber)

            if operator == "×":
                result = num1 * num2
            elif operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "÷":
                if num2 == 0:
                    result = "Error"
                else:
                    result = num1 / num2
        else:
            result = "Error"

        output_text.set(result)  
        clear_all()  

    except ValueError:
        output_text.set("Error")

buttonequal = tkinter.Button(frame, text="=", width=5, height=2, font=("Arial", 14), command=equals)
buttonequal.grid(row=5, column=2)

root.mainloop()
