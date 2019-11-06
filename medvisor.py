from tkinter import *

class MyApp:

	def __init__(self, window):
		self.window = window
		self.window.geometry('600x500')
		self.window.title("Medvisor")
		Button(self.window, text = "Add Patient", command = self.add_patient).grid(row = 0, column = 0, sticky = 'news')
		Button(self.window, text = "Existing patient", command = self.existing_patient).grid(row = 0, column = 1, sticky = 'news')
		
		self.body = Frame(self.window)
		self.body.grid(row = 1, columnspan = 3)
		self.window.rowconfigure(0, weight = 1)
		self.window.rowconfigure(1, weight = 12)
		self.window.columnconfigure(0, weight=1)
		self.window.columnconfigure(1, weight=1)

	def add_patient(self):
		fields = ['RecordID', 'Age', 'Gender', 'Height', 'ICUType', 'Weight']

		for i in range(fields):
			Label(self.body, text = "Enter " + fields[i] + ": ").grid(row = i, column = 0, sticky = 'news', pady = 5)
			ent = Entry(self.body)
			ent.grid(row = 0, column = 1, pady = 5)
			
		


	def existing_patient(self):
		print("Existing patient") 

	def delete_patient(self):
		print("Delete patient") 

window = Tk()
gui = MyApp(window)
window.mainloop()