import random as r
import time
import sys

class SortedDisplayDict(dict):
   def __str__(self):
       return "{" + ", ".join("%r: %r" % (key, self[key]) for key in sorted(self)) + "}"


class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def show(self):
        print("stack:",self.stack)

    def isempty(self):
        if len(self.stack)<1:
            return True
        else:
            return False

    def returnstack(self):
        return self.stack

    
class Node:
    def __init__(self ,node ,data = None):
        self.node = node
        self.visited = False
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.data = data

class GraphMaker:
    def __init__(self,totalsize):
        #totalsize is assumed to be [row,column]
        self.masterdictionary = {}
        self.currentposition = [0,0]
        if type(totalsize) is list:
            self.totalsize = totalsize
        else:
            self.totalsize = [totalsize,totalsize]
         
        self.masterdictionary[str(self.currentposition)] = Node(self.currentposition, "Start")

        self.listvisualisation = [['#' for i in range(self.totalsize[1])] for l in range(self.totalsize[0])]
        self.listvisualisation[self.currentposition[0]][self.currentposition[1]] = '.' 

    def isdeadend(self, node):
        if str(node) not in self.masterdictionary:
            return "Node doesn't exist"
        else:
            currentnode = self.masterdictionary[str(node)]
            if currentnode.up != None and currentnode.down != None and currentnode.left != None and currentnode.right != None:
                return True
            else:
                return False

    def isempty(self, node):
        if str(node) not in self.masterdictionary:
            return "Node doesn't exist"
        else:
            count = 0

            if self.masterdictionary[str(node)].left != None:
                count += 1
            if self.masterdictionary[str(node)].right != None:
                count += 1
            if self.masterdictionary[str(node)].up != None:
                count += 1
            if self.masterdictionary[str(node)].down != None:
                count += 1

            if count > 1:
                return False
            else:
                return True


    
    def foresight(self, node, direction, level = 1):
##        print('instance')

        
        if str(node) not in self.masterdictionary:
            return False
        else:
            
            left = [node[0],node[1]-1]
            right = [node[0],node[1]+1]
            up = [node[0]-1,node[1]]
            down = [node[0]+1,node[1]]
            
            for i in range(level):
