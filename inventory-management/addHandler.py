class AddHandler():
    def __init__(self) -> None:
        self.newItem = dict()
        # Store functions to be accessed from CLI
        self.commands = dict()
        self.commands['0'] = self.addCabinet
        self.commands['1'] = self.addTray
        self.commands['2'] = self.addSlot
        self.commands['3'] = self.addCategory
        self.commands['4'] = self.addIdentifier
        self.commands['5'] = self.addDescription
        self.commands['6'] = self.addQuantity
        self.commands['7'] = self.addManufacturer
        self.commands['8'] = self.addMPN
        self.commands['a'] = None
        self.commands['q'] = None
    
    def addCabinet(self):
        self.newItem['Cabinet'] = input('Please enter the Cabinet #: ')

    def addTray(self):
        self.newItem['Tray'] = input('Please enter the Tray #: ').upper()

    def addSlot(self):
        self.newItem['Slot'] = input('Please enter the Slot #: ')

    def addCategory(self):
        self.newItem['Category'] = input('Please enter the Category: ').upper()

    def addIdentifier(self):
        self.newItem['Identifier'] = input('Please enter the Identifier: ').upper()
    
    def addDescription(self):
        self.newItem['Description'] = input('Please enter the Description: ').upper()

    def addQuantity(self):
        self.newItem['Quantity'] = input('Please enter the Quantity: ')

    def addManufacturer(self):
        self.newItem['Manufacturer'] = input('Please enter the Manufacturer: ').upper()
    
    def addMPN(self):
        self.newItem['MPN'] = input('Please scan the MPN barcode: ').upper()
    
    # Remove empty info
    def checkInfo(self):
        self.newItem = {k: v for k, v in self.newItem.items() if v}

