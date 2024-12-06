class ToDo:
  def __init__(self, id, title, progress, deadline, description):
    self.__id = id
    self.__title = title
    self.__progress = progress
    self.__deadline = deadline
    self.__description = description
    self.__pinned = False

  def setId(self, id):
    self.__id = id

  def getId(self):
    return self.__id
  
  def setTitle(self, title):
    self.__title = title

  def getTitle(self):
    return self.__title
  
  def setProgress(self, progress):
    self.__progress = progress

  def getProgress(self):
    return self.__progress
  
  def setDeadline(self, deadline):
    self.__deadline = deadline

  def getDeadline(self):
    return self.__deadline
  
  def setDescription(self, description):
    self.__description = description

  def getDescription(self):
    return self.__description
  
  def getPin(self):
    return self.__pinned
  
  def setPin(self):
    if self.__pinned == False:
      self.__pinned = True
    else:
      self.__pinned = False

  def toString(self):
    pass

  def generateFile(self):
    #use id as file name
    pass

  def readFile(self):
    pass

  def deleteFile(self):
    pass
