from abc import ABC, abstractmethod
class house(ABC):
	def receipt(self, amount):
		print("Total is: ", amount)
	
	def payment(self, amount):
		pass
		
class CreditCardPayment(house):
	def payment(self,amount):
		print('Total {} exceeds limit '.format(amount))
		
obj = CreditCardPayment()
obj.receipt("$100")
obj.payment("$100")