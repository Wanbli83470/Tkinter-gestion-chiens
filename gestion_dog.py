import tkinter
from tkinter import *
from tkinter import ttk
import random


class coureur():
	def __init__(self, root):
		self.counter_dog = 3
		self.status_label = ttk.Label(root, text="Mon nombre de chien : 3")
		self.add_girlfriend_button = ttk.Button(root, text="j'ai de nouvelles naissance",command=self.add_dog)
		self.remove_girlfrind_butoon = ttk.Button(root, text="j'ai vendu un chien",command=self.remove_dog)
		self.status_label.pack()
		self.add_girlfriend_button.pack()
		self.remove_girlfrind_butoon.pack()

	def add_dog(self):
		self.counter_dog += 2
		self.status_label.config(text='nombre de chiens actuel : ' + str(self.counter_dog))

	def remove_dog(self):
		if self.counter_dog > 0:
			self.counter_dog -= 1
			self.status_label.config(text='nombre de chiens actuel : ' + str(self.counter_dog))




root = Tk()
root.title('gestion chiens chenil')
app = coureur(root)
root.mainloop()


		