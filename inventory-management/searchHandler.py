class SearchHandler():
    def __init__(self):
        self.criteria = dict()
        # Store functions to be accessed from CLI
        self.commands = dict()
        self.commands['0'] = self.searchById
        self.commands['1'] = self.searchByCabinet
        self.commands['2'] = self.searchByTray
        self.commands['3'] = self.searchBySlot
        self.commands['4'] = self.searchByCategory
        self.commands['5'] = self.searchByIdentifier
        self.commands['6'] = self.searchByQuantity
        self.commands['7'] = self.searchByAvailability
        self.commands['8'] = self.searchByManufacturer
        self.commands['9'] = self.searchByMPN
        self.commands['s'] = None
        self.commands['q'] = None

    def searchById(self):
        self.criteria['ID'] = input('Please enter the ID: ')
    
    def searchByCabinet(self):
        self.criteria['Cabinet'] = input('Please enter the Cabinet #: ')

    def searchByTray(self):
        self.criteria['Tray'] = input('Please enter the Tray #: ').upper()

    def searchBySlot(self):
        self.criteria['Slot'] = input('Please enter the Slot #: ')

    def searchByCategory(self):
        self.criteria['Category'] = input('Please enter the Category: ').upper()

    def searchByIdentifier(self):
        self.criteria['Identifier'] = input('Please enter the Identifier: ').upper()

    def searchByQuantity(self):
        self.criteria['Quantity'] = input('Please enter the Quantity: ')

    def searchByAvailability(self):
        if 'Availability' not in self.criteria:
            self.criteria['Availability'] = True
        else:
            self.criteria['Availability'] = not self.criteria['Availability']

    def searchByManufacturer(self):
        self.criteria['Manufacturer'] = input('Please enter the Manufacturer: ').upper()
    
    def searchByMPN(self):
        self.criteria['MPN'] = input('Please scan the MPN barcode: ').upper()
    
    # Remove empty search terms
    def checkInfo(self):
        self.criteria = {k: v for k, v in self.criteria.items() if v}
    
    def startSearching(self):
        # Init query
        self.query = 'SELECT * FROM Items WHERE'
        
        # Add the criteria
        if not self.criteria: # No condition
            self.query = self.query[:20]
        else:
            for key, value in self.criteria.items():
                if key == 'Availability':
                    # Remove '' for boolean value
                    self.query += f''' {key} = {value} and'''
                else:
                    self.query += f''' {key} = '{value}' and'''

            # Remove the last 'and' keyword from the query
            self.query = self.query[:-4]
            
            # Reset criteria
            self.criteria = dict()
