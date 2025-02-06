def categorize_age(age):
    ageCategory = "TBD"

    if age <= 1:
         ageCategory = "Infant"
    else:
        ageCategory != "Infant"
    if age > 1 and age < 13:
        ageCategory = "Child"
    else:
        ageCategory != "Child"
    if age > 13 and age < 20:
        ageCategory = "Teenager"
    else:
        ageCategory != "Teenager"
    if age >= 20:
        ageCategory = "Adult"
    else:
        ageCategory != "Adult"



    return ageCategory



if __name__ == '__main__':
   
    age = float(input("Enter the person's age: "))
   
    ageBucket = categorize_age(age)
    print (ageBucket)
    
    #Program #2, Donovan Thompson 2/5/25
