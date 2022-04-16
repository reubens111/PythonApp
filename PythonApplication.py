#username - complete info
#id1      - 209339704 
#name1    - Gal Reubens 
#id2      - 313330490
#name2    - Bar Avidov



"""A class represnting a node in an AVL tree"""

import array
from hashlib import new
from platform import node
from re import S
from this import d
from types import NoneType
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

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self):

		if self.right.isRealNode() == False:
			RH=0
		else:
			RH=self.rigth.height
		if self.left.isRealNode() == False:
			LH=0
		else:
			LH=self.left.height


		if LH > RH:
			self.height = LH + 1
		else:
			self.height = RH + 1
		

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		if self.value == -1:
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

	"""calculates and sets the size of the node
	@type
	@param size: size of both sons + 1
	"""
	def setSize(self):
		self.size = self.left.size + self.right.size + 1

	"""returns the balance factor of the node
	@rtype: int
	@returns: balance factor of the node
	"""

	def getBalanceFactor(self):
		return self.balancefactor

	"""calculates and sets the balance of the node
	@type
	@returns: balance factor as the difference in heights of left and right son

	"""

	def setBalanceFactor(self):
		LH=0 #left and right height, if they dotn exist the value will be 0
		RH=0
		if self.left.isRealNode:
			LH=self.left.height
		if self.right.isRealNode:
			RH=self.right.heigth
		self.balancefactor = self.left.height - self.right.height
		
	"""

	@type: prints the fields of the node
	@returns: prints value, parent, value of left child, value of right child,
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


	"""returns the height of the tree

	@rtype: int
	@returns: the height of the tree, -1 if the tree is not real
	"""

	def getHeight (self):
		if self.root.isRealNode():
			return self.height
		return -1
	
	"""returns the being of the tree

	@rtype: boolean
	@returns: True if the tree is empty, false if the tree has atleast one element
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

			if i == 1:
				self.first = newNode
			else:
				if i == self.root.size:
					self.last = newNode

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
					node = self.getNodeFromIndex(i)
					if node.left.isRealNode() == False:
						node.left = newNode
						newNode.parent = node
						newNode.left = newVirtualLeft
						newNode.right = newVirtualRight
					else:
						prev = self.predecessor(node)
						prev.right = newNode
						newNode.parent = prev
						newNode.left = newVirtualLeft
						newNode.right = newVirtualRight


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
		return self.deleteNode(node)



	##deletes the given node from the tree with balancing
	def deleteNode(self,node):

		nxt=None#the succesor of node
		con=None#the right child of next, if it is not real, the left child


		nxt=self.succesor(node)
		if node.getRight.isRealNode:
			con=nxt.getRight()
		else:
			con=nxt.getLeft()

		##connects con	 to next.parent
		nxt.getParent().setLeft(con)
		con.setParent(nxt.getParent())
		

		##sets the childrens of nxt (the former children of node)
		nxt.setLeft(node.getLeft())
		nxt.setRight(node.getRight())

		##sets the parent of nxt (the former parent of node)
		if node==self.root:
			self.root=nxt
			nxt.setParent(None)
		else:
			nxt.setParent(node.getParent())	
		
		if self.empty():
			return 0
		return self.balance(con)

		
			


	##checks if the node is a leaf
	##if it is, it deletes it without balancing
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
	right is an AVLTreeList representing
   the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):

		left=AVLTreeList()
		right=AVLTreeList()
		root=None

		root,left,right=self.splitRec(self.root,left,right,i)
		root.setRight(right)
		root.setLeft(left)

		return root
			
	def splitRec(self,root,left,right,i):
		
		if i==root.getLeft().getSize()+1: ##case: root id the i item
			root.getLeft().concat(left)
			return root,left,right


		if i<root.getLeft.getSize()+1: #case: root is bigger than i
			return self.concat(self.splitRec(root.getLeft(),left,right,i))

		return self.concat(self.splitRec(root.getRight(),left,right,i-root.getLeft.getSize-1))



		a
	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):

		returnValue=abs(self.height-lst.height)
		
		## while the trees are not at the same height
		while abs(self.root.getHeight() - lst.getRoot().getHeight()) >1:
			self.setNextNode(lst) 
			
		return returnValue



		



	"""returns the next node to be connected

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: AVLNode
	@returns: the next node to be contacted to self
	"""
	def setNextNode (self,lst):
		
		if self.height > lst.getHeight():
			big = self
			small=lst
			node = self
			h=lst.height
		else:
			small=self
			big = lst
			node = lst
			h=self.height
		
		while big.getleft().isRealNode() and abs(node.getHeight()-h)>1:
			node=node.getLeft()


		
		nxt=node.getRight()
		big.delete(node)

		if big.getRoot()==self.getRoot():
			node.setleft(nxt)
			nxt.setParent(node)
			node.setRight(small.getRoot())
			small.getRoot.setParent(node)
			small.setRoot(node)
		else:
			node.setRight(nxt)
			nxt.setParent(node)
			node.setLeft(small.getRoot())
			small.getRoot.setParent(node)
			small.setRoot(node)

		

		

	"""takes out node from the tree 

	@type node: AVLNode
	@param node: 
	"""

	def realeaseFromDuty(self, node):

		nxt=None#the succesor of node
		con=None#the right child of next, if it is not real, the left child


		nxt=self.succesor(node)

		if node.getRight.isRealNode():
			con=nxt.getRight()
		elif node.getLeft.isRealNode():
			con=nxt.getLeft()
		else:  #the node is a leaf
			node.setParent(None)
			return



		##connects con	 to next.parent
		nxt.getParent().setLeft(con)
		con.setParent(nxt.getParent())
		

		##sets the childrens of nxt (the former children of node)
		nxt.setLeft(node.getLeft())
		nxt.setRight(node.getRight())

		##sets the parent of nxt (the former parent of node)
		if node==self.root:
			self.root=nxt
			nxt.setParent(None)
		else:
			nxt.setParent(node.getParent())	
		
		

	

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return self.searchTree(self.root, val)
		

	"""searches for a *value* in the tree that it's root is node

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found
	"""
	def searchTree(self, node, val):

		if node.isRealNode() == False:
			return -1

		if self.searchTree(node.left, val) != -1:
			return self.searchTree(node.left, val)

		if node.getValue() == val:
			return self.getIndexFromNode(node)

		if self.searchTree(node.right, val) != -1:
			return self.searchTree(node.right, val)

		return -1

	"""returns the index of the node in the list

	@type node: AVLNode
	@param node: pointer to the node
	@rtype: int
	@returns: the index of the node
	"""
	
	def getIndexFromNode(self, node):
		i = node.left.getSize() + 1
		while node != None:
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
		if self.isEmpty():
			return None
		return self.root

	"""returns a pointer to the node in the i index

	@rtype: int
	@returns: the node in the i index
	"""

	def getNodeFromIndex(self, i):
		a = self.root
		while i != 0:
			if i == a.left.size + 1:
				return a
			else:
				if i < a.left.size + 1:
					a = a.left
				else:
					i = i - a.left.size - 1
					a = a.right
					
		return a

	"""return a pointer to the node in the next index

	@rtype: AVLNode
	@returns: the next node in the list, None if node is the last in the list
	"""
	def succesor(self, node): ##recieves a node and returns the next node on the list

		if node == self.last:
			return None
		if node.right.isRealNode == True:
			a = node.right
			while a.left.isRealNode == True:
				a = a.left
			return a
		else:
			while a.parent.left != a:
				a = a.parent
			return a.parent

	"""returns a pointer to the node in the previous index

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

	"""performs a left rotation

	@rtype: AVLNode
	"""

	def leftRotation(self, node):
		print("left-Rotation")
		a = node
		b = node.right
		c = b.right

		a.right = b.left
		b.left.parent = a
		if self.root == node:
			self.root = b
			b.parent = None
		else:
			b.parent = a.parent
			if a.parent.left == a:
				a.parent.left = b
			else:
				a.parent.right = b

			
		a.parent = b
		b.left = a

		a.setSize()
		a.setHeight()
		a.setBalanceFactor()
		c.setSize()
		c.setHeight()
		c.setBalanceFactor()
		b.setSize()
		b.setHeight()
		b.setBalanceFactor()

	"""performs a right rotation

	@rtype: AVLNode
	"""

	def rightRotation(self, node):
		print("right-Rotation")
		a = node
		b = node.left
		c = b.left

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
			b.parent = a.parent
			a.parent = b
			b.right = a

		a.setSize()
		a.setHeight()
		a.setBalanceFactor()
		c.setSize()
		c.setHeight()
		c.setBalanceFactor()
		b.setSize()
		b.setHeight()
		b.setBalanceFactor()
			
	"""performs a right and left rotation

	@rtype: AVLNode
	"""

	def rightleftRotation(self, node):
		print("right-left-Rotation")
		c = node
		a = node.right
		b = a.left

		b.parent = c.parent
		c.right = b.left
		a.left = b.right
		b.left.parent = c
		b.right.parent = a
		if self.root == c:
			self.root = b
			b.parent = None
		else:
			if c.parent.right == c:
				c.parent.right = b
			else:
				if c.parent.left == c:
					c.parent.left = b
				else:
					c.parent.right = b
				b.parent = c.parent

		b.left = c
		b.right = a
		c.parent = b
		a.parent = b

		a.setSize()
		a.setHeight()
		a.setBalanceFactor()
		c.setSize()
		c.setHeight()
		c.setBalanceFactor()
		b.setSize()
		b.setHeight()
		b.setBalanceFactor()
		
		
	"""performs a left right rotation

	@rtype: AVLNode
	"""
	def leftrightRotation(self, node):
		print("left-right-Rotation")
		c = node
		a = node.left
		b = a.right

		b.parent = c.parent
		c.left = b.right
		a.right = b.left
		if self.root == c:
			self.root = b
			b.parent = None
		else:	
			if c.parent.left == c:
				c.parent.left = b
			else:
				c.parent.right = b
			b.parent = c.parent
		
		b.left = a
		a.parent = b
		b.right = c
		c.parent = b

		a.setSize()
		a.setHeight()
		a.setBalanceFactor()
		c.setSize()
		c.setHeight()
		c.setBalanceFactor()
		b.setSize()
		b.setHeight()
		b.setBalanceFactor()










	######################################## Put these functions ########################################
	##################################### inside AVLTreeList class ######################################

	"""Checks if the AVL tree properties are consistent

	##self notes about the tester:
	#getSentinel() => isRealNode

	@rtype: boolean 
	@returns: True if the AVL tree properties are consistent
	"""
	def check(self):
		if not self.isAVL():
			print("The tree is not an AVL tree!")
		if not self.isSizeConsistent():
			print("The sizes of the tree nodes are inconsistent!")
		if not self.isHeightConsistent():
			print("The heights of the tree nodes are inconsistent!")
		if not self.isRankConsistent():
			print("The ranks of the tree nodes are inconsistent!")

	"""Checks if the tree is an AVL

	@rtype: boolean 
	@returns: True if the tree is an AVL tree
	"""
	def isAVL(self):
		return self.isAVLRec(self.getRoot())

	"""Checks if the subtree is an AVL
	@type x: AVLNode
	@param x: The root of the subtree
	@rtype: boolean 
	@returns: True if the subtree is an AVL tree
	"""
	def isAVLRec(self, x):
		# If x is a virtual node return True
		if x == self.getSentinel():
			return True
		# Check abs(balance factor) <= 1
		bf = x.balanceFactor()
		if bf > 1 or bf < -1:
			return False
		# Recursive calls
		return self.isAVLRec(x.getLeft()) and self.isAVLRec(x.getRight())

	"""Checks if sizes of the nodes in the tree are consistent

	@rtype: boolean 
	@returns: True if sizes of the nodes in the tree are consistent
	"""
	def isSizeConsistent(self):
		return self.isSizeConsistentRec(self.getRoot())

	"""Checks if sizes of the nodes in the subtree are consistent

	@type x: AVLNode
	@param x: The root of the subtree
	@rtype: boolean 
	@returns: True if sizes of the nodes in the subtree are consistent
	"""
	def isSizeConsistentRec(self, x):
		# If x is a virtual node return True
		if x == self.getSentinel():
			return True
		# Size of x should be x.left.size + x.right.size + 1
		if x.getSize() != (x.getLeft().getSize() + x.getRight().getSize() + 1):
			return False
		# Recursive calls
		return self.isSizeConsistentRec(x.getLeft()) and self.isSizeConsistentRec(x.getRight())

	"""Checks if heights of the nodes in the tree are consistent

	@rtype: boolean 
	@returns: True if heights of the nodes in the tree are consistent
	"""
	def isHeightConsistent(self):
		return self.isHeightConsistentRec(self.getRoot())

	"""Checks if heights of the nodes in the subtree are consistent

	@type x: AVLNode
	@param x: The root of the subtree
	@rtype: boolean 
	@returns: True if heights of the nodes in the subtree are consistent
	"""
	def isHeightConsistentRec(self, x):
		# If x is a virtual node return True
		if x == self.getSentinel():
			return True
		# Height of x should be maximum of children heights + 1
		if x.getHeight() != max(x.getLeft().getHeight(), x.getRight().getHeight()) + 1:
			return False
		# Recursive calls
		return self.isSizeConsistentRec(x.getLeft()) and self.isSizeConsistentRec(x.getRight())

	"""Checks if the ranks of the nodes in the tree are consistent

	@returns: True if the ranks of the nodes in the tree are consistent
	"""
	def isRankConsistent(self):
		root = self.getRoot()
		for i in range(1, root.getSize()):
			if i != self.rank(self.select(i)):
				return False
		nodesList = self.nodes()
		for node in nodesList:
			if node != self.select(self.rank(node)):
				return False
		return True

	"""Returns a list of the nodes in the tree sorted by index in O(n)

	@rtype: list
	@returns: A list of the nodes in the tree sorted by index
	"""
	def nodes(self):
		lst = []
		self.nodesInOrder(self.getRoot(), lst)
		return lst

	"""Adds the nodes in the subtree to the list
	 following an in-order traversal in O(n)

	@type x: AVLNode
	@type lst: list
	@param x: The root of the subtree
	@param lst: The list
	"""
	def nodesInOrder(self, x, lst):
		if not x.isRealNode():
			return
		self.nodesInOrder(x.getLeft(), lst)
		lst.append(x)
		self.nodesInOrder(x.getRight(), lst)


	###################################################### printree ######################################################
	###################################################### function ######################################################

	def printree(t, bykey=False):
		"""Print a textual representation of t
		bykey=True: show keys instead of values"""
		return trepr(t, t.getRoot(), bykey)


	def trepr(t, node, bykey=False):
		"""Return a list of textual representations of the levels in t
		bykey=True: show keys instead of values"""
		if node == t.getSentinel():  # You might want to change this, depending on your implementation
			return ["#"]    # Hashtag marks a virtual node

		thistr = str(node.getValue())

		return conc(trepr(t, node.getLeft(), bykey), thistr, trepr(t, node.getRight(), bykey))


	def conc(left, root, right):
		"""Return a concatenation of textual representations of
		a root node, its left node, and its right node
		root is a string, and left and right are lists of strings"""

		lwid = len(left[-1])
		rwid = len(right[-1])
		rootwid = len(root)

		result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

		ls = leftspace(left[0])
		rs = rightspace(right[0])
		result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

		for i in range(max(len(left), len(right))):
			row = ""
			if i < len(left):
				row += left[i]
			else:
				row += lwid * " "

			row += (rootwid + 2) * " "

			if i < len(right):
				row += right[i]
			else:
				row += rwid * " "

			result.append(row)

		return result


	def leftspace(row):
		"""helper for conc"""
		# row is the first row of a left node
		# returns the index of where the second whitespace starts
		i = len(row) - 1
		while row[i] == " ":
			i -= 1
		return i + 1


	def rightspace(row):
		"""helper for conc"""
		# row is the first row of a right node
		# returns the index of where the first whitespace ends
		i = 0
		while row[i] == " ":
			i += 1
		return i

	## same methods with different names
	def getSentinel(self):
		return self.isRealNode()














	
##tester
"""""
AVLTreeList1 = AVLTreeList(None, None, None, 0, 0)
print("number of rotations", AVLTreeList1.insert(1,3))
print("-------")
AVLTreeList1.root.printDetails()