##                print(node,left,right,up,down,i)
                if direction == '0':
                    if (str(left) in self.masterdictionary) or left[1] < 0:
                        return False

                elif direction == '1':
                    if (str(right) in self.masterdictionary) or right[1] >= self.totalsize[1]:
                        return False

                elif direction == '2':
                    if (str(up) in self.masterdictionary) or up[0] < 0:
                        return False

                elif direction == '3':
                    if (str(down) in self.masterdictionary) or down[0] >= self.totalsize[0]:
                        return False

                else:
                    return False

                left = [left[0], left[1]-1]
                right = [right[0], right[1]+1]
                up = [up[0]-1, up[1]]
                down = [down[0]+1, down[1]]
        return True


            

    def insertleft(self, data = None):
        if int(self.currentposition[1]) > 0:
            newposition = [self.currentposition[0],self.currentposition[1]-1]
            if str(newposition) in self.masterdictionary:
                self.masterdictionary[str(self.currentposition)].left =self.masterdictionary[str(newposition)]
                self.masterdictionary[str(newposition)].right = self.masterdictionary[str(self.currentposition)]
            else:
                newnode = Node(newposition, data)
                self.masterdictionary[str(self.currentposition)].left = newnode
                self.masterdictionary[str(newposition)] = newnode
                newnode.right = self.masterdictionary[str(self.currentposition)]

                if str([newposition[0]+1,newposition[1]]) in self.masterdictionary:
                    newnode.down = self.masterdictionary[str([newposition[0]+1,newposition[1]])]
                    self.masterdictionary[str([newposition[0]+1,newposition[1]])].up = newnode
                if str([newposition[0]-1,newposition[1]]) in self.masterdictionary:
                    newnode.up = self.masterdictionary[str([newposition[0]-1,newposition[1]])]
                    self.masterdictionary[str([newposition[0]-1,newposition[1]])].down = newnode
                if str([newposition[0],newposition[1]-1]) in self.masterdictionary:
                    newnode.left = self.masterdictionary[str([newposition[0],newposition[1]-1])]
                    self.masterdictionary[str([newposition[0],newposition[1]-1])].right = newnode
                 
                self.listvisualisation[newposition[0]][newposition[1]] = '.'

            self.currentposition = newposition
        else:
            return ("FailedLeft")
         
    def insertright(self, data = None):
        if int(self.currentposition[1]) < self.totalsize[1]-1:
            newposition = [self.currentposition[0],self.currentposition[1]+1]
            if str(newposition) in self.masterdictionary:
                self.masterdictionary[str(self.currentposition)].right =self.masterdictionary[str(newposition)]
                self.masterdictionary[str(newposition)].left = self.masterdictionary[str(self.currentposition)]
            else:
                newnode = Node(newposition, data)
                self.masterdictionary[str(self.currentposition)].right = newnode
                self.masterdictionary[str(newposition)] = newnode
                newnode.left = self.masterdictionary[str(self.currentposition)]

                if str([newposition[0]+1,newposition[1]]) in self.masterdictionary:
                    newnode.down = self.masterdictionary[str([newposition[0]+1,newposition[1]])]
                    self.masterdictionary[str([newposition[0]+1,newposition[1]])].up = newnode
                if str([newposition[0]-1,newposition[1]]) in self.masterdictionary:
                    newnode.up = self.masterdictionary[str([newposition[0]-1,newposition[1]])]
                    self.masterdictionary[str([newposition[0]-1,newposition[1]])].down = newnode
                if str([newposition[0],newposition[1]+1]) in self.masterdictionary:
                    newnode.right = self.masterdictionary[str([newposition[0],newposition[1]+1])]
                    self.masterdictionary[str([newposition[0],newposition[1]+1])].left = newnode
         
                self.listvisualisation[newposition[0]][newposition[1]] = '.'

            self.currentposition = newposition
        else:
            return ("FailedRight")
            
    def insertup(self, data = None):
        if int(self.currentposition[0]) > 0:
            newposition = [self.currentposition[0]-1,self.currentposition[1]]
            if str(newposition) in self.masterdictionary:
                self.masterdictionary[str(self.currentposition)].up =self.masterdictionary[str(newposition)]
                self.masterdictionary[str(newposition)].down = self.masterdictionary[str(self.currentposition)]
            else:
                newnode = Node(newposition, data)
                self.masterdictionary[str(self.currentposition)].up = newnode
                self.masterdictionary[str(newposition)] = newnode
                newnode.down = self.masterdictionary[str(self.currentposition)]


                if str([newposition[0]-1,newposition[1]]) in self.masterdictionary:
                    newnode.up = self.masterdictionary[str([newposition[0]-1,newposition[1]])]
                    self.masterdictionary[str([newposition[0]-1,newposition[1]])].down = newnode
                if str([newposition[0],newposition[1]-1]) in self.masterdictionary:
                    newnode.left = self.masterdictionary[str([newposition[0],newposition[1]-1])]
                    self.masterdictionary[str([newposition[0],newposition[1]-1])].right = newnode
                if str([newposition[0],newposition[1]+1]) in self.masterdictionary:
                    newnode.right = self.masterdictionary[str([newposition[0],newposition[1]+1])]
                    self.masterdictionary[str([newposition[0],newposition[1]+1])].left = newnode
             
                self.listvisualisation[newposition[0]][newposition[1]] = '.'

            self.currentposition = newposition
        else:
            return ("FailedUp")
         
    def insertdown(self, data = None):
        if int(self.currentposition[0]) < self.totalsize[0]-1:
            newposition = [self.currentposition[0]+1,self.currentposition[1]]
            if str(newposition) in self.masterdictionary:
                self.masterdictionary[str(self.currentposition)].down =self.masterdictionary[str(newposition)]
                self.masterdictionary[str(newposition)].up = self.masterdictionary[str(self.currentposition)]
            else:
                newnode = Node(newposition, data)
                self.masterdictionary[str(self.currentposition)].down = newnode
                self.masterdictionary[str(newposition)] = newnode
                newnode.up = self.masterdictionary[str(self.currentposition)]

                if str([newposition[0]+1,newposition[1]]) in self.masterdictionary:
                    newnode.down = self.masterdictionary[str([newposition[0]+1,newposition[1]])]
                    self.masterdictionary[str([newposition[0]+1,newposition[1]])].up = newnode
                if str([newposition[0],newposition[1]-1]) in self.masterdictionary:
                    newnode.left = self.masterdictionary[str([newposition[0],newposition[1]-1])]
                    self.masterdictionary[str([newposition[0],newposition[1]-1])].right = newnode
                if str([newposition[0],newposition[1]+1]) in self.masterdictionary:
                    newnode.right = self.masterdictionary[str([newposition[0],newposition[1]+1])]
                    self.masterdictionary[str([newposition[0],newposition[1]+1])].left = newnode
             
                self.listvisualisation[newposition[0]][newposition[1]] = '.'

            self.currentposition = newposition
        else:
            return ("FailedDown")


    def visualise(self):
        for item in self.listvisualisation:
            print(item)
    def tofile(self):
        self.f = open("mymaze.txt",'w')
        for item in self.listvisualisation:
            self.f.write(str(item)+"\n")
        self.f.close()

