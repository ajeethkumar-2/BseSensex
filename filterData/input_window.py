import tkinter as tk
from calendar import monthrange
import pandas as pd


def all_days(y, m):
    return ['{:04d}-{:02d}-{:02d}'.format(y, m, d) for d in range(1, monthrange(y, m)[1] + 1)]


def filtering_data():
    x1 = entry1.get()
    response_label = tk.Label(root, text='The selected Month is:', font=('helvetica', 10))
    canvas1.create_window(200, 265, window=response_label)
    answer_label = tk.Label(root, text=x1, font=('helvetica', 10))
    canvas1.create_window(200, 240, window=answer_label)
    feedback_label = tk.Label(root, text='The Data of the selected month is saved.', font=('helvetica', 10))
    canvas1.create_window(200, 265, window=feedback_label)
    days = all_days(2020, int(x1))
    data = pd.read_excel("bse_data.xlsx", sheet_name='YTD')
    filtered_data = data.loc[(data['Date'] >= days[0]) & (data['Date'] <= days[-1])]
    feed_data = pd.DataFrame(filtered_data)
    feed_data.to_excel('bse_data_filter.xlsx', sheet_name='month')


root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

heading_label = tk.Label(root, text='Filtering the data of a Month')
heading_label.config(font=('helvetica', 14))

note_label = tk.Label(root, text='Note: Enter the months as show below:')
note_label.config(font=('helvetica', 12))
canvas1.create_window(200, 115, window=note_label)

example_label = tk.Label(root, text="'If June enter as 6'")
example_label.config(font=('helvetica', 9))
canvas1.create_window(200, 140, window=example_label)

entry1 = tk.Entry(root)
canvas1.create_window(200, 45, window=heading_label)
canvas1.create_window(200, 170, window=entry1)

button1 = tk.Button(text='enter', command=filtering_data, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 200, window=button1)