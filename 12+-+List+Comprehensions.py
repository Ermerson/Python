
# coding: utf-8

# In[4]:


#pegar as letras em uma palavra
lista1 = [x for x in 'palavra']


# In[2]:


lista1


# In[5]:


#elevar os valores de um range ao quadrado e fazer um lista
lista2 = [x**2 for x in range(0,11)]


# In[6]:


lista2


# In[7]:


#colocando um If
lista3 = [x for x in range(11) if x%2==0]


# In[8]:


lista3


# In[9]:


#contas mais complicadas
celsius = [0,10,20,1,34.5]


# In[10]:


farenheit = [((9/5)*temp + 32) for  temp in celsius ]


# In[11]:


farenheit


# In[12]:


lista4 = [x**2 for x in [x**2 for x in range(11)]]


# In[13]:


lista4