class kroneckers:
    def __new__(self):
        initsize = 2

        initialmatrix = [[0.5 for i in range(initsize)] for i in range(initsize)]
        initialmatrix = [[1,1],[0.5,1]]
        matrix2 = list(initialmatrix)
        

        output = self.kroneckerproduct(self,initsize,initialmatrix,matrix2)
        print(output)
        print(self.cointosser(self,output))
        

    def kroneckerproduct(self, initsize, matrix1, matrix2):
        outputmatrix = []
        for i in range(initsize):
            for j in range(initsize):
                outputsubmatrix = []
                for k in range(initsize):
                    for l in range(initsize):
                        #print(matrix[i][k],matrix2[j][l])
                        outputsubmatrix.append(matrix1[i][k] * matrix2[j][l])
                outputmatrix.append(outputsubmatrix)
        return outputmatrix

    def cointosser(self, matrix):
        output = [[None for item in matrix] for item in matrix]
        print(output)

        for i in range(len(output)):
            for j in range(len(output[i])):
                current = matrix[i][j]
                if output[i][j] != 1:
                    if r.randint(1,100) <= current*100:
                        output[i][j] = 1
                        #output[j][i] = 1
                    else:
                        output[i][j] = 0
        return output
                
                
                    
        

        

        
    
class SimpleRandomGenerator:
    def __new__(self,size):
        Graph = GraphMaker(size)
        self.functions = {'0':Graph.insertleft, '1':Graph.insertright, '2':Graph.insertup, '3':Graph.insertdown}

        self.seed = r.randrange(sys.maxsize)
        r.seed(self.seed)
        print(self.seed)

        while Graph.currentposition!=[Graph.totalsize[0]-1,Graph.totalsize[1]-1]:
            self.randomfunction = r.randint(0,3)
            self.functions[str(self.randomfunction)]()
            self.functions[str(self.randomfunction)]()
        Graph.masterdictionary[str([Graph.totalsize[0]-1,Graph.totalsize[1]-1])].data = 'Finish'

        Graph.visualise()
        return Graph.masterdictionary


