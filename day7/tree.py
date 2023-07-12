class Node:
    def __init__(self, parentDir, dirName):
        self.size = 0
        self.parentDir = parentDir
        self.childrenDirs = []
        self.files = {}
        self.name = dirName

    def get_size(self):
        return self.size

    def inc_size(self, size):
        self.size += size

    def get_parent(self):
        return self.parentDir

    def add_child(self, child):
        self.childrenDirs.append(child)

    def get_name(self):
        return self.name

    def add_file(self, file_size, name):
        self.files[name] = file_size
