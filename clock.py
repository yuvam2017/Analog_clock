from tkinter import *
import os
import shutil
from datetime import *
import time
from math import *
from PIL import ImageTk,Image,ImageDraw
os.chdir('/home/tony/projects/Kali_mess')
class Clock:
    def __init__(self,root):
        self.root = root
        self.root.title("GUI Ananlog Clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        self.title  = Label(self.root,text="Welcome Analog Clock",fg="white",font='tallytextbold 50 bold',bg="#04444a")
        self.title.place(x=0,y=50,relwidth=1)
        self.lbl = Label(self.root,bg="white",bd=20,relief=RAISED)
        self.lbl.place(x=450,y=150,height=400,width=400)
        # self.clock_image()
        self.working()


    def clock_image(self,hr,min_,sec):
        clock = Image.new("RGB",(400,400),(255,255,255))
        draw = ImageDraw.Draw(clock)
        #======For Clock image
        
        os.mkdir("Images")
        shutil.move("clnh5.jpg","Images/clnh5.jpg")
        shutil.move("cl14.jpg","Images/cl4.jpg")
        shutil.move("cl13.jpg","Images/vl13.jpg")
        shutil.move("cl20.gif","Images/cl20.gif")
        shutil.move("clm20.gif","Images/clm20.gif")
        shutil.move("clm65.png","Images/clm65.png")
        
        path = "Images/clnh5.jpg"
        bg=Image.open(f"{path}")
        bg = bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))

        # # Formula to rotate the Clock
        # angle_in_radians = angle_in_degrees * math.pi / 100
        # line_length=100
        # center_x = 250
        # center_y = 250
        # end_x = center_x + line_length * math.cos(angle_in_radians)
        # end_y = center_y + line_length * math.sin(angle_in_radians)

        origin = 200,200
        #====Hour Line Image
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
        
        #====Minutes Line Image
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)
        
        #====seconds Line Image
        draw.line((origin,200+100*sin(radians(sec)),200-100*cos(radians(sec))),fill="red",width=4)
        draw.ellipse((190,190,210,210),fill='#13004f')
        clock.save("clock_new.png")
    
    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second
        hr=(h/12)*360
        min_ = (m/60)*360
        sec = (s/60)*360
        self.clock_image(hr,min_,sec)
        self.img = ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.configure(image=self.img)
        self.lbl.after(200,self.working)





root = Tk()
obj = Clock(root)
root.mainloop()
