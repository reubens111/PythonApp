#username - complete info
#id1      - 209339704 
#name1    - Gal Reubens 
#id2      - complete info
#name2    - complete info  

##search, delete
# pre, type etc

"""A class represnting a node in an AVL tree"""

from hashlib import new
from platform import node
from re import S
from types import NoneType
from typing import ValuesView


class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value=None,left=None,right=None,parent=None,height=-1,size=1,index=-1):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent
		self.height = height
		self.size = size
		self.setBalanceFactor() 
		self.index=index


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		if self.left == None:
			return None
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		if self.right == None:
			return None
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		if self.parent == None:
			return None
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		if self.isRealNode == True:
			return self.value
		return None

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		if self.isRealNode == True:
			return self.height
		return -1

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""

	def setLeft(self, node):
		self.left = node
		self.setHeight()
		self.setBalanceFactor()

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node
		self.setHeight()
		self.setBalanceFactor()

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node
		self.setHeight()
		self.setBalanceFactor()

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value

	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self):

		if self.left.height > self.right.height:
			self.height = self.left.height + 1
		else:
			self.height = self.right.height + 1
		

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setBalanceFactor(self):
		
		if self.getRight().isRealNode == False:
			RH=0
		else:
			RH=self.getRight().getHeight()+1
		if self.getLeft(node).isRealNode == False:
			LH=0
		else: LBF=self.getLeft().getHeight()+1

		self.balanceFactor=LH-RH

		
				
		




	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		if self.value == -1:
			return False #virutal
		return True #real node

	def getSize(self):
		if self.isRealNode() == True:
			return self.size
		return 0

	def setSize(self):
		self.size = self.left.size + self.right.size + 1

	def getBalanceFactor(self):
		return self.balancefactor

	def setBalanceFactor(self):
		self.balancefactor = self.left.height - self.right.height
		

	##for testing

	def printDetails(self):
		print("details for node ", self.value)
		print("value: ", self.value)
		if self.parent == None:
			print("this is the root")
		else:
			print("value of parent: ", self.parent.value)
		print("value of left son: ", self.left.value)
		print("value of right son: ", self.right.value)
		print("size: ", self.size)
		print("height: ", self.height)
		print("balance factor: ", self.balancefactor)
		print()


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self, root = None, first = None, last = None, length = 0, height = 0):
		self.root = None
		self.first = None
		self.last = None
		self.length = 0
		self.height = 0

	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		if self.root == None:
			return True
		else:
			return False

	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		a = self.root
		while i != 0:
			if i == a.right.size + 1:
				return a.value
			else:
				if i < a.right.size + 1:
					a = a.left

				else:
					i = i - a.right.size -1
					a = a.right
		





	##creates a new virtual node
	def newVirtualNode(self):
		return AVLNode(AVLNode(-1, None, None, None, -1, 0, -1))
	    




	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

	def insert(self, i, val):

			counter = 0
			newNode = AVLNode(val, None, None, None, -1, -1, -1)
			newVirtualLeft = AVLNode(-1, None, None, None, -1, 0, -1)
			newVirtualRight = AVLNode(-1, None, None, None, -1, 0, -1)

			if self.empty() == True: ##empty tree case
				self.root = newNode
				newNode.setLeft(newVirtualLeft)
				newNode.setRight(newVirtualRight)
				##mainting of fields
				newNode.setSize()
				newNode.setHeight()
				newNode.setBalanceFactor()
				return counter
			else: ##tree not empty
				if self.root.size < i: ##insert last
					a = self.root
					while a.right.isRealNode() == True:
						a = a.right
					a.setRight(newNode)
					newNode.setLeft(newVirtualLeft)
					newNode.setRight(newVirtualRight)
					newNode.setParent(a)
				else:
					##tree size is bigger than index
					a = self.predecessor(self.getNodeFromIndex(i))
					if a.right.isRealNode() == False: ##insert as right son
						a.right = newNode
						newNode.parent = a
						newNode.left = newVirtualLeft
						newNode.right = newVirtualRight
					else: ##insert between paretn and right son
						b = a.right
						a.right = newNode
						newNode.parent = a
						b.parent = newNode
						newNode.right = b
						newNode.left = newVirtualLeft

				##check balance factor and perform rotations

				pointer = newNode
				while pointer != None:
					pointer.setSize()
					pointer.setHeight()
					oldbf = pointer.getBalanceFactor()
					pointer.setBalanceFactor()
					newbf = pointer.getBalanceFactor()

					if newbf >= -1 and newbf <= 1: ##bf of node is valid
						if newbf == oldbf:
							break
					else: ##balance factor is not valid
						if pointer.getBalanceFactor() == -2:
							if pointer.right.getBalanceFactor() == -1:
								self.leftRotation(pointer)
								pointer.setSize()
								pointer.setHeight()
								pointer.setBalanceFactor()
								pointer.parent.setSize()
								pointer.parent.setHeight()
								pointer.parent.setBalanceFactor()
								counter = counter + 1
							else:
								self.rightleftRotation(pointer)
								counter = counter + 1
						else: ## balance factor is +2
							if pointer.left.balancefactor == -1:
								self.leftrightRotation(pointer)
								counter = counter + 1
							else:
								self.rightRotation(pointer)
								pointer.setSize()
								pointer.setHeight()
								pointer.setBalanceFactor()
								pointer.parent.setSize()
								pointer.parent.setHeight()
								pointer.parent.setBalanceFactor()
								counter = counter + 1
					pointer = pointer.parent

				while pointer != None:
					pointer.setSize()
					pointer.setHeight()
					pointer.setBalanceFactor()
					pointer = pointer.parent
				return counter


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		node=self.getNodeFromIndex(i)
		parent=node.getParent()


		##case: node is leaf
		if self.nodeLeafCase(node):
			parent.setBalanceFactor()
			return self.balance(parent)
			

		#case: node is not a leaf
		return self.deleteNodet()

		


		
	
	def deleteNode(self,node):
		nxt=self.succesor(node)
		balance=nxt.getRight()

		##connects nxt.right to next.parent
		nxt.getParent().setLeft(nxt.getRight())
		nxt.getRight().setParent(nxt.getParent())
		

		##sets the childrens of nxt
		nxt.setLeft(node.getLeft())
		nxt.setRight(node.getRight())

		##sets the parent of nxt
		if node==self.root:
			self.root=nxt
			nxt.setParent(None)
		else:
			nxt.setParent(node.getParent())	
		

		return self.balance(balance)

		
			



	


	##checks if the node is a leaf
	##if it is, it deletes it
	def nodeLeafCase(self,node):
		if node.right.isRealNode()==False and node.left.isRealNode()==False:
			if node.parent.right==node:
				node.parent.right=self.newVirtualNode()
				return True
			node.parent.left=self.newVirtualNode()
			return True
		return False

	##balances the given node
	##returns the number of rotation that were done
	def balance(self,node,cnt=0):
		b=node.getBalanceFactor()
		if b==1 or b==-1 or b==0:##if the balance factor is legal
			if node==self.root:
				return cnt
			return self.balance(node.getParent()) ##continues to balance up


		if b<-1: ##if the balance factor is illegal
			if node.getRight().getBalanceFactor()==-1:
				self.leftRotation(node)
				cnt+=1
			else:
				self.rightleftRotation(node)
				cnt+=2
		else:
			if node.getLeft.getBalanceFactor()==-1:
				self.leftrightRotation(node)
				cnt+=2
			else:
				self.rightRotation(node)
				cnt+=1
		node.setBalanceFactor()
		
		if node==self.root: ##continues up untill the root
			return cnt

		return self.balance(node.getParent(node.getParent(),cnt))
		


		







		


	


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		if self.isEmpty == True:
			return None
		return self.first.value

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return self.last.value

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		return None

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		if self.isEmpty == True:
			return 0
		return self.root.size

	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		a = self.first
		index = 1
		for  i in range(self.root.size):
			if self.retrieve(index) == val:
				return index
		return -1


	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		if self.isEmpty():
			return None
		return self.root


	def getNodeFromIndex(self, i):
		node=self.root
		while i!=node.index:
			if node.index>i:
				node=node.right
				continue
			node=node.left
		return node



	def succesor(self, node): ##recieves a node and returns the next node on the list

		if node.right.isRealNode == True:
			a = node.right
			while a.left.isRealNode == True:
				a = a.left
			return a
		else:
			while a.parent.left != a:
				a = a.parent
			return a.parent

	def predecessor(self, node): #recieves a node and returns the previous node on the list

		if node.left.isRealNode == True:
			a = node.left
			while a.right.isRealNode == True:
				a = a.right
			return a
		else:
			if node.parent.right == node:
				a = node.parent
				return a
			else:
				a = node.parent
				while a.parent.right == a:
					a = a.parent
				return a
		
	def getNode(self, i):
		a = self.root
		while i != 0:
			if i == a.left.size + 1:
				return a
			else:
				if i < a.size + 1:
					a = a.left
				else:
					a = a.right
					i = i - a.left.size	

	def printTree(self):
		for i in range(self.root.size):
			print(self.retrieve(i))

	def leftRotation(self, node):
		a = node
		b = node.right
		c = b.right

		a.right = b.left
		b.left.parent = a
		if self.root == node:
			self.root = b
			b.left = a
			b.parent = None
		else:
			if a.parent.left == a:
				a.parent.left = b
			else:
				a.parent.right = b

		b.parent = a.parent
		a.parent = b
		b.left = a

	def rightRotation(self, node):

		a = node
		b = node.left
		c = b.left

		a.left = b.right
		b.right.parent = a
		if self.root == a:
			self.root = b
			b.right = a
			b.parent = None
		else:
			if a.parent.left == a:
				a.parent.left = b
			else:
				a.parent.right = b
			b.parent = a.parent
			a.parent = b
			b.right = a
			


	def rightleftRotation(self, node):
		c = node
		a = node.right
		b = a.left

		if c.parent.right == c:
			c.parent.right = b
		else:
			c.parent.left = b
		c.right = b.left
		b.left = c
		a.parent = b
		b.right = a

	def leftrightRotation(self, node):
		c = node
		a = node.left
		b = a.right

		if c.parent.left == c:
			c.parent.left = b
		else:
			c.parent.right = b
		b.parent = c.parent
		c.left = b.right
		b.right = c
		a.parent = b
		b.left = a

	

	def printTree(self):
		if self.empty() == False:
			for i in range(self.root.size):
				print(self.retrieve(i))


