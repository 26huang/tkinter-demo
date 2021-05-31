import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar, Button
import threading
import time

demo = tk.Tk()


def start_thread():
    start['state'] = 'disabled'
    pb.start()
    thread = threading.Thread(target=test, args=(5,))
    thread.start()
    monitor(thread)


# def stop_process():
#     pb.stop()
#     pb_var.set(0)
#     label['text'] = 'Stopped'


def test(num=5):
    time.sleep(num)


def monitor(thread, count=0):
    """ Monitor the download thread """
    if thread.is_alive():
        count += 1
        print('alive ', count)
        label['text'] = '{} seconds'.format(count)
        demo.after(1000, lambda: monitor(thread, count))
    else:
        print('finished')
        label['text'] = 'Completed in {} seconds'.format(count)
        pb_var.set(0)
        pb.stop()
        start['state'] = 'normal'


pb_var = tk.StringVar()

# progressbar
pb = Progressbar(demo, orient='horizontal', maximum=10, variable=pb_var, mode='determinate')
pb.pack(fill=tk.BOTH)

# progress status
label = ttk.Label(text='0 seconds')
label.pack(fill=tk.BOTH)

# buttons
start = Button(demo, text='Start', command=lambda: start_thread())
start.pack(fill=tk.BOTH)
# stop = Button(ws, text='Stop', command=stop_process)
# stop.pack(fill=tk.BOTH)

demo.mainloop()