"""

Program:InvestmentGUI.py
Author: Kofi
Excercise on pages 276 - 277
from Chapter 3

"""

from breezypythongui import EasyFrame

class InvestmentGUI(EasyFrame):
	"""An investment calculator that demonstarates the use of a multi-line text area."""

	def __init__(self):
		"""Sets up the window and widgets"""
		EasyFrame.__init__(self, title = "Investment Calculator", background = "tan")
		self.setResizable(False)

		# Labels for the window 
		self.addLabel(text = "Initial Amount", 
					  row = 0, 
					  column = 0,
					  background = "tan")

		self.addLabel(text = "Number of Years", 
					  row = 1, 
					  column = 0,
					  background = "tan")

		self.addLabel(text = "Interest Rate in %", 
					  row = 2, 
					  column = 0,
					  background = "tan") 

		# Entry fields
		self.amount = self.addFloatField(value = 0.0,
										 row = 0,
										 column = 1)

		self.period = self.addIntegerField(value = 0,
										   row = 1,
										   column = 1)

		self.rate = self.addIntegerField(value = 0,
										   row = 2,
										   column = 1)

		# Text-area widget
		self.outputArea = self.addTextArea(text = "", 
										   row = 4, 
										   column = 0,
										   columnspan = 2,
										   width = 50,
										   height = 15)

		# Command button widgets
		self.compute = self.addButton(text = "Compute", 
			row = 3, 
			column = 0,
			columnspan = 2, 
			command = self.compute)

	# Event handling method
	def compute (self):
		"""Computes the investment schedule based on the inputes of the GUI and then outputs the schedule in the text area."""
		# Obtain and validate the inputs
		startBalance = self.amount.getNumber()
		rate = self.rate.getNumber() / 100
		years = self.period.getNumber()
		if startBalance == 0 or rate == 0 or years == 0:
			return

		# Set the header for the table
		result = "%4s%18s%10s%16s\n" % ("Year", 
									  "Starting Balance",
									  "Interest", 
									  "Ending Balance")

		# Compute and append the result for each year
		totalInterest = 0.0
		for year in range(1, years + 1):
			interest = startBalance * rate 
			endBalance = startBalance + interest
			result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest

		# Append the toats foe the entire period
		result += "Ending balance: $%0.2f\n" % endBalance
		result += "Total interest earned: $%0.2f\n" % totalInterest

		#Output the result while preserving read-onluy status
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"

def main():
	"""Instantiate and pop the window"""
	InvestmentGUI().mainloop()

# Global call to the main() function
main()


	 


			 
				  
