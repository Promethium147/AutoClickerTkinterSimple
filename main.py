from ttkbootstrap import Style, Button, Entry, Window
from time import sleep, time
from pynput.mouse import Button as Btn, Controller

# Set to True to display the Mouse Position button
# Click it to display the mouse position in the terminal for 10 seconds
# So you can fit the clicker to your needs

MOUSE_POSITION = False

DELAY = 20

GREEN_BUTTON_TEXT = "Go"
GREEN_BUTTON_STANDARD_TIME = 15

RED_BUTTON_TEXT = "80s"
RED_BUTTON_STANDARD_TIME = 80

root = Window(themename='darkly')
root.title('AutoClicker')

# Smaller window if we don't show the mouse position button
if MOUSE_POSITION:
    root.geometry('360x50')
else:
    root.geometry('220x50')

# Keep the window always on top of all other windows
root.wm_attributes("-topmost", 1)

mouse = Controller()


def auto_click(sec):
    """Click the mouse for the seconds entered in the input field (Use the green button),
    or the amount of seconds passed as an argument (green and red button)."""

    mouse.position = (300, 400)

    try:
        seconds = int(seconds_entry.get())
    except ValueError:
        seconds = sec

    end_time = time() + seconds

    def click():
        while time() < end_time:
            mouse.click(Btn.left)
            root.after(DELAY, click)
            return
    click()


def get_mouse_position():
    """Display the mouse position in the terminal for 10 seconds."""
    for i in range(50):
        print(mouse.position)
        sleep(0.2)


seconds_entry = Entry(root, width=10)
seconds_entry.grid(column=0, row=0, padx=10, pady=10)

go_button = Button(text=GREEN_BUTTON_TEXT,
                   command=lambda: auto_click(GREEN_BUTTON_STANDARD_TIME), bootstyle=('success', 'outline'))
go_button.grid(column=1, row=0, padx=10, pady=10)

long_go_button = Button(text=RED_BUTTON_TEXT,
                        command=lambda: auto_click(RED_BUTTON_STANDARD_TIME), bootstyle=('danger', 'outline'))
long_go_button.grid(column=2, row=0, padx=10, pady=10)


if MOUSE_POSITION:
    get_mouse_position_button = Button(text="Mouse Position", command=get_mouse_position, bootstyle=('primary', 'outline'))
    get_mouse_position_button.grid(column=3, row=0, padx=10, pady=10)

root.mainloop()

# Note to "Unexpected Argument" warning for bootstyle in PyCharm. See:
# https://stackoverflow.com/questions/77681696/unexpected-argument-in-pycharm-for-the-ttkbootstrap-bootstyle-argument
# So you can completely ignore that warning or "fix" it.
# I've chosen to ignore it.
