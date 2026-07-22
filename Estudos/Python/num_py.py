import numpy as np

dados = np.array([1,3,5,7])

print(dados.mean())

print(dados.std())

x = np.arange(start=0,stop=50,step=2).reshape(5,5)
print(type(x))
print(len(x))
print(x)
print(x.mean())


s = np.arange(10)

#[start:stop:step]
print(s[-1:0:-1])

i = np.zeros(9, dtype=np.int8).reshape(3,3)

for j in range(3):
    i[j:j+1:,j:j+1:] = 1    

    
print(i)

print(i.diagonal())

l = np.linspace(0,1,9).reshape(3,3) 
f = np.full((3,3),1)

print(l+f)

r = l+f*2

print(r)
print(r.sum())
print(r.mean())
print(r.max())
print(r.trace())

col = np.array([1,2,3])[:,np.newaxis]

result = r*col
print(result)
print(result.mean(axis=0))