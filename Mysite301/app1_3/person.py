class Person():
    def __init__(self, pid, fullname, contactaddress):
        self.pid=pid
        self.fullname=fullname
        self.contactaddress=contactaddress

    # Getters
    def getPid(self):
        return self.pid

    def getFullName(self):
        return self.fullname

    def getContactAddress(self):
        return self.contactaddress

    # Setters
    def setPid(self, pid):
        self.pid=pid

    def setFullName(self, fullname):
        self.fullname=fullname

    def setContactAddress(self, contactaddress):
        self.contactaddress=contactaddress

    def __str__(self):
        return str(self.pid)+", "+self.fullname+", "+self.contactaddress