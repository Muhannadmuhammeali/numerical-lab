def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    
    if func(a) * func(b) > 0:
        print("The function does not change sign on the interval [a, b].")
        return None
    
    
    iter_count = 0
    
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        
        
        if func(c) == 0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        
        iter_count += 1
        
        if iter_count >= max_iter:
            print("Maximum iterations reached.")
            break
    

    return (a + b) / 2




def func(x):
    return x**2 - 4  


a = int(input("a :"))
b = int(input("b :"))
tolerance = 1e-6

root = bisection_method(func, a, b, tol=tolerance)

if root is not None:
    print(f"The root is approximately: {root}")