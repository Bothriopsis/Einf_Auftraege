import heapq
import sys
import tkinter as tk
import tkinter.messagebox as mbox

root = tk.Tk()
root.geometry('700x350')
root.title('Shop Game')
root.resizable(False, True)


def starting_price(main_ar, sec_arr):
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
    return sub_summ

def main():
    try:
        t = int(text.get('1.0', '1.end'))
        z = 2
        global text1
        text1.destroy()
        for x in range(t):
            arr = []

            n, k = list(map(int, text.get(f'{z}.0', f'{z}.end').strip().split()))
            z += 1
            a = list(map(int, text.get(f'{z}.0', f'{z}.end').strip().split()))
            z += 1
            b = list(map(int, text.get(f'{z}.0', f'{z}.end').strip().split()))
            z += 1
            print(a)
            print(b)
            a = [-x for x in a]
            k_arr = []
            temp_pop = []
            max_value = 0
            sub_sum = 0
            my_bool = False

            for i in range(n):
                arr.append([a[i], b[i]])
            arr.sort(key=lambda y: y[1], reverse=False)

            for k_range in range(1, k + 1):
                if arr:
                    heapq.heappush(k_arr, arr[-1])
                    arr.pop()
            if arr:
                sub_sum = starting_price(arr, k_arr)
            if sub_sum > max_value:
                max_value = sub_sum
            while arr:
                if arr:
                    if arr[-1][1] + arr[-1][0] >= 0:
                        sub_sum -= arr[-1][1]
                    else:
                        sub_sum += arr[-1][0]
                    temp_pop = heapq.heappushpop(k_arr, arr[-1])
                    arr.pop()
                    if temp_pop:
                        sub_sum -= temp_pop[0]
            if sub_sum > max_value:
                max_value = sub_sum
            text1 = tk.Label(text=max_value, font=('Helvetica', 10, 'bold'))
            text1.pack()
    except:
        mbox.showerror(title='Error', message='Ein Fehler ist aufgetreten')


title = tk.Label(text='Shop Game',font=('Helvetica', 20,'bold'))
title.pack()
anweisung = tk.Label(text='Input Specs:',font=('Helvetica', 10))
anweisung.pack()


text = tk.Text(root, width=80, height=7,wrap='none')
text.pack()
S = tk.Scrollbar(root,command=text.xview,orient=tk.HORIZONTAL)
S.pack(fill=tk.X)
text.config(xscrollcommand=S.set)
button1 = tk.Button(root, text="Run", command=main)
button1.pack(ipadx=150,pady=20)
ausgabe = tk.Label(text='The max profit is:',font=('Helvetica', 10))
ausgabe.pack()
text1 = tk.Label()

root.mainloop()