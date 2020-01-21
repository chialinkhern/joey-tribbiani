import tkinter as tk
import joey

class GUI:

	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Joey Tribbiani")

		self.fin = tk.StringVar()

		self.image = tk.PhotoImage(file="Images/Joey.gif")
		self.imgLabel = tk.Label(image=self.image)
		self.imgLabel.pack()

		self.browseButton = tk.Button(self.root, text="Select File", command=self.askopenfile)
		self.browseButton.pack()

		self.selectedDir = tk.Label(self.root, text=" ")
		self.selectedDir.pack()

		self.executeButton = tk.Button(self.root, text="Joeyfy", command=self.doTheJoey)
		self.executeButton.pack()

		self.root.mainloop()

	def askopenfile(self):
		self.finDir = tk.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
		self.selectedDir['text'] = self.finDir

	def doTheJoey(self):
		Joey = joey.Joey(str(self.finDir))
		Joey.joeyfy()
		self.root.destroy()

