"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues,  Bilbo, and Hussein Alawami.  Summer 2016.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
#     root = tkinter.Tk()
#     root.mainloop()
#
#     print("Bye.")

    # ------------------------------------------------------------------
    # done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------

#     root1 = tkinter.Tk()
#
#     frame = ttk.Frame(root1, padding=22)
#     frame.grid()
#
#     button = ttk.Button(frame, text='Heyo')
#     button.grid()
#     root1.mainloop()


    # ------------------------------------------------------------------
    # done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------

#     root2 = tkinter.Tk()
#     frame2 = ttk.Frame(root2, padding=1)
#     frame2.grid()
#
#     button = ttk.Button(root2, text='hy')
#     button.grid()
#
#     root2.mainloop()

    # ------------------------------------------------------------------
    # done: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------

#     root3 = tkinter.Tk()
#     frame3 = ttk.Frame(root3, padding=50)
#     frame3.grid()
#
#     button3 = ttk.Button(frame3, text='Hello 5x')
#     button3['command'] = (lambda: helloo())
#     button3.grid()
#     root3.mainloop()
#
# def helloo():
#     for _ in range(5):
#         print("Hello")

    # ------------------------------------------------------------------
    # done: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #       on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------

#     root4 = tkinter.Tk()
#     frame4 = ttk.Frame(root4, padding=30)
#     frame4.grid()
#
#     entry = ttk.Entry(frame4)
#     entry.grid()
#     button123 = ttk.Button(root4, text='Enter something')
#     button123['command'] = (lambda: printt(entry))
#     button123.grid()
#     button4 = ttk.Button(root4, text='qwerty')
#     button4['command'] = (lambda: funct(entry))
#     button4.grid()
#     root4.mainloop()
#
# def printt(stuff):
#     something = stuff.get()
#     print(something)
# def funct(entryBox):
#     contents = entryBox.get()
#     if contents == 'ok':
#         print('Hello')
#     else:
#         print ("Goodbye")



    # ------------------------------------------------------------------
    # done: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    root5 = tkinter.Tk()
    frame5 = ttk.Frame(root5, padding=10)
    frame5.grid()

    frame6 = ttk.Frame(root5, padding=20)
    frame6.grid()

    entry2 = ttk.Entry(frame5)
    entry2.grid()

    entry3 = ttk.Entry(frame6)
    entry3.grid()
    button123 = ttk.Button(root5, text='Enter something')
    button123['command'] = (lambda: printt(entry2))
    button123.grid()
    button5 = ttk.Button(root5, text="Something")
    button5['command'] = (lambda: funct(entry2))
    button5.grid()
    button6 = ttk.Button(root5, text='something else')
    button6['command'] = (lambda: function(entry2, entry3))
    button6.grid()
    root5.mainloop()

def printt(stuff):
    something = stuff.get()
    print(something)
def funct(entryBox):
    contents = entryBox.get()
    if contents == 'ok':
        print('Hello')
    else:
        print ("Goodbye")
def function(word, number):
    n = number.get()
    w = int(n)
    for k in range (w):
        print(word.get())

    # ------------------------------------------------------------------
    # done: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
