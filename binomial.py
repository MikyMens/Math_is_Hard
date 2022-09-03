from math import factorial
import pandas as pd

def binomial(p,n,r):
    return (factorial(n)/ (factorial(r)*factorial((n-r)))) * p**r * ((1-p)**(n-r))

if __name__ == "__main__":
    ans = [[binomial(0.6, i, j) for j in range(0,i+1)] for i in range(1,10)]
    df = pd.DataFrame(ans)
    df.columns.name = 'r'
    df.index.name = 'n'
    print('With a probability of 0.6, flip a coin n times and r is going to be number of sucessful head flips')
    print(df)
    