class DepthFirstMazeGenerator:
    def __new__(self,size,foresight = 2,seed = r.randrange(sys.maxsize)):
        #print(seed)
        self.timestart = time.time()
        self.Graph = GraphMaker(size)
        self.functions = {'0':self.Graph.insertleft, '1':self.Graph.insertright, '2':self.Graph.insertup, '3':self.Graph.insertdown}
        self.excess = Stack()
        self.largest = [0,0]
        self.previous = None



        r.seed(seed)

        self.count = 0
        self.returned = None

        while self.Graph.currentposition!=[self.Graph.totalsize[0]-1, self.Graph.totalsize[1]-1] and self.count <= (0.5*(size*size)) and self.returned != "StackEmpty":
            self.returned = self.move(self,foresight)
##            print(self.returned)
            if self.returned != "StackEmpty" and self.returned>self.largest:
                self.largest = self.returned
            self.count += 1

        #print(self.returned)
        self.Graph.masterdictionary[str(self.largest)].data = "Finish"
        #self.Graph.visualise()
        self.Graph.tofile()
        self.timestop = time.time()
        #print(self.timestop - self.timestart)
        return self.Graph.masterdictionary

    def move(self, step):
        self.selector = ['0', '1', '2', '3']
        self.current = self.Graph.currentposition
        
##        print("previous", self.previous)

        if self.current[1] > self.Graph.totalsize[1]-step or self.previous == '0' or self.Graph.foresight(self.current, '1',step) == False:
            self.selector.remove('1')
        if self.current[1] < 1 or self.previous == '1' or self.Graph.foresight(self.current, '0',step) == False:
            self.selector.remove('0')
        if self.current[0] > self.Graph.totalsize[0]-step or self.previous == '2' or self.Graph.foresight(self.current, '3',step) == False:
            self.selector.remove('3')
        if self.current[0] < 1 or self.previous == '3' or self.Graph.foresight(self.current, '2',step) == False:
            self.selector.remove('2')

##        print('current selector', self.selector, self.Graph.currentposition)

        if len(self.selector) > 0:
            self.randomfunction = r.randint(0,len(self.selector)-1)
            self.functions[self.selector[self.randomfunction]]()
            self.functions[self.selector[self.randomfunction]]()


            self.previous = self.selector[self.randomfunction]
##            print('moved', self.selector[self.randomfunction])
            del self.selector[self.randomfunction]


##            print('added to stack', self.selector)
            for item in self.selector:
                if item == '0':
                    self.excess.push([self.current,'0'])
                elif item == '1':
                    self.excess.push([self.current,'1'])
                elif item == '2':
                    self.excess.push([self.current,'2'])
                elif item == '3':
                    self.excess.push([self.current,'3'])
                
        else:    
            while True:
                if self.excess.isempty() == True:
                    return "StackEmpty"
##                self.excess.show()
                self.next = self.excess.pop()
                if self.Graph.foresight(self.next[0],self.next[1],step) == False:
                    continue

                else:
                    self.Graph.currentposition = self.next[0]
                    self.functions[self.next[1]]()
                    self.functions[self.next[1]]()
                    break

##            print('from stack',self.next)
            
##        self.Graph.visualise()
##        print('')
        return self.current

class DepthFirstSearch:
    def __init__(self, maze):
        self.timestart = time.time()
        self.maze = maze
        self.stack = Stack()
        
        self.maze[str([0,0])].visited = True

        self.stack.push([0,0])
        self.current = [0,0]
        self.masterlist = []
        self.indexoflastbranch = 0
        self.counter = 0

        while self.maze[str(self.current)].data != "Finish":
            self.counter += 1
            self.pathcount = 0

            self.current = self.stack.pop()
            self.maze[str(self.current)].visited = True

            
            
            if self.maze[str(self.current)].up != None and self.maze[str(self.current)].up.visited == False and self.maze[str(self.current)].up.node not in self.stack.returnstack():
                self.stack.push(self.maze[str(self.current)].up.node)
                self.pathcount += 1
            if self.maze[str(self.current)].down != None and self.maze[str(self.current)].down.visited == False and self.maze[str(self.current)].down.node not in self.stack.returnstack():
                self.stack.push(self.maze[str(self.current)].down.node)
                self.pathcount += 1
            if self.maze[str(self.current)].left != None and self.maze[str(self.current)].left.visited == False and self.maze[str(self.current)].left.node not in self.stack.returnstack():
                self.stack.push(self.maze[str(self.current)].left.node)
                self.pathcount += 1
            if self.maze[str(self.current)].right != None and self.maze[str(self.current)].right.visited == False and self.maze[str(self.current)].right.node not in self.stack.returnstack():
                self.stack.push(self.maze[str(self.current)].right.node)
                self.pathcount += 1

            if self.pathcount > 1:
                self.indexoflastbranch = len(self.masterlist)

            self.masterlist.append(self.current)
            #print(self.current)
            #self.stack.show()

            if self.pathcount < 1:
                self.masterlist = self.masterlist[0:self.indexoflastbranch + 1]
        if self.maze[str(self.current)].data == "Finish":
            self.masterlist.append(self.current)
        
        self.timestop = time.time()


        #print("Depth First Search:")
        #print("length of agent", [len(self.masterlist), "steps taken", self.counter],"\n")
        
    def returned(self):
        return [self.counter]
        
            

        
        


class BreadthFirstSearch:
    def __init__(self, maze):
        self.maze = maze
        self.timestart = time.time()
        self.startnode = self.maze[str([0,0])]
        self.startnode.visited = True

        self.previouscontainer = [self.startnode]
        self.currentcontainer = []
        self.masterlist = [[self.startnode]]
        self.counter = 0
        self.maxflow = 0

        while not(self.isfinish(self.currentcontainer)):
            self.counter += 1
            self.currentcontainer = []

            for nodes in self.previouscontainer:
                if nodes.up != None and nodes.up.visited == False :
                    self.currentcontainer += [nodes.up]
                    nodes.up.visited = True
                if nodes.down != None and nodes.down.visited == False:
                    self.currentcontainer += [nodes.down]
                    nodes.down.visited = True
                if nodes.left != None and nodes.left.visited == False:
                    self.currentcontainer += [nodes.left]
                    nodes.left.visited = True
                if nodes.right != None and nodes.right.visited == False:
                    self.currentcontainer += [nodes.right]
                    nodes.right.visited = True
            self.masterlist += [self.currentcontainer]
            self.previouscontainer = list(self.currentcontainer)
            #print([item.node for item in self.currentcontainer])
            if len(self.currentcontainer) > self.maxflow:
                self.maxflow = len(self.currentcontainer)
        self.x = [item.node for item in self.currentcontainer]
        self.timestop = time.time()


        #print("Breadth First Search:")
        #print("Current Container", [[item.node for item in self.masterlist[-1]], "steps taken", self.counter],"\n")

    def returned(self):
        return [self.counter,self.maxflow]

       
    def isfinish(self, container):
        for item in container:
            if item.data == "Finish":
                return True
        return False
      
      
      
