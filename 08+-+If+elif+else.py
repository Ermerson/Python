
# coding: utf-8

# Estrutura Condicional
# 

# In[1]:


if True:
    print('É verdadeiro')


# In[2]:


x = 1
if x > 0:
    print('x é positivo')
else:
    print('x é negativo ou nulo')


# In[4]:


x=-1
if x > 0:
    print('x é positivo')
elif x == 0:
    print('x é nulo')
else:
    print('x é negativo')


# In[5]:


#indentação
if False:
    print('É verdadeiro')
    print('Dentro do If')
print('Fora do If')


# In[6]:


x = 0
if x > 0:
    print('x é positivo')
else:
    if x == 0:
        print('x é nulo')
    else:
        pass #palavra chave reservada para indicar passagem.
    print('x é negativo')

