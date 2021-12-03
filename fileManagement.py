import os
from os import walk

class DirectoryManager:

    def __init__(self, dirPath):
        self.dirPath = dirPath
        self.allFiles = []
        self.allDirectories = []
        for (dirpath, dirnames, filenames) in walk(dirPath):
            self.allFiles.extend(filenames)
            self.allDirectories.extend(dirnames)
            break

    def getFilesAndDirectories(self):
        return { "Directories": self.allDirectories, "Files": self.allFiles}


class FileManager():

    def __init__(self, filePath):
        self.directoryPath = None
        if not filePath.startswith('/'):
            filePath = '/' + filePath
        self.filePath = filePath
        if os.path.isdir(self.filePath):
            self.directoryPath = DirectoryManager(self.filePath)

    def isDirectory(self):
        return self.directoryPath is not None

    def getFileList(self):
        if self.isDirectory():
            return (self.directoryPath.getFilesAndDirectories(), True)
        else:
            return ("{}  is not directory".format(self.filePath), False)

    def readData(self):
        try:
            with open(self.filePath,"r") as current_file:
                return ( { "File_Content" : current_file.read() }, True)
        except Exception as e:
            return (str(e.strerror), False)

    def writeDate(self, data):
        try:
            with open(self.filePath,"w") as current_file:
                current_file.write(data)
                return ( "File content updated.".format(self.filePath), True)
        except Exception as e:
            return (str(e.strerror), False)

    def createFile(self):
        try:
            new_file = open(self.filePath, 'x')
            new_file.close()
            return ( "The file {} Created.".format(self.filePath), True)
        except Exception as e:
            return (str(e.strerror), False)

    def deleteFile(self):
        try:
            os.remove(self.filePath)
            return ( "The file {} removed.".format(self.filePath), True)
        except Exception as e:
            return (str(e.strerror), False)