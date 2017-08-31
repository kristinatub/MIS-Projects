#constants
NUMBER_OF_MINUTES_ALLOWED=500
NUMBER_OF_TEXTS_ALLOWED=100
CHARGE_PER_MINUTE=.25
CHARGE_PER_TEXT=.2
MONTHLY_PLAN_RATE=79.95
TAX_RATE=.08255
#create class
class CellPhoneUsage:
    
    #init definition
    def __init__(self):
        
        self.__account_num=''
        self.__account_name=''
        self.__minutes_used=0
        self.__texts_sent=0
        
    #accessor for account num
    def get_account_num(self):
        return self.__account_num
    
    #mutator for account num
    def set_account_num(self, new_account_num):
        self.__account_num=new_account_num
        
    # accessor for account name      
    def get_account_name(self):
        return self.__account_name
    
    #mutator for account name
    def set_account_name(self,name):
        self.__account_name=name
        
    #access for minutes used
    def get_minutes_used(self):
        return self.__minutes_used
    
    #mutator for make_call
    def make_call(self, new_minutes):
        #validate minutes
        if new_minutes>0:
            self.__minutes_used+=new_minutes
            return True
        
        else:
            print("Invalid amount of minutes")
            return False
        
    #access for get_texts_sent
    def get_texts_sent(self):
        return self.__texts_sent
    
    #mutator for send_texts
    def send_texts(self, new_texts_sent):
        if new_texts_sent>0:
            self.__texts_sent+=new_texts_sent
            return True
        else:
            print("Invalid number")
            return False
        
    #calculate minutes charged        
    def calculate_minutes_charge(self):
        if self.__minutes_used>NUMBER_OF_MINUTES_ALLOWED:
            phone_charge=.25*(self.__minutes_used-NUMBER_OF_MINUTES_ALLOWED)
        else:
            phone_charge=0
        return phone_charge
    
    #calculate texts_charge
    def calculate_texts_charge(self):
        if self.__texts_sent>NUMBER_OF_TEXTS_ALLOWED:
            text_charge=.2*(self.__texts_sent-NUMBER_OF_TEXTS_ALLOWED)
        else:
            text_charge=0
        return text_charge
    
    #calculate_total
    def calculate_total(self):
        minutes=self.calculate_minutes_charge()
        texts=self.calculate_texts_charge()
        total=texts+minutes+MONTHLY_PLAN_RATE
        return total
    
    #def display_bill
    def display_bill(self):
        
        #calculate everything
        text_charge = self.calculate_texts_charge()
        phone_charge = self.calculate_minutes_charge()
        total = self.calculate_total()
        tax = total * TAX_RATE
        total_with_tax = tax + total
        
        #print all necessary info
        print("Bill Displayed")
        print("Account Number: ",self.__account_num)
        print("Account Name: ", self.__account_name)
        print("Minutes Allowed: ",NUMBER_OF_MINUTES_ALLOWED)
        print("Minutes Used: ",self.__minutes_used)
        print("Minutes overage charge: $", format(phone_charge, '.2f'),sep='')
        print("Texts allowed: ",NUMBER_OF_TEXTS_ALLOWED)
        print("Texts used: ",self.__texts_sent)
        print("Texts overage charge: $", format(text_charge,'.2f'),sep='')
        print("Total charge(before tax): $", format(total,'.2f'),sep='')
        print("tax amount: $", format(tax,'.2f'),sep='')
        print("total due(total charge and tax amount): $", format(total_with_tax,'.2f'),sep='')

    # define str for all attributes
    def __str__(self):
        var = self.__account_name+' '+'Account number: ' + self.__account_num +' '+ 'sent ' + str(self.__texts_sent) + ' texts and used ' +  str(self.__minutes_used) + ' minutes.'
        return var


