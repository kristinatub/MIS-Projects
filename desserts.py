class Desserts:
    #define attributes
    def __init__(self,start_name,start_kind):
        self.__start_name=''
        self.__start_kind=''
    #return name
    def get_name(self):
        return self.__name
    #return kind
    def get_kind(self):
        return self.__kind
    #print all
    def __str__(self):
        var= (str(self.__start_name)+str(self.__start_kind))
        return var


