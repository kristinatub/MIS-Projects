#Author: Kristina Tubera
#Homework Number & Name: Homework 6
#Due Date:3/20/2017
#Program Description:List and Tuples Homework

#DECLARE CONSTANTS
DONOR_DATA="DonorData.txt"
DONOR_SUMMARY_DATA="DonorSummaryData.txt"
#def main
def main():
        try:
            #open files
            donor_input=open(DONOR_DATA,'r')
            donor_output=open(DONOR_SUMMARY_DATA, 'w')
            #create lists

            donor_names=[]
            personal_donor_donations=[]
            donation_matching_codes=[]
            donation_matching_amount=[]
            total_donation=[]

            name=donor_input.readline().rstrip('\n')
            #while loop to put data into list
            while name!='':
                
                donor_names.append(name)
                
                
                personal_donation=donor_input.readline().rstrip('\n')
                personal_donor_donations.append(int(personal_donation))
                                                
                donation_code=donor_input.readline().rstrip('\n')
                donation_matching_codes.append(donation_code)
                
                
                name=donor_input.readline().rstrip('\n')
            
                                                                
            all_calculations=calculate_employer_donation_match(personal_donor_donations,donation_matching_codes)
            get_total_benefit= calculate_total_donation(personal_donor_donations,all_calculations,total_donation)
            
            get_total_personal=calculate_total_values(personal_donor_donations)
            get_total_matched=calculate_total_values(donation_matching_amount)
            
              #print all                                              
            print_donor_names(donor_output,donor_names,get_total_benefit,total_donation)
            print("Number of Donors processed:",len(donor_names))
            print("Total personal donations $", (format(get_total_personal,",.0f")))
            print("Total matched donations $", (format(get_total_matched),",.2f"))
            print("Total donations received $", (format(sum(get_total_matched)+sum(get_total_personal),",.0f")))
            donor_input.close()
            donor_output.close()
        except FileNotFoundError:
            print("File Could not be found")
            pass
        except ValueError:
            print("The input file is empty.")
            pass
        except Exception as err:
            print(err)
                       
#def calculate match
def calculate_employer_donation_match(personal_donation,donation_code):
    donation_amount=[]
    index=0
    for code in donation_code:
        if code in donation_code[index]=="Ratio":
            for num in personal_donation:
                match=.5*int(num)
                if match<15000:
                    donation_amount.append(int(match))
                                       
        
                elif match>=15000:
                    amount=15000
                    donation_amount.append(int(amount))
                    
        elif code in donation_code[index]=="Dollar":
            for num in personal_donation:
                 if num<10000:                                           
                    match=num
                    donation_amount.append(int(match))
                
                 elif num>=10000:
                    match=10000
                    donation_amount.append(int(match))
                
        elif code in donation_code[index]=="None":
            for num in personal_donation:
                num=0
                donation_amount.append(int(num))
    index+=1
    return donation_amount
#def calculate donation
def calculate_total_donation(money_list,donation_list,total_benefits_list):                     
    index=0
    for num in money_list:
        total=int(money_list[index])+int(donation_list[index])
        total_benefits_list.append(int(total))
        index=index+1
    return total_benefits_list
                                                                               
def calculate_total_values(all_list):
    return sum(all_list)
#def donor names
def print_donor_names(donor_file,name,donation_matching,all_total_donation):
    index=0     
    for donor_name in name: 
        while donor_name!='':
            matched=str((format(donation_matching[index],",.2f")))
            total_benefits=str((format(all_total_donation[index],",.2f")))
            donor_file.write((name)+' has $'+matched+" in employer matched donations and"+ total_benefits+"total_donations.\r")
            donor.readline().rstrip('\n')
        index+=1
            
#def main
main()



        
    

