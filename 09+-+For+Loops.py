
# coding: utf-8

# Laços de Repetição

# In[1]:


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[2]:


for num in lista1:
    print(num)


# In[3]:


for garrafa in lista1:
    print(garrafa)


# In[5]:


#somente os pares
for num in lista1:
    if num%2 == 0:
        print(num)


# In[9]:


#somar os numero a lista
list_sum = 0
for num in lista1:
    list_sum += num
print(f'A soma é {list_sum}')


# In[12]:


for letra in 'Esta é uma String':
    print(letra)


# In[14]:


tup = (1,2,3,4,5)
for t in tup:
    print(t)


# In[15]:


lista2 = [(2,4),(6,8),(10,12)]


# In[17]:


for tup in lista2:
    print (tup)


# In[20]:


#tuple unpacking - desempacotando
for (t1,t2) in lista2:
    print(t1,t2,t1)


# In[21]:


d = {'k1':1, 'k2':2, 'k3':3}


# In[22]:


for item in d:
    print(item)


# In[23]:


for k,v in d.items():
    print(k,v)

