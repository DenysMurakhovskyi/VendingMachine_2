from window_app import Fullscreen_Window
import threading
from rpi_com import detect_press

if __name__ == '__main__':
	w = Fullscreen_Window()
	t = threading.Thread(target=detect_press, args=(1, w))
	t.setDaemon(daemonic=True)
	t.start()
	w.tk.mainloop()
