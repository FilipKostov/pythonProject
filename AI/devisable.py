
def check_dev(x, y):
    if x%y==0:
        return True
    else:
        return False

if __name__ == "__main__":
    print("Enter x:")
    x=float(input())
    print(f"Enter y:")
    y=float(input())
    pom=check_dev(x,y)
    if pom:
        print(f"The two numbers are devisable.")
    else:
        print(f"The two numbers are NOT devisable.")