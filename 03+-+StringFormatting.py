
# coding: utf-8

# Formatação com PlaceHolders

# In[1]:


print('Vou inserir %s aqui.' %'alguma coisa')


# In[2]:


x = 3.14159265
print('o valor de x é %f' %x)


# In[3]:


x = 3.14159265
print('o valor de x é %.2f' %x)


# In[4]:


#veja o Arredondamento
x = 3.14159265
print('o valor de x é %.5f' %x)


# In[5]:


x = 3.14159265
print('o valor de x é %15.2f' %x)


# In[6]:


y = 123.555
print('o valor de y é %2.5f' %y)


# In[8]:


#Formatação com .format
print ('Vou inserir {} aqui.'.format('Alguma Coisa'))


# In[10]:


print('Vou inserir três coisas. A {}, a {} e a {}.' .format('primeira', 'segunda', 'terceira'))


# In[11]:


print('Vou inserir três coisas. A {2}, a {1} e a {0}.' .format('primeira', 'segunda', 'terceira'))


# In[12]:


print('{0:8} | {1:9}'.format('Fruta','Qtde') )


# In[14]:


print('{0:8} | {1:9}'.format('Fruta','Qtde'))
print('{0:8} | {1:9}'.format('Maças',3.0))
print('{0:8} | {1:9}'.format('Laranjas',10))


# Formatação com f-string

# In[15]:


nome = 'José'
print(f'Ele disse que seu nome é {nome}.')


# In[17]:


num = 23.45678
print('o numero é {0:10.4f}'.format(num))
print(f'o numero é {num:{10}.{6}}')


# In[22]:


#f-string não faz padding
num = 23.45
print('o numero é {0:10.4f}'.format(num))
print(f'o numero é {num:{10}.{6}}')


# In[24]:


#misture com .format()
num = 23.45
print('o numero é {0:10.4f}'.format(num))
print(f'o numero é {num:10.4f}')

