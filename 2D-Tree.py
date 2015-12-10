"""
@author - Christopher Silva
@date -  12/10/2015
@description - 4553 Final Exam
"""
import random

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.level = None

    def __repr__(self):
        return "< Key=%s Parent=%s Level=%s>" % (self.key,self.p, self.level)

    def __str__(self):
        return "< Key=%s Parent=%s Level=%s>" % (self.key,self.p, self.level)

class KDTree:
    def __init__(self, dimensions):
        self.root = None
        self.dim = dimensions

    def length(self):
        return self.size

    def inorder(self, node):
        if node == None:
            return None
        else:
            self.inorder(node.left)
            print node.key,
            self.inorder(node.right)

    def search(self, values):
        disc = 0
        node = self.root
        while node != None:
            print 'Looking at', node
            if node.key == values:
                return node
            if node.key[disc] > values[disc]:
                node = node.left
            else:
                node = node.right
            disc = (disc+1)%self.dim
        return None

    def minimum(self, node):
        x = None
        while node.left != None:
            x = node.left
            node = node.left
        return x

    def maximum(self, node):
        x = None
        while node.right != None:
            x = node.right
            node = node.right
        return x

    def successor(self, node):
        parent = None
        if node.right != None:
            return self.minimum(node.right)
        parent = node.p
        while parent != None and node == parent.right:
            node = parent
            parent = parent.p
        return parent

    def predecessor(self, node):
        parent = None
        if node.left != None:
            return self.maximum(node.left)
        parent = node.p
        while parent != None and node == parent.left:
            node = parent
            parent = parent.p
        return parent

    def insert(self, values):
        level = 0
        disc = 0
        t = TreeNode(values)
        parent = None
        node = self.root
        while node != None:
            parent = node
            if node.key[disc] > t.key[disc]:
                node = node.left
            elif node.key[disc] < t.key[disc]:
                node = node.right
            else:
                print 'Node already in the tree'
            if node == None:
                disc = (disc+1)%self.dim
            level+=1
        t.level = level
        t.p = parent
        if parent == None:
            self.root = t
        elif t.key[disc] < parent.key[disc]:
            parent.left = t
        else:
            parent.right = t
        return t


    def delete(self, node):
        if node.left == None:
            self.transplant(node, node.right)
        elif node.right == None:
            self.transplant(node, node.left)
        else:
            succ = self.minimum(node.right)
            if succ.p != node:
                self.transplant(succ, succ.right)
                succ.right = node.right
                succ.right.p = succ
            self.transplant(node, succ)
            succ.left = node.left
            succ.left.p = succ

    def transplant(self, node, newnode):
        if node.p == None:
            self.root = newnode
        elif node == node.p.left:
            node.p.left = newnode
        else:
            node.p.right = newnode
        if newnode != None:
            newnode.p = node.p

if __name__ == "__main__":

    insertvals = ([11,11],[22,22],[33,33],[44,44],[55,55],[66,66],[77,77],[88,88],[99,99],[100,100])
    K = KDTree(2)
    for i in range(10):
        K.insert([random.randint(1,100), random.randint(1,100)])
    for value in insertvals:
        K.insert(value)
    search = K.search([100,100])
    if search:
        print 'Found it!', search
    else:
        print "Didn't find it"
    """If I wanted to insert pairs of numbers"""
    """
    for i in range(10):
        for j in range(10):
            r1 = random.randint(1,100)
            r2 = random.randint(1,100)
            B.insert([r1,r2])
            print (r1,r2)
   """
