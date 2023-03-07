import sys

from common import *
from searchHandler import *
from addHandler import *

class CommandHandler():
    def __init__(self, itemsDb):
        self.itemsDb = itemsDb

        # Store functions to be accessed from CLI
        self.commands = dict()
        self.commands['s'] = self.searchItems
        self.commands['u'] = self.useItem
        self.commands['r'] = self.returnItem
        self.commands['a'] = self.addItem
        self.commands['d'] = self.removeItem
        self.commands['q'] = self.quitProg
        
        # Init function handlers
        self.searchHandler = SearchHandler()
        self.addHandler = AddHandler()
    
    def searchItems(self):
        # Prompting
        while True:
            print(search_menu)
            self.searchHandler.checkInfo()
            print('Search input:', self.searchHandler.criteria)
            command = input('Please select the search command: ')

            if command in self.searchHandler.commands:
                if command.upper() == 'S': # Start searching
                    self.searchHandler.startSearching()
                    print('\nResult:')
                    self.itemsDb.searchQuery(self.searchHandler.query)
                    break

                if command.upper() == 'Q': # Go back to main menu
                    return
                
                self.searchHandler.commands[command]()
            else:
                print('Unrecognized option')

        while True:
            cont = input('\nQuit program? (Y|N): ')

            if cont.upper() == 'N':
                return
            elif cont.upper() == 'Y':
                self.quitProg()
            
            print('Unrecognized option\n')

        
    def useItem(self):
        # Prompting
        print('\nUse an specific item from NTI inventory')
        print('\tPress q to go back to main menu\n')

        # TODO: Should use the ID as the barcode instead of MPN
        userInput = input('Please scan the barcode of the item you want to use: ')

        if userInput.upper() == 'Q': # Go back to main menu
                return

        else:
            if self.itemsDb.useOrReturnQuery(use=True, itemMPN=userInput):
                print('The item is updated and ready to use')
            else:
                print('Cannot use this item at the moment')

        while True:
            cont = input('\nQuit program? (Y|N): ')

            if cont.upper() == 'N':
                return
            elif cont.upper() == 'Y':
                self.quitProg()
            
            print('Unrecognized option\n')

    def returnItem(self):
        # Prompting
        print('\nReturn an specific item to NTI inventory')
        print('\tPress q to go back to main menu\n')

        # TODO: Should use the ID as the barcode instead of MPN
        itemMPN = input('Please scan the barcode of the item you want to return: ')
        if itemMPN.upper() == 'Q': # Go back to main menu
                return

        else:
            while True:
                itemReuse = input('\nIs the item still reusable? (Y|N): ')
                if itemReuse.upper() == 'Y':
                    itemReuse = True
                    break
                elif itemReuse.upper() == 'N':
                    itemReuse = False
                    break
                elif itemReuse.upper() == 'Q':
                    return

            print('Unrecognized option\n')

            if self.itemsDb.useOrReturnQuery(itemMPN=itemMPN, use=False, reuse=itemReuse):
                print('The item is updated. Please put the item in the correct location')
            else:
                print('Cannot return this item at the moment')

        while True:
            cont = input('\nQuit program? (Y|N): ')
            
            if cont.upper() == 'N':
                return
            elif cont.upper() == 'Y':
                self.quitProg()
            
            print('Unrecognized option\n')

    def addItem(self):
        # Prompting
        while True:
            print(add_menu)
            self.addHandler.checkInfo()
            print('New item:', self.addHandler.newItem)
            command = input('Please insert the information of the new item: ')

            if command in self.addHandler.commands:
                if command.upper() == 'A': # Add the item to database
                    if len(self.addHandler.newItem) == 9:
                        if self.itemsDb.addQuery(self.addHandler.newItem):
                            print('New item is added')
                        else:
                            print('Cannot add this item at the moment')

                        break
                        
                    print('Not enough information. Please add more')
                    continue

                if command.upper() == 'Q': # Go back to main menu
                    return
                
                self.addHandler.commands[command]()
            else:
                print('Unrecognized option')

        while True:
            cont = input('\nQuit program? (Y|N): ')

            if cont.upper() == 'N':
                return
            elif cont.upper() == 'Y':
                self.quitProg()
            
            print('Unrecognized option\n')

    def removeItem(self):
        # Prompting
        print('\nRemove an specific item from NTI inventory')
        print('\tPress q to go back to main menu\n')

        # TODO: Should use the ID as the barcode instead of MPN
        userInput = input('Please scan the barcode of the item you want to remove: ')

        if userInput.upper() == 'Q': # Go back to main menu
                return

        else:
            if self.itemsDb.removeQuery(itemMPN=userInput):
                print('The item is removed')
            else:
                print('Cannot remove this item at the moment')
        
        while True:
            cont = input('\nQuit program? (Y|N): ')

            if cont.upper() == 'N':
                return
            elif cont.upper() == 'Y':
                self.quitProg()
            
            print('Unrecognized option\n')

    def quitProg(self):
        sys.exit()