##tester

AVLTreeList1 = AVLTreeList(None, None, None, 0, 0)
a = AVLTreeList1.empty()
print(a)
print("number of rotations: ", AVLTreeList1.insert(1, 1))

print("number of rotations", AVLTreeList1.insert(2,2))
print("size of tree/1: ", AVLTreeList1.root.size)
print("value: ", AVLTreeList1.root.right.value)
print("height: ", AVLTreeList1.root.right.height)
print("size: ", AVLTreeList1.root.right.size)
print("balance factor: ", AVLTreeList1.root.right.balancefactor)
AVLTreeList1.root.printDetails()
AVLTreeList1.root.right.printDetails()
print("number of rotations of 3: ", AVLTreeList1.insert(3,3))
print("-------")
AVLTreeList1.root.printDetails()
AVLTreeList1.root.left.printDetails()
AVLTreeList1.root.right.printDetails()
print("number of rotations of 4: ", AVLTreeList1.insert(4,5))
print("--------------")
AVLTreeList1.root.printDetails()
AVLTreeList1.root.left.printDetails()
AVLTreeList1.root.right.printDetails()
AVLTreeList1.root.right.right.printDetails()
print("number of rotations of 4: ", AVLTreeList1.insert(4,4))
AVLTreeList1.root.printDetails()
AVLTreeList1.root.left.printDetails()
AVLTreeList1.root.right.printDetails()
AVLTreeList1.root.right.right.printDetails()
AVLTreeList1.root.right.left.printDetails()



