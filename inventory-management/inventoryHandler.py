import pyodbc
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 180)

class InventoryHandler():
    def __init__(self):
        pass
    
    def initConn(self):
        try:
            self.conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                            r'DBQ=/path/to/INVENTORY_DB.accdb;')
            self.cursor = self.conn.cursor()
            return True
        except Exception as e:
            # print(e)
            print('Cannot connect to database')
            return False

    def searchQuery(self, query):
        if not self.initConn():
            return
        
        try:
            data = pd.read_sql(query, self.conn)

            if data.empty:
                print('No matched record')
                return
            
            data = data[['ID', 'Cabinet', 'Tray', 'Slot', 'Category', 'Identifier', 'Description', 'Quantity',
                        'Availability', 'Manufacturer', 'MPN']]
            print(data)
        except Exception as e:
            print('An error occured while searching')
            # print(e)
        finally:
            self.cursor.close()
            self.conn.close()
    
    # boolean use: True (borrow), False (return)
    def useOrReturnQuery(self, itemMPN, use, reuse=True):
        if not self.initConn():
            return False
        
        try:
            # Check item's availability
            query = f'''SELECT Availability 
                        FROM Items 
                        WHERE MPN = '{itemMPN}' '''
            self.cursor.execute(query)

            # No item with the given MPN
            records = self.cursor.fetchall()

            if len(records) == 0:
                print('The item with this barcode does not exist')
                return False

            for record in records:
                if record.Availability == False and use == True:
                    print('The item is already in use')
                    return False
                elif record.Availability == True and use == False:
                    print('The item has not been used')
                    return False

            # Update the item's availability
            # Search by MPN (barcode)

            # TODO: Should use the ID as the barcode instead of MPN
            # Keep 'Availability' to False if the item cannot be reused
            if reuse:
                query = f'''UPDATE Items 
                            SET Availability = {not use} 
                            WHERE MPN = '{itemMPN}' '''
                self.cursor.execute(query)
                self.conn.commit()
            
            # Return the updated version
            query = f'''SELECT * 
                        FROM Items 
                        WHERE MPN = '{itemMPN}' '''
            data = pd.read_sql(query, self.conn)
            data = data[['ID', 'Cabinet', 'Tray', 'Slot', 'Category', 'Identifier', 'Description', 'Quantity',
                        'Availability', 'Manufacturer', 'MPN']]
            print(data)
            return True
        except Exception as e:
            print('An error occured while updating the item\'s availability')
            # print(e)
            return False
        finally:
            self.cursor.close()
            self.conn.close
    
    def addQuery(self, item):
        if not self.initConn():
            return False

        try:
            query = f'''INSERT into Items
                        (Cabinet, Tray, Slot, Category, Identifier, Description, Quantity, Manufacturer, MPN)
                        values ('{item['Cabinet']}', '{item['Tray']}', '{item['Slot']}', '{item['Category']}', '{item['Identifier']}', 
                            '{item['Description']}', '{item['Quantity']}', '{item['Manufacturer']}', '{item['MPN']}')'''
            self.cursor.execute(query)
            self.conn.commit()
            return True
        except Exception as e:
            print('An error occured while inserting the item')
            # print(e)
            return False
        finally:
            self.cursor.close()
            self.conn.close()
    
    def removeQuery(self, itemMPN):
        if not self.initConn():
            return False

        try:
            # Check item's availability
            query = f'''SELECT Availability 
                        FROM Items 
                        WHERE MPN = '{itemMPN}' '''
            self.cursor.execute(query)

            # No item with the given MPN
            records = self.cursor.fetchall()

            if len(records) == 0:
                print('The item with this barcode does not exist')
                return False

            for record in records:
                if record.Availability == False:
                    print('The item is in use. Please return the item before removing')
                    return False

            # Remove the item
            query = f'''DELETE * 
                        FROM Items
                        WHERE MPN = '{itemMPN}' '''
            self.cursor.execute(query)
            self.conn.commit()
            return True
        except Exception as e:
            print('An error occured while removing the item')
            # print(e)
            return False
        finally:
            self.cursor.close()
            self.conn.close()
