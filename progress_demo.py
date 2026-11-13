"""A tiny ttk.Progressbar tour — runs in cleanroom's virtual tkinter and on a
real PC (python progress_demo.py).

Three bars, one behavior each:
1. stepped by hand — step() wraps at maximum and keeps cycling (the rule
   measured against real Tk 9.0, not folklore);
2. driven by start(120) — the widget schedules its own step() timer, stop()
   cancels it;
3. indeterminate — the value climbs, the bar just bounces while running.
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("progressbar demo")
root.geometry("430x300")

# 1 — determinate, stepped by hand
manual = ttk.Progressbar(root, orient="horizontal", length=320,
                         mode="determinate", maximum=10)
manual.pack(padx=14, pady=(10, 2))
manual_label = tk.Label(root, text="manual step: 0 / 10 — wraps and cycles")
manual_label.pack()


def bump():
    manual.step()
    manual_label.config(text="manual step: " +
                        str(int(float(manual["value"]))) + " / 10 — wraps and cycles")


tk.Button(root, text="step +1", command=bump).pack(pady=(2, 8))

# 2 — determinate, driven by start(): the widget steps itself until stop()
auto = ttk.Progressbar(root, orient="horizontal", length=320,
                       mode="determinate", maximum=40)
auto.pack(padx=14, pady=2)
auto_label = tk.Label(root, text="auto: 0 / 40")
auto_state = {"on": False}


def tick():
    if auto_state["on"]:
        auto_label.config(text="auto: " + str(int(float(auto["value"]))) + " / 40")
        root.after(200, tick)


def toggle_auto():
    if auto_state["on"]:
        auto.stop()
        auto_state["on"] = False
        auto_button.config(text="start() the auto bar")
    else:
        auto.start(120)
        auto_state["on"] = True
        auto_button.config(text="stop() the auto bar")
        root.after(200, tick)


auto_button = tk.Button(root, text="start() the auto bar", command=toggle_auto)
auto_button.pack(pady=2)
auto_label.pack()

# 3 — indeterminate: bounce while running
indet = ttk.Progressbar(root, orient="horizontal", length=320,
                        mode="indeterminate", maximum=30)
indet.pack(padx=14, pady=(8, 2))
indet_state = {"on": False}


def toggle_indet():
    if indet_state["on"]:
        indet.stop()
        indet_state["on"] = False
        indet_button.config(text="start() the indeterminate bar")
    else:
        indet.start()
        indet_state["on"] = True
        indet_button.config(text="stop() the indeterminate bar")


indet_button = tk.Button(root, text="start() the indeterminate bar",
                         command=toggle_indet)
indet_button.pack(pady=2)
tk.Label(root, text="indeterminate: the value climbs; the bar just bounces").pack()

root.mainloop()
