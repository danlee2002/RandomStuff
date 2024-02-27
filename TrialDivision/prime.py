import math 
#trial division implementation for checking prime  
def prime(val: int) -> bool:
    n = int(math.sqrt(val))
    if val == 1:
        return False
    for i in range(2,n):
        if val % i == 0:
            return False
    else:
        return True

def main():
    print(prime(23))


if __name__ == "__main__":
    main()

