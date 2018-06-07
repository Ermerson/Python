
# coding: utf-8

# Laços de Repetição While Loops

# In[2]:


x = 0

while x < 10:
    print(f'o valor de x é {x}')
    print('x ainda é menor que 10')
    x+=1


# In[5]:


x = 0
while x < 10:
    print(f'o valor de x é {x}')
    print('x ainda é menor que 10')
    x+=1
else:
    print('Terminou')


# In[7]:


x = 0 
while True:
    if x > 10:
        print(f'{x} Saindo...')
        break
    else:
        print(f'{x} continuando...')
    x+=1


# In[8]:


x = 0 
while True:
    if x > 10:
        print(f'{x} Saindo...')
        break
    else:
        print(f'{x} continuando...')
        #continue = FuDEU LoopInfernal
    x+=1


# In[9]:


x = 0 
while True:
    x+=1
    if x > 10:
        print(f'{x} Saindo...')
        break
    else:
        continue
        print(f'{x} continuando...')
        #continue = FuDEU LoopInfernal

