import tkinter
import tkinter as tk
from PIL import Image, ImageTk
import cv2 as cv

pa="./"
root=tk.Tk()
root.geometry("600x600+100+100")

pics=["santaelf.png","captainmorgan.jpg","Pampero.jpg","Oronoc.jpg","guinness2.jpg"]

for pic in pics:
  path=pa+pic 
  #im = Image.open(path)  
    
  # Size of the image in pixels (size of orginal image)  
  # (This is not mandatory)  
  #width, height = im.size  
  newsize = (500, 500) 
  #im1 = im.resize(newsize) 
  # Shows the image in windows image viewer  
  #im1.show()  
  #using PIL
  image = Image.open(path)
  phot=image.resize(newsize)
  phot=ImageTk.PhotoImage(phot)
  #photo = ImageTk.PhotoImage(image)
  #You can use a PhotoImage instance everywhere Tkinter accepts an image object. An example:

  label = tk.Label(root,image=phot)
  label.image = phot # keep a reference!
  label.pack()
  print (path)
  key=cv.waitKey(0)&0xFF
  #canvas
  # photo = tk.PhotoImage(file=path)
  # w = tk.Canvas(root, image=photo,width=700, height=500)
  # w.pack()
  # w.create_line(0, 0, 200, 100)
  # w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
  # w.create_rectangle(800, 650, 150, 75, fill="blue")


  # label
  # photo = tk.PhotoImage(file=path)
  # w = tk.Label(root, text="hello")
  # w.photo = photo
  # w.pack()

  #frame = tk.Frame(root,highlightbackground="black", borderwidth=1,relief="sunken")   #highlightthickness=1  highlightbackground="black"
  # label = tk.Label(root,image=path,width=768, height=576, bg="", highlightbackground="black",borderwidth=1)
  # frame.pack()

  # redbutton = tk.Button(frame, text="Red", fg="red")
  # redbutton.pack( side = LEFT)
  # bottomframe = tk.Frame(root)
  # bottomframe.pack( side = BOTTOM )
  
#key=cv.waitKey(0)&0xFF








root.mainloop()