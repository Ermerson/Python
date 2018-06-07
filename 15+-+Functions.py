
# coding: utf-8

# Forma geral de definir funções

# In[5]:


def nome_da_funcao(arg1, arg2):
    #faça alguma coisa
    #retorne o resultado desejado
    pass #necessário para evitar erro de parse quando se declara uma função que não faz nada


# In[1]:


def say_hello():
    print('Hello')


# In[2]:


say_hello()


# In[6]:


#algumas funções são pré-definidas em Python
print("O print é uma delas")


# In[9]:


#passagem de parâmetros
def greeting(nome):
    print('Hello, %s' %(nome));


# In[10]:


greeting('José')


# In[11]:


def add_num(num1, num2):
    return num1 + num2;


# In[12]:


add_num(4, 5)


# In[13]:


add_num('4', '5')


# In[21]:


def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            print(num, 'não é primo')
            break
    else:
        print(num, 'é primo')


# Indentação é extremamente importante em Python para que as coisas funcionem como o esperado (posição do ```else``` no exemplo acima)

# In[25]:


is_prime(37)


# In[31]:


import math

def is_prime2(num):
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


# In[29]:


is_prime2(38)


# In[30]:


is_prime2(37)


# In[32]:


is_prime2(37)


# In[33]:


list(range(3, int(math.sqrt(81)) + 1, 2))


# In[34]:


is_prime(3421348902452034)


# In[35]:


is_prime2(7487236777777777777777623487263874623462378462738462873647283647826347826347826378263)