print("number of rotations", AVLTreeList1.insert(1,1))
print("-------")
AVLTreeList1.root.printDetails()
AVLTreeList1.root.left.printDetails()

print("number of rotations", AVLTreeList1.insert(2,2))
print("-------")
AVLTreeList1.root.printDetails()
AVLTreeList1.root.left.printDetails()
AVLTreeList1.root.right.printDetails()




AVLTreeList1 = AVLTreeList(None, None, None, 0, 0)
a = AVLTreeList1.empty()
print("Is Empty: ", a)
print("number of rotations: ", AVLTreeList1.insert(1, 1))
AVLTreeList1.root.printDetails()
print("-------")

print("number of rotations", AVLTreeList1.insert(2,2))
AVLTreeList1.root.printDetails()
AVLTreeList1.root.right.printDetails()
print("-------")

print("number of rotations of 3: ", AVLTreeList1.insert(3,3))
AVLTreeList1.root.printDetails()
AVLTreeList1.root.left.printDetails()
AVLTreeList1.root.right.printDetails()
print("-------")

print("number of rotations of 4: ", AVLTreeList1.insert(4,5))
AVLTreeList1.root.printDetails()
AVLTreeList1.root.left.printDetails()
AVLTreeList1.root.right.printDetails()
AVLTreeList1.root.right.right.printDetails()
print("-------")

print("number of rotations of 4: ", AVLTreeList1.insert(4,4))
AVLTreeList1.root.printDetails()
AVLTreeList1.root.left.printDetails()
AVLTreeList1.root.right.printDetails()
AVLTreeList1.root.right.right.printDetails()
AVLTreeList1.root.right.left.printDetails()
print("-------")

print(AVLTreeList1.listToArray())

print(AVLTreeList1.search(3))

"""




AVLTreeList1 = AVLTreeList(None, None, None, 0, 0)
a = AVLTreeList1.empty()
AVLTreeList1.root.printDetails()

AVLTreeList1.root.printDetails()
AVLTreeList1.root.right.printDetails()

AVLTreeList1.root.printDetails()
AVLTreeList1.root.left.printDetails()
AVLTreeList1.root.right.printDetails()

AVLTreeList1.root.printDetails()
AVLTreeList1.root.left.printDetails()
AVLTreeList1.root.right.printDetails()
AVLTreeList1.root.right.right.printDetails()

AVLTreeList1.root.printDetails()
AVLTreeList1.root.left.printDetails()
AVLTreeList1.root.right.printDetails()
AVLTreeList1.root.right.right.printDetails()
AVLTreeList1.root.right.left.printDetails()




tree.check()