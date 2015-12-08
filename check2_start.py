''' @Author: Lucien Brule, Sibel Adali(?)
    @Descr: Tribal T shirt generator
'''

from Tkinter import *


class MyApp(object):

    def __init__(self, parent):
        self.width = 600
        self.height = 600
        self.parent = parent
        self.main_frame = Frame(parent)
        self.main_frame.pack()
        self.canvas_frame = Frame(self.main_frame)
        self.canvas_frame.pack(side=TOP)
        self.canvas = Canvas(self.main_frame,
                             width=self.width, height=self.height,background = 'black')
        self.canvas.pack()

        self.button_frame = Frame(self.main_frame)
        self.button_frame.pack(side=BOTTOM)
        self.drawbutton = Button(self.button_frame, text="Draw",
                                 command=self.draw)
        self.drawbutton.pack(side=LEFT)
        self.clearbutton = Button(self.button_frame, text="Clear",
                                  command=self.clear)
        self.clearbutton.pack(side=LEFT)
        self.quitbutton = Button(self.button_frame, text="Quit",
                                 command=self.quit)
        self.quitbutton.pack(side=RIGHT)

    def clear(self):
        self.canvas.delete("all")

    def quit(self):
        self.parent.destroy()

    def draw(self):
        self.draw_lines(self.width / 2, self.height / 2,
                        min(self.width, self.height) / 4)

    # Modify this function to call itself recursively to draw smaller
    # plus signs at the four end points of the current plus sign.
    # You must have a stopping condition to make sure that the
    # recursion ends!
    def draw_lines(self, centerx, centery, length):
        if length < 4:
            return
        if length < 10:
            length += 1
        xsh = 0
        ysh = 0
        xsh += 0
        ysh += 0
        length = 3*length/5
        c1 = (((centerx - length) * (255 - 100)) / (600 + 50 - 50)) + 100
        c2 = (((centery + length) * (255 - 100)) / (600 + 50 - 50)) + 100
        c3 = ((((centerx + centery) - 600) * (255 - 100)) / (600 - -600)) + 100
        c1 , c2 ,c3 = map(abs,(c1,c2,c3))
        print c1, c2, c3
        self.canvas.configure(background='#%02x%02x%02x' % ((255-c1)/2, (255-c2)/2, (255-c3)/2))

        self.canvas.create_line(centerx + xsh, centery + length,
                                centerx - xsh, centery - length, fill='#%02x%02x%02x' % (c1, c2, c3))
        self.canvas.create_line(centerx + length, centery + ysh,
                                centerx - length, centery - ysh, fill='#%02x%02x%02x' % (c1, c2, c3))
        self.canvas.update()
        # self.canvas.after(1)

        self.draw_lines(centerx + length, centery, length / 2)
        self.draw_lines(centerx, centery - length, length / 2)
        self.draw_lines(centerx - length, centery, length / 2)
        self.draw_lines(centerx, centery + length, length / 2)


# The main code simply creates a canvas and three buttons.
if __name__ == "__main__":
    root = Tk()
    root.title("Recursion Example: Lab 12 Checkpoint 2")
    myapp = MyApp(root)
    root.mainloop()
