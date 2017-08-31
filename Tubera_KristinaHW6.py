#Author: Kristina Tubera
#Homework Number & Name: Homework 6
#Due Date:10/17/16
#Program Description:List and Tuples Homework

#DECLARE CONSTANTS
EMPLOYEE_DATA="EmployeeData.txt"
EMPLOYEE_SUMMARY_DATA="EmployeeSummaryData.txt"
CONTRIBUTION_401K= .05
LIFE_INSURANCE_COST= .01

def main():
    try:
        employee_input=open(EMPLOYEE_DATA, 'r')
        employee_output=open(EMPLOYEE_SUMMARY_DATA ,'w')
        
        employee_name_list=[]
        salary_list=[]
        life_insurance_election_list=[]
        health_insurance_election_list=[]
       
        name=employee_input.readline().rstrip('\n')
    
        while name!='':
            employee_name_list.append(name)
            
            salary=employee_input.readline().rstrip('\n')
            salary_list.append(int(salary))
            
            life_insurance=employee_input.readline().rstrip('\n')
            life_insurance_election_list.append(life_insurance)
            
            health_insurance=employee_input.readline().rstrip('\n')
            health_insurance_election_list.append(health_insurance)
            
            name=employee_input.readline().rstrip('\n')
            
        get_401k_contribution=calc_contribution(salary_list)
        get_life_insurance=calc_life_insurance(life_insurance_election_list,salary_list)
        get_health_insurance=calc_health_insurance(health_insurance_election_list)
        get_total_benefit= calc_total_benefit(get_401k_contribution,get_life_insurance,get_health_insurance)

        get_total_salary=calc_total(salary_list)
        get_total_401k=calc_total(get_401k_contribution)
        get_total_life_insurance=calc_total(get_life_insurance)
        get_total_health_insurance=calc_total(get_health_insurance)
  
        

        total_summary(employee_output,employee_name_list, salary_list,get_total_benefit)

        print("Number of employee processed:",len(employee_name_list))
        print("Total salary paid: $", (format(get_total_salary,",.0f")))
        print("Total benefits paid: $", (format(sum(get_401k_contribution)+sum(get_life_insurance)+sum(get_health_insurance),",.2f")))
        print("Total 401k paid: $", (format(get_total_401k,",.0f")))
        print("Total life insurance paid: $", (format(get_total_life_insurance,',.0f')))
        print("Total health insurance paid: $", (format(get_total_health_insurance,',.0f')))
        employee_input.close()
        employee_output.close()
    except FileNotFoundError:
        print("File Could not be found")
        pass
    except ValueError:
        print("The input file is empty.")
        pass
    except Exception as err:
        print(err)
                   
#define calc_contribution   
def calc_contribution(payment_list):
    contribution_list_1=[]
    for num in payment_list:
        contribution_amount=int(num)*CONTRIBUTION_401K
        contribution_list_1.append(contribution_amount)
    return contribution_list_1
#define calc_life_insurance
def calc_life_insurance(life_insurance_list,salary1_list):
    life_insurance_cost_list=[]
    index=0
    for life_insurance_choice in life_insurance_list:
        if life_insurance_choice=='Y':
            life_cost =int(salary1_list[index])*LIFE_INSURANCE_COST
            index+=1
        if life_insurance_choice=="N":
            life_cost=0
            index+=1
        life_insurance_cost_list.append(life_cost)
    return life_insurance_cost_list
#define calc_health_insurance
def calc_health_insurance(health_list):
    health_insurance_cost_list=[]
    for choice in health_list:
        if choice =="PPOI":
            cost=1875
        elif choice =="PPOF":
            cost=3890       
        elif choice =="NONE":
            cost=0
        health_insurance_cost_list.append(cost)
    return health_insurance_cost_list

#define calc_total_benefit
def calc_total_benefit(money_list,life_insurance1,health_insurance1):
    total_benefits_list=[]
    index=0
    for num in money_list:
        total=float(money_list[index])+float(life_insurance1[index])+float(health_insurance1[index])
        total_benefits_list.append(float(total))
        index+=1
    return total_benefits_list
#define calc_total
def calc_total(all_list):
    return sum(all_list)
#define total_summary
def total_summary(donor_file,name,salary,benefit_amount):
    employee=name.readline().rstrip('\n')
    while employee in name!='':
        output_salary=format(int(salary),",.0f")
        output_benefits=format(int(benefit_amount),",.2f")
        employee_file.write((name)+' earns $'+str(output_salary)+" and contributes"+ str(output_benefits)+"towards benefits.\r")
        employee=name.readline().rstrip('\n')
    
#def main    
main()

        
        
    
        
