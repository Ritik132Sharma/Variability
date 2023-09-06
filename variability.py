import pandas as pd

df = pd.read_csv("C:\\Users\\Admin\\Downloads\\Mall_Customers.csv")
print(df)


'''range'''

def rang(data):

    cal_range= max(data) - min(data)
    return cal_range

'''variance'''

def var(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data)/(len(data)-1)
    return variance

'''Standard deviation'''

def sd(data):
    std= var(data) ** 0.5
    return std

'''Interquartile range'''

def ir(data):
    s=sorted(data)
    n = len(s)
    q1 = (n + 1) // 4
    q3 = 3 * q1
    iqr= (s[q3 - 1] + s[q3]) / 2 - (s[q1 - 1] + s[q1]) / 2
    return iqr


ai=df['Annual Income (k$)']

r=rang(ai)
print(r)

v=var(ai)
print(v)

s=sd(ai)
print(s)

iq=ir(ai)
print(iq)















