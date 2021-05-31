import tkinter as tk
import json

# # Create a configuration file
# config = {
#     'frame1': True,
#     'frame2': True,
#     'frame3': True,
#     'hidden': {
#         'a': True,
#         'b': True
#     },
#     'apple': False}
#
# with open("config.json", "w") as f:
#     json.dump(config, f, indent=4, sort_keys=True)

with open('config.json') as f:
    settings = json.load(f)

gui = tk.Tk()
if settings['frame1']:
    frame1 = tk.Frame(gui)
    frame1.pack()

    label1 = tk.Label(frame1, text='Label in Frame1 is {}'.format(settings['frame1']))
    label1.pack()

if settings['frame2']:
    frame2 = tk.Frame(gui)
    frame2.pack()

    label2 = tk.Label(frame2, text='Label in Frame2 is {}'.format(settings['frame2']))
    label2.pack()

if settings['frame3']:
    frame3 = tk.Frame(gui)
    frame3.pack()

    label3 = tk.Label(frame3, text='Label in Frame3 is {}'.format(settings['frame3']))
    label3.pack()

if settings['hidden']['a']:
    label4 = tk.Label(text='Label in hidden a is {}'.format(settings['hidden']['a']))
    label4.pack()

if settings['hidden']['b']:
    label5 = tk.Label(text='Label in hidden b is {}'.format(settings['hidden']['b']))
    label5.pack()

gui.mainloop()

