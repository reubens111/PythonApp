#username - complete info
#id1      - 209339704 
#name1    - Gal Reubens 
#id2      - 313330490
#name2    - Bar Avidov



"""A class represnting a node in an AVL tree"""

import array
from hashlib import new
from platform import node
from random import randint
from re import S
from this import d
from typing import ValuesView

#def setFirst setlast

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value=None,left=None,right=None,parent=None,height=-1,size=1):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent
		self.height = height
		self.size = size
		self.balancefactor = None
		


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
		if self.isRealNode() == True:
			return self.value
		return None

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		if self.isRealNode() == True:
			return self.height
		return -1

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""

	def setLeft(self, node):
		self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value

	"""sets height

	@type height: int
	"""
	def setHeight(self):

		if self.right.isRealNode() == True:
			RH = self.right.getHeight()
		else:
			RH = -1
		if self.left.isRealNode() == True:
			LH = self.left.getHeight()
		else:
			LH = -1


		if LH > RH:
			self.height = LH + 1
		else:
			self.height = RH + 1
		

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		if self.height == -1:
			return False #virutal
		return True #real node

	"""returns the size of the node

	@rtype: int
	@returns: size of the node's rooted tree, 0 if virtual node
	"""

	def getSize(self):
		if self.isRealNode() == True:
			return self.size
		return 0

	"""sets size
	@type size: int
	"""
	def setSize(self):
		self.size = self.left.size + self.right.size + 1

	"""returns the balance factor
	@rtype: int
	@returns: balance factor of the node
	"""

	def getBalanceFactor(self):
		return self.balancefactor

	"""sets balance factor
	@type balancefactor: int

	"""

	def setBalanceFactor(self):
		LH = -1 #left and right height, if they dotn exist the value will be 0
		RH = -1
		if self.left.isRealNode():
			LH=self.left.height
		if self.right.isRealNode():
			RH=self.right.height
		self.balancefactor = LH - RH
		
	"""

	@type: prints the fields of the node
	@returns: prints value, parent value, left child value, right child value,
			  size, height and balance factor 

	"""
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
		self.root = root
		self.first = first
		self.last = last
		self.length = length
		self.height = height

	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""

	def empty(self):
		if self.root == None:
			return True
		else:
			return False

	"""returns the height of the tree

	@rtype: int
	@returns: the height of the tree, -1 if the tree is empty
	"""

	def getHeight (self):
		if self.root.isRealNode():
			return self.height
		return -1

	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the value of the i'th item in the list
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
			newNode = AVLNode(val, None, None, None, -1, -1)
			newVirtualLeft = AVLNode(-1, None, None, None, -1, 0)
			newVirtualRight = AVLNode(-1, None, None, None, -1, 0)
			newNode.setLeft(newVirtualLeft)
			newNode.setRight(newVirtualRight)

			if self.empty() == True:
				self.root = newNode
				self.first = newNode
				self.last = newNode
				self.maintainFields(newNode)
				return 0

			if i == 0:
				self.first = newNode
			else:
				if i == self.root.size:
					self.last = newNode
			return self.insertNode(i, newNode)

	"""inserts a new node in the i'th index of the list
	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert the node
	@type node: AVLNode
	@param node: the node intended to insert
	@rtype: list
	@returns: the number of rotation operations due to AVL rebalancing
	
	"""
	def insertNode(self, i, node):

		if i == self.root.getSize():
			currentnode = self.root
			while currentnode.right.isRealNode() == True:
				currentnode = currentnode.right
			currentnode.setRight(node)
			node.setParent(currentnode)
		else:
			currentnode = self.getNodeFromIndex(i+1)
			if currentnode.left.isRealNode() == False:
				currentnode.setLeft(node)
				node.setParent(currentnode)
			else:
				predecessor = self.predecessor(currentnode)
				predecessor.setRight(node)
				node.setParent(predecessor)
		
		
		return self.balance(node)


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		node = self.getNodeFromIndex(i+1)
		return self.deleteNode(node)

		

	##deletes the given node from the tree with balancing
	def deleteNode(self,node):


		if node == self.root:

			if self.root.size == 1:
				self.root = None
				return 0

			if  node.right.isRealNode() == False:
				self.root = self.root.left
				self.root.setParent(None)
				return 0


			succesor=self.succesor(node)
			succesorparent=succesor.parent
			succesorson=succesor.right

			if succesor.parent == node:
				self.root = succesor
				succesor.setParent(None)
				succesor.left = node.left
				node.left.setParent(succesor)
				return 0

			succesorparent.setLeft(succesorson)
			if succesorson.isRealNode():
				succesorson.setParent(succesorparent)

			self.root = succesor
			succesor.setParent(None)
			succesor.setLeft(node.left)
			succesor.setRight(node.right)
			node.right.setParent(succesor)
			node.left.setParent(succesor)
			return self.balance(succesorparent)
		
		##case1: node is leaf
		if self.nodeLeafCase(node):
			if self.root == node:
				self.root = None
			parent=node.getParent()
			if node.parent.right == node:
				node.parent.setRight(node.left)
			else:
				node.parent.setLeft(node.left)

			return self.balance(node.parent)

		#case2: node has two children
		else:
			if node.left.isRealNode() and node.right.isRealNode():
				succesor = self.succesor(node)
				if node.right == succesor:
					succesor.setParent(node.parent)
					if node.parent.left == node:
						node.parent.setLeft(succesor)
					else:
						node.parent.setRight(succesor)
					succesor.setLeft(node.left)
					node.left.setParent(succesor)
					return self.balance(succesor)
				else:
					succesorparent = succesor.getParent()
					succesorson = succesor.getRight()

					succesorparent.setLeft(succesorson)
					succesorson.setParent(succesorparent)

					succesor.setParent(node.parent)
					if node.parent.left == node:
						node.parent.left = succesor
					else:
						node.parent.right = succesor
					succesor.setRight(node.right)
					node.right.setParent(succesor)
					succesor.setLeft(node.left)
					node.left.setParent(succesor)

				return self.balance(succesorparent)

		#case3: node has one children
			else:
				if node.left.isRealNode() == True:
					parent = node.parent
					left = node.left

					if parent.getLeft() == node:
						parent.setLeft(left)
					else:
						parent.setRight(left)
					left.setParent(parent)
					node.setParent(None)
					node.setLeft(None)
				else:
					parent = node.parent
					right = node.right

					if parent.getRight() == node:
						parent.setRight(right)
					else:
						parent.setLeft(right)
					right.setParent(parent)
					node.setParent(None)
					node.setRight(None)
			
			return self.balance(parent)
			


	##checks if the node is a leaf
	##if it is, it deletes it without balancing
	def nodeLeafCase(self,node):
		if node.right.isRealNode() == False and node.left.isRealNode() == False:
			return True
		else:
			return False




	
		


		


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		if self.isEmpty:
			return None
		node=self.root
		while node.getLeft().isRealNode():
			node=node.getLeft()
		return node.getValue()

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		if self.isEmpty:
			return None
		node=self.root
		while node.getRight().isRealNode():
			node=node.getRight()
		return node.getValue()

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):

		array = []
		if self.empty() == False:
			self.inOrder(self.root, array)
		return array

	"""adds the value of all nodes in tree in order to an array
	@pre array is empty
	@rtype: list

	"""

	def inOrder(self, node, array):
		if node.left.isRealNode() == True:
			self.inOrder(node.left, array)
		array.insert(len(array), node.value)
		if node.right.isRealNode() == True:
			self.inOrder(node.right, array)

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

		if lst.empty():
			if self.empty():
				return 0
			return self.root.height
		if self.empty():
			self.root=lst.root
			return self.root.height

		returnValue=abs(self.root.height-lst.root.height)

		x=lst.first
		lst.delete(0)

		if lst.empty():
			self.insert(self.root.size,x.value)
			return returnValue

		if self.root.size > lst.root.size:
			h=lst.root.height
			b=self.root
			a=lst.root
			root=self.root
		else:
			h=self.root.height
			b=lst.root
			a=self.root
			root=lst.root
		
		while abs(h-b.height) > 1:
			
			if b.left.isRealNode():
				b=b.left
			else:
				b=b.right

			
		
		

		if b.parent != None:
			if  b.parent.left == b:
				b.parent.setLeft(x)
				x.setParent(b.parent)
			else:
				b.parent.setRight(x)
				x.setParent(b.parent)
		else:
			root=x
			
		
		
		
		if a==self.root:
			x.setLeft(a)
			x.setRight(b)
			self.root=root
			lst.root=self.root
			
		else:
			x.setLeft(b)
			x.setRight(a)
			self.root=root
			lst.root=self.root
			

		while x != None:

			self.maintainFields(x)
			x=x.parent
		
		return returnValue
		

	


	



	"""updates fields height, size and balance factor of the node
	@param node: AVLTree
	"""
	def maintainFields(self, node):
		node.setHeight()
		node.setSize()
		node.setBalanceFactor()

		



	

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return self.searchTree(self.root, val) - 1
		

	"""searches for a *value* in the tree that it's root is node

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found
	"""
	def searchTree(self, node, val):

		if node.isRealNode() == False:
			return 0

		if self.searchTree(node.left, val) != 0:
			return self.searchTree(node.left, val)

		if node.getValue() == val:
			return self.getIndexFromNode(node)

		if self.searchTree(node.right, val) != 0:
			return self.searchTree(node.right, val)

		return 0

	"""returns the index of the node in the list

	@type node: AVLNode
	@param node: pointer to the node
	@rtype: int
	@returns: the index of the node
	"""
	
	def getIndexFromNode(self, node):
		i = node.left.getSize() + 1
		while node != None:
			if self.root == node.parent and node.parent.right == node:
				i = i + self.root.left.getSize() + 1
			else:
				if node != self.root:
					if node.parent.right == node:
						i = i + node.parent.left.getSize() + 1
			
			node = node.parent
		return i

	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		if self.empty() == True:
			return None
		return self.root

	"""returns a pointer to the node in the i index

	@rtype: int
	@returns: the node in the i index
	"""

	def getNodeFromIndex(self, i):
		j = i
		a = self.root

		while j != a.left.size + 1:
			if j < a.left.size + 1:
					a = a.left
			else:
				j = j - a.left.size - 1
				a = a.right
		return a

	"""return a pointer to the node in the next index
	@type node: AVLNode
	@rtype: AVLNode
	@returns: the next node in the list, None if node is the last in the list
	"""
	def succesor(self, node): ##recieves a node and returns the next node on the list

		if node == self.last:
			return None
		if node.right.isRealNode() == True:
			a = node.right
			while a.left.isRealNode() == True:
				a = a.left
			return a
		else:
			while a.parent.left != a:
				a = a.parent
			return a.parent

	"""returns a pointer to the node in the previous index in the list
	@type node: AVLNode
	@rtype: AVLNode
	@returns: the previous node in the list, None if the node is the first in the list
	"""

	def predecessor(self, node): #recieves a node and returns the previous node on the list

		if node == self.first:
			return None
		if node.left.isRealNode() == True:
			a = node.left
			while a.right.isRealNode() == True:
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

	"""performs balance rotations if needed to balance the AVL tree
	@type node: AVLNode
	@rtype: int
	@returns: number of rotations performed on tree
	"""

	def balance(self,node):
		counter = 0
		while node != None:
			oldbalancefactor = node.getBalanceFactor()
			self.maintainFields(node)
			newbalancefactor = node.getBalanceFactor()


			if newbalancefactor == 2:
				if node.left.getBalanceFactor() == 1 or node.left.getBalanceFactor() == 0:
					self.rightRotation(node)
					counter = counter + 1
				else:
					self.leftrightRotation(node)
					counter = counter + 1
			if newbalancefactor == -2:
				if node.right.getBalanceFactor() == -1 or node.right.getBalanceFactor() == 0:
					self.leftRotation(node)
					counter = counter + 1
				else:
					self.rightleftRotation(node)
					counter = counter + 1
			node = node.parent
		return counter


	"""performs a left rotation
	@type node: AVLNode
	@rtype: int
	@returns: number of rotation operations performed
	"""

	def leftRotation(self, node):
		a = node
		b = node.right
		c = b.right

		a.right = b.left
		b.left.parent = a
		if self.root == node:
			self.root = b
			b.parent = None
		else:
			if a.parent.left == a:
				a.parent.left = b
			else:
				a.parent.right = b
			b.setParent(a.parent)
		a.setParent(b)
		b.setLeft(a)

		self.maintainFields(a)
		self.maintainFields(b)
		self.maintainFields(c)

	"""performs a right rotation
	@type node: AVLNode
	@rtype: int
	@returns: number of rotation operations performed
	"""

	def rightRotation(self, node):
		a = node
		b = node.left
		c = a.left.left

		a.left = b.right
		b.right.parent = a
		if self.root == a:
			self.root = b
			b.parent = None
		else:
			if a.parent.left == a:
				a.parent.left = b
			else:
				a.parent.right = b
			b.setParent(a.parent)
		a.setParent(b)
		b.setRight(a)

		self.maintainFields(a)
		self.maintainFields(b)
		self.maintainFields(c)
			
	"""performs a right and left rotation
	@type node: AVLNode
	@rtype: int
	@returns: number of rotation operations performed
	"""

	def rightleftRotation(self, node):
		a = node
		b = node.right
		c = node.right.left

		if self.root == a:
			self.root = c
			c.setParent(None)
		else:
			if a.parent.left == a:
				a.parent.left = c
			else:
				a.parent.right = c
			c.setParent(a.parent)
		b.setLeft(c.right)
		b.left.setParent(b)
		a.setRight(c.left)
		a.right.setParent(a)

		b.setParent(c)
		a.setParent(c)
		c.setLeft(a)
		c.setRight(b)

		self.maintainFields(a)
		self.maintainFields(b)
		self.maintainFields(c)

	"""performs a left right rotation
	@type node: AVLNode
	@rtype: int
	@returns: number of rotation operations performed
	"""
	def leftrightRotation(self, node):
		a = node
		b = node.left
		c = node.left.right

		if self.root == a:
			self.root = c
			c.setParent(None)
		else:
			if a.parent.left == a:
				a.parent.left = c
			else:
				a.parent.right = c
			c.setParent(a.parent)
		b.setRight(c.left)
		b.right.setParent(b)
		a.setLeft(c.right)
		a.left.setParent(a)

		b.setParent(c)
		a.setParent(c)
		c.setLeft(b)
		c.setRight(a)

		self.maintainFields(a)
		self.maintainFields(b)
		self.maintainFields(c)

	##tester functions:

	def inOrderPrint(self, node):

		if node.left.isRealNode() == True:
			self.inOrderPrint(node.left)
		print(self.getIndexFromNode(node))
		if node.left==None:
			print(node.value, "left")
		if node.right==None:
			print(node.value, "right")
		if abs(node.getBalanceFactor())>1:
			print(node.value, "balanceFactor")
		if node != self.root and node.parent==None:
			print(node.value, "parnet")
		if node.right.isRealNode() == True:
			self.inOrderPrint(node.right)
	
##experiments


tree1=AVLTreeList()
tree2=AVLTreeList()
tree3=AVLTreeList()

n1 = 100
counter1 = 0
counter2=0
for i in range (0, n1):
	if tree2.empty() == True:
		index = randint(0, 0)
	else:
		index = randint(0, tree2.root.size)
	if i<n1/2:
		counter1 = counter1 + tree1.insert(index, i)
	counter2 = counter2 + tree2.insert(index, i)
	
tree1.concat(tree2)

print(tree1.root.size)
