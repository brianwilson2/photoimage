root.geometry("%dx%d+%d+%d" % (w, h, x, y))
panel1 = tk.Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')
panel1.image = image1
root.overrideredirect(True)

root.mainloop()