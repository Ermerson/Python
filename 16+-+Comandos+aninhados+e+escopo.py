
# coding: utf-8

# In[1]:


x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())


# In[2]:


print(x)


# Acima podemos ver o Python sendo estranho pra cacete. A função ```printer()``` não altera o valor da variável x, pois elas possuem endereços de memória diferentes.

# In[5]:


name = 'Este é um nome global'

def greet():
    name = 'José'
    
    def hello():
        print('Hello, ' + name)
        
    hello()
    
greet()
#a variável name dentro da enclosing function tem precedência sobre a global


# In[6]:


print(name)


# In[7]:


x = 50

def func(x):
    print('x é', x)
    x = 2
    print('x é alterado localmente para', x)
    
func(x)
print('x ainda é', x)


# In[8]:


x = 50

def func():
    global x
    print('Esta função agora está usando um x global')
    print('A global x é:', x)
    x = 2
    print('O valor de x mudou para', x)
    
print('Antes de chamar func(), x é:', x)
func()
print('O valor de x fora de func() é', x)


# In[9]:


x


# Ao definir como variável global, o valor de x é atualizado.
