class Insert:   
    def one(self):
        print('insert one')
    
    def many(self):
        print('insert MANY')

class Select():
    def one(self):
        print('select one')
    
    def many(self):
        print('select MANY')

class Repertory:
    def __init__(self) -> None:
        self.__insert = Insert()
        self.__select = Select()

    def r_select_one(self):
        self.__select.one()

call = Repertory()
call.r_select_one()