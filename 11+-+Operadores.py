
# coding: utf-8

# Operadores Uteis

# In[1]:


range(0,11)


# In[2]:


list(range(0,11))


# In[3]:


list(range(11))


# In[4]:


list(range(5,11))


# In[5]:


list(range(0,11,2))


# In[6]:


list(range(0,111, 10))


# In[7]:


list(range(0,101,10))


# In[9]:


contador = 0

for letra in 'abcde':
    print(f'No indice {contador} está a letra {letra}.')
    contador += 1


# In[11]:


for i,letra in enumerate('abcde'):
    print(f'No indice {contador} está a letra {letra}.')
    contador += 1


# In[12]:


'x' in ['x', 'y', 'z']


# In[13]:


'x' in ['U', 'y', 'z']


# In[14]:


lista1 = [1,2,3,4,5,6,7,8,9,10]


# In[15]:


min(lista1)


# In[16]:


max(lista1)


# In[19]:


lista1 = list(range(1,11))
print(lista1)


# In[18]:


max(lista1)


# In[20]:


from random import shuffle


# In[21]:


print(lista1)


# In[22]:


shuffle(lista1)


# In[23]:


print(lista1)


# In[24]:


from random import randint


# In[26]:


randint(0,100)


# In[29]:


input('Digite alguma coisa')


# In[31]:


x = input('Digite alguma coisa')


# In[32]:


x


# In[33]:


x = int(input('Digite um valor '))


# In[34]:


x


# In[35]:


x = float(input('Digite um valor '))


# In[36]:


x

