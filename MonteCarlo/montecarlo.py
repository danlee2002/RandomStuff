import random 
import math 
def main():
    inside, outside = 0,0
    # monte carlo approximation of pi, add epochs as needed
    iterations = 100000
    for i in range(iterations):
        x = random.uniform(-0.5,0.5)
        y = random.uniform(-0.5,0.5)
        if math.sqrt(x**2 + y **2) <=0.5:
            inside+=1
        else:
            outside+=1
    expected = math.pi
    approx = inside/outside
    error = abs(approx - expected)
    print(f'Iterations: {iterations}, Value: {inside/outside}, Expected: {expected}, Diff: {error}')
if __name__ == '__main__':
   main()
