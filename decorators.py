"""
@ Will be used to decorate the function


"""

def cal(func):
    def addition():
        a= 20
        b = 30
        print(f"sum of {a} + {b} = {a+b}")
        
        func()

        print(f"sub of {b} - {a} = {b-a}")
    
    return addition

@cal
def return_func():
    print("Please decorate me")

return_func()