import warnings

from common import *
from inventoryHandler import *
from commandHandler import *

warnings.resetwarnings()
warnings.simplefilter('ignore', UserWarning)


def main():
    # Init database handler
    itemsDb = InventoryHandler()

    # Init command handler
    commandHandler = CommandHandler(itemsDb)
    
    # Prompting
    while True:
        print(main_menu)

        while True:
            command = input('Please select the command: ')

            if command in commandHandler.commands:
                break
            else:
                print('Unrecognized command\n')
        
        commandHandler.commands[command]()

if __name__ == '__main__':
    main()