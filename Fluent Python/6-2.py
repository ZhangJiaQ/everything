#coding: utf-8
from abc import ABC, abstractmethod
from collections import nametuple

Customer = nametuple('Customer', 'name fidelity')

class LineItem(object):
	
	def __init__(self, product, quantity, price):
		self.product = product
		self.quantity = quantity
		self.price = price
		
	def total(self):
		return self.quantity * self.price
		

class Order(object):   #上下文
	
	def __init__(self, customer, cart, promotion=None):
		self.customer = customer
		self.cart = list(cart)
		self.promotion = promotion
		
	def total(self):
		if not hasattr(self, '__total'):
			self.__total = sum(item.total() for item in self.cart)
		return self.__total
	
	
	def due(self):
		if self.promotion is None:
			discount = 0
		else:
			discount = self.promotion.discount(self)
		return total - discount
		
		
	def __repr__(self):
		fmt = '<Order total: {:.2f} due: {:.2f}>'
		return fmt.format(self.total(), self.due())
	
			
class Promotion(ABC): #策略：抽象基类
	
	@abstractmethod
	def discount(self, order):
		return 
			

class FidelityPromo(Promotion):
	
	def discount(self, order):
		return order.total() * .05 if order.customer.fidelity >= 1000 else 0
		

class BulkItemPromo(Promotion):

	def discount(self, order):
		discount = 0
		for item in order.cart:
			if item.quantity >= 20:
				discount += item.total() * .1
		return discount
		

class LargeOrderPromo(Promotion):

	def discount(self, order):
		distinct_items = {item.product for item in order.cart}
		if len(distinct_items) >= 10:
			return order.total() * .07
		return 0
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			