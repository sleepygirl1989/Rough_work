def primal_check(input_number= int(input("Please enter a number : "))):
    for i in range(2,input_number):
        result=input_number%i
        if result ==0 :
           return False
        else:
            return True


print(primal_check())