class BreadthLimitedSearch:
    def __init__(self, maze, no_of_agents, detail = False, size = 15):
        self.timestart = time.time()
        self.startnode = maze[str([0,0])]
        self.startnode.visited = True

        self.private = GraphMaker(size)
        self.functions = {'0':self.private.insertleft, '1':self.private.insertright, '2':self.private.insertup, '3':self.private.insertdown}



        self.maze = maze
        self.HiveMind = [[self.startnode.node] for i in range(no_of_agents)]

        self.GroupingMaster = [[i for i in range(no_of_agents)]]

        self.excess = Stack()

        self.counter = 0

        self.found = False

        if detail==True:
            self.PrintAgents(self.HiveMind)        
        #-------------------------------------------------------------
        #This is post check loop, the stopping condition is at the end of the loop with a break
        while True:
            self.counter += 1

            if detail == True:
                print("next step---------------------------------------------------------")
                print("Current Grouping: ",self.GroupingMaster)

            self.currentgroupingmaster = list(self.GroupingMaster)
        #-------------------------------------------------------------
        #the following code creates the container,
        #the container keeps the list of coordinates it can move next according to its current location
            for group in range(len(self.currentgroupingmaster)):
                
                if detail==True:
                    print("next group-----------------------------------------")
                    print("now working on group:",group)

                self.currentcontainer = []

                self.move = self.maze[str(self.HiveMind[self.currentgroupingmaster[group][0]][-1])]
                if self.move.up != None and self.move.up.visited == False:
                    self.currentcontainer += [self.move.up.node]
                    self.move.up.visited = True
                    self.functions['2']()
                if self.move.down != None and self.move.down.visited == False:
                    self.currentcontainer += [self.move.down.node]
                    self.move.down.visited = True
                    self.functions['3']()
                if self.move.left != None and self.move.left.visited == False:
                    self.currentcontainer += [self.move.left.node]
                    self.move.left.visited = True
                    self.functions['0']()
                if self.move.right != None and self.move.right.visited == False:
                    self.currentcontainer += [self.move.right.node]
                    self.move.right.visited = True
                    self.functions['1']()

                if detail==True:
                    print("the current container: ",self.currentcontainer)



                self.finished = self.isfinish(self.currentcontainer)
                if self.finished != False:
                    self.found = True
                    for item in self.currentgroupingmaster[group]:
                        self.HiveMind[item].append(self.finished)

                    for i in range(len(self.HiveMind)):
                        if maze[str(self.HiveMind[i][-1])].data == "Finish":
                            self.success = [i,self.HiveMind[i]]
                            #print(self.success)
                            
                    if detail==True:
                        self.PrintAgents(self.HiveMind)
                    self.timestop = time.time()

                    #BFS = BreadthFirstSearch(self.private.masterdictionary)
                    #print("Breadth Limited Search:")
                    #print(["steps taken: " + str(self.counter+1), "agent: " + str(self.success[0]), "finishing: " + str(self.finished), "EuclideanDistance: " + str((((self.finished[0]+1)**2)+((self.finished[1]+1)**2))**0.5)], self.timestop - self.timestart,"\n")

                    return

                    
                    
        #-------------------------------------------------------------
        #checks if the current group is in a dead end, if so it injects one part of the stack to the container

                if len(self.currentcontainer) == 0 and self.excess.isempty() == False:
                    self.currentcontainer.append(self.excess.pop())

                    if detail==True:
                        print("showing stack:")
                        self.excess.show()
                        print("the new container: ",self.currentcontainer)
        #-------------------------------------------------------------
        #the if else below checks for any path divergence the agents faced
        #if the container has more than one coordinates, it means that the agent has more than one possible path

                if len(self.currentcontainer) > 1:
                    self.currentgroup = self.currentgroupingmaster[group]
                    self.GroupingMaster.remove(self.currentgroup)

                    if detail==True:
                        print("path divergence")

        #-------------------------------------------------------------
        #the if else below determines if there is more agents than path, or vice versa\
                    if len(self.currentcontainer) > len(self.currentgroup):
                        self.newgroup = []

                        if detail==True:
                            print("container is more than agent count")

                        self.newgroup += [[item] for item in self.currentgroup]
                        for agentnumlist in self.newgroup:
                            self.Visited = self.currentcontainer.pop()
                            self.HiveMind[agentnumlist[0]].append(self.Visited)
                        self.GroupingMaster += self.newgroup
                        for i in range(len(self.currentcontainer)):
                            self.excess.push(self.currentcontainer[i])

                        if detail==True:                            
                            print("showing stack:")
                            self.excess.show()

                            print("currentgroup: ",self.currentgroup)
                            print("newgroup: ",self.newgroup)
                            print("GroupingMaster: ",self.GroupingMaster)
                            print("currentgroupingmaster: ",self.currentgroupingmaster)

                        
                    else:
                        self.newgroup = []
                        if detail==True:
                            print("agent count is more than container")

                        self.newgroup += [[] for i in range(len(self.currentcontainer))]
                        for groupindex in range(len(self.currentgroup)):
                            self.newgroup[groupindex%len(self.newgroup)].append(self.currentgroup[groupindex])
                            self.HiveMind[self.currentgroup[groupindex]].append(self.currentcontainer[groupindex%len(self.currentcontainer)])
                        self.GroupingMaster += self.newgroup
                        if detail==True:                            
                            print("currentgroup: ",self.currentgroup)
                            print("newgroup: ",self.newgroup)
                            print("GroupingMaster: ",self.GroupingMaster)
                            print("currentgroupingmaster: ",self.currentgroupingmaster)
                else:
                    if detail==True:
                        print("no path divergence")
                    for agent in self.currentgroupingmaster[group]:
                        
                        for item in self.currentcontainer:
                            self.HiveMind[agent].append(item)


            if detail == True:
                self.PrintAgents(self.HiveMind)
                

    def returned(self):
        #second item in the list is the euclidean distance of the start to finish
        return [self.counter+1,(((self.finished[0]+1)**2)+((self.finished[1]+1)**2))**0.5]

    def isfinish(self,container):
        for item in container:
            if self.maze[str(item)].data == "Finish":
                return item
        return False

    def PrintAgents(self,HiveMind):
        for i in range(len(HiveMind)):
            print("Agent %d: "%i,HiveMind[i])
        print("")



      
      
      
            
def autotest():
    count = 100
    size = 100
    foresight = 2

    fileoutput = open('mazeoutput.csv','w')
    fileoutput.write("DFS Count,BLS Count,BFS Count\n")
    
    for i in range(count):
        outputstring = ""
        printlist = []
        printlisttuple = []
        
        random = r.randrange(sys.maxsize)
        print("Test Case:", i, "  Seed:", random)
        

        maze = DepthFirstMazeGenerator(size = size,foresight = foresight,seed = random)
        DFS = DepthFirstSearch(maze)
        DFSOutput = DFS.returned()[0]
        printlisttuple.append("DFS")
        printlisttuple.append(DFSOutput)
        printlist.append(printlisttuple)
        outputstring += str(DFSOutput) + ","

        maze = DepthFirstMazeGenerator(size = size,foresight = foresight,seed = random)
        BFS = BreadthFirstSearch(maze)
        BFSOutput = BFS.returned()[0]
        
        maxflow = BFS.returned()[1]

        BLSProportion = []

        for i in range(1,maxflow+1,1):
            printlisttuple = []
            maze = DepthFirstMazeGenerator(size = size,foresight = foresight,seed = random)
            BLS = BreadthLimitedSearch(maze,i)
            BLSOutput = BLS.returned()
            printlisttuple.append("BLS"+str(i))
            printlisttuple.append(BLSOutput[0])
            BLSProportion.append(BLSOutput[0])
            printlist.append(printlisttuple)
            outputstring += str(BLSOutput[0]) + ","

        printlisttuple = []
        euclideandistance = BLSOutput[1]
        

        printlisttuple.append("BFS")
        printlisttuple.append(BFSOutput)
        printlist.append(printlisttuple)
        outputstring += str(BFSOutput) + ","
        
        printlisttuple = []
        printlisttuple.append("MaxFlow")
        printlisttuple.append(maxflow)
        printlist.append(printlisttuple)
        printlisttuple = []
        printlisttuple.append("EuclideansDistance")
        printlisttuple.append(euclideandistance)
        printlist.append(printlisttuple)
        
##        for item in printlist:
##            print(item)
##        fileoutput.write(outputstring+"\n")

        proportion = []
        print(BLSProportion)
        for i in range(1,len(BLSProportion)):
            proportion.append(str("BLS"+str(i+1)+": ")+str(((BLSProportion[i-1]/BLSProportion[i])*100)-100)+"% more efficient than previous number of agent")
        for item in proportion:
            print(item)
        
        print("-----------------------------------------------------------------------------------------------------------")
        
    fileoutput.close()

autotest()


