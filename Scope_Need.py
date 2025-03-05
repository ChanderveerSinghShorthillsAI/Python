# Global Scope
x = "Global x"

def outer_function():
    # Enclosed Scope
    x = "Enclosed x"
    
    def inner_function():
        # Local Scope
        x = "Local x"
        print("Inside inner_function:", x)
    
    inner_function()
    print("Inside outer_function:", x)

outer_function()
print("Outside all functions:", x)