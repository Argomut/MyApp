########## Class for To-Do List Manager Module (Elden) #########


import os

class ToDo:
  #Static variables
  __next_id = 0
  __max_id = 0
  __toDoList = []

  #Constructor
  def __init__(self, title="Untitled", progress=0, deadline="None", description="", existing=False):
    self.__id =self.getNextId()
    self.__title = title
    self.__progress = progress
    self.__deadline = deadline
    self.__description = description
    self.__pinned = "False"
    self.incNextId()
    if not existing:
      self.generateFile()
      self.__toDoList.append(self)
     
      
  #Getters and Setters
  def getId(self):
    return self.__id

  def setId(self, id):
    self.__id = id
  

  def getTitle(self):
    return self.__title
  
  def setTitle(self, title):
    self.__title = title
    self.generateFile()

  
  def getProgress(self):
    return self.__progress
  
  def setProgress(self, progress):
    try:
      progress = round(float(progress))
    except:
      return False
    else: 
      self.__progress = min(100,max(0,progress))
      self.generateFile()
      return True

  
  def getDeadline(self):
    return self.__deadline
  
  def setDeadline(self, deadline):
    self.__deadline = deadline
    self.generateFile()

  
  def getDescription(self):
    return self.__description
  
  def setDescription(self, description):
    self.__description = description
    self.generateFile()

  
  def getPin(self):
    return self.__pinned
  
  def setPin(self, pin):
    self.__pinned = pin
    self.generateFile()
  

  #Other Methods
  def togglePin(self):
    if self.getPin() == "False": self.setPin("True")
    else: self.setPin("False")

  #Used in file creation
  def toString(self):
    return ("{}\n{}\n{}\n{}\n{}\n{}".format(self.getId(), self.getTitle(), self.getProgress(), self.getDeadline(), self.getPin(), self.getDescription()))
  
  #Used for testing
  def __repr__(self):
    return "ToDo({},{},{},{},{},{})".format(self.getId(), self.getTitle(), self.getProgress(), self.getDeadline(), self.getPin(), self.getDescription())

  #Find file using Id
  def getFile(self, id):
    return("ToDoFiles//ToDo{}.txt".format(id))
  
  # def getFile(self):
  #   return("ToDoFiles//ToDo{}.txt".format(self.getId()))

  #File creation/overwrite
  def generateFile(self):
    try:
      file = open(self.getFile(self.getId()), "w")
      file.write(self.toString())
      file.close()
    except:
      print("Error creating file")

  #Assigning values of the files to the object
  def readFile(self, id):
    try:
      file = open(self.getFile(id), "r")
      self.setId(file.readline().strip())
      self.setTitle(file.readline().strip())
      self.setProgress(file.readline().strip())
      self.setDeadline(file.readline().strip())
      self.setPin(file.readline().strip())
      self.setDescription(file.read().strip())
      file.close()
    except:
      print("Error reading file")


  #Deleting file and removing from list
  def deleteFile(self):
    try:
      self.__toDoList.remove(self)
      if os.path.exists(self.getFile(self.getId())):
        os.remove(self.getFile(self.getId()))
      else:
        print("File has already been removed")
    except:
      print("Error removing file")
  
  #class methods
  @classmethod
  def setNextId(cls, next_id):
    cls.__next_id = next_id
    try:
      file = open("ToDoFiles//ToDoConfig.txt", "w")
      file.write(cls.__next_id)
    except:
      print("Error writing file")
    file.close()

  #Next Id increment
  @classmethod
  def incNextId(cls):
    cls.__next_id = int(cls.__next_id) + 1
    cls.setNextId(str(cls.__next_id))
  
  @classmethod
  def getNextId(cls):
    try:
      file = open("ToDoFiles//ToDoConfig.txt", "r")
      cls.__next_id = file.read().strip()
      try: int(cls.__next_id)
      except: cls.__next_id = "1"
      else: 
        if cls.__next_id < 1:
          cls.__next_id = "1"
    except:
      cls.__next_id = 1
      file = open("ToDoFiles//ToDoConfig.txt", "w")
      file.write(str(cls.__next_id))
    while os.path.exists("ToDoFiles//ToDo{}.txt".format(cls.__next_id)):
      cls.incNextId()
    file.close()
    return cls.__next_id

  #Recovery in case folder and files were deleted or modified
  @classmethod
  def fixConfig(cls):
    if not os.path.exists("ToDoFiles"): os.makedirs("ToDoFiles", exist_ok=True)
    fixing_range = 10000
    for x in range(int(cls.getNextId()) + fixing_range, 0, -1):
      if os.path.exists("ToDoFiles//ToDo{}.txt".format(x)):
        cls.__max_id = str(x)
        break

  @classmethod
  def initialiseToDoList(cls):
    # del cls.__toDoList[-1]
    cls.fixConfig()
    for x in range(int(cls.__max_id)+1):
      if os.path.exists("ToDoFiles//ToDo{}.txt".format(x)):
        obj = ToDo(existing=True)
        obj.readFile(x)
        cls.__toDoList.append(obj)

  #Sorting so that earlier deadlines are displayed first
  @classmethod
  def sortToDoList(cls):
    cls.__toDoList.sort(key=lambda todo: (todo.__deadline, todo.__pinned))

  @classmethod
  def getToDoList(cls):
    cls.sortToDoList()
    return cls.__toDoList

  #Search function to filter results
  @classmethod
  def searchToDoList(cls, search):
    pinnedSearchList = []
    unpinnedSearchList = []
    for x in cls.getToDoList():
      if search.upper().strip() in x.getTitle().upper().strip():
        if (x.getPin() == "False"):
          unpinnedSearchList.append(x)
        else:
          pinnedSearchList.append(x)
    pinnedSearchList.extend(unpinnedSearchList)
    return pinnedSearchList
