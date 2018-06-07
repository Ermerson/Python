
# coding: utf-8

# In[1]:


def my_func(a, b):
    return sum((a,b)) * .05

my_func(40,60)


# In[2]:


def my_func(a=0, b=0, c=0, d=0, e=0):
    return sum((a,b,c,d,e))*0.05

my_func(40, 60, 20)


# In[4]:


def my_func(*args):
    return sum(args)*0.05


# In[5]:


my_func(40, 60, 20)


# In[7]:


def my_func(*valores):
    return sum(valores)*0.05

my_func(40, 60, 20)


# In[9]:


def my_func(**kwargs):
    if 'fruit' in kwargs:
        print(f"Minha fruta favorita é {kwargs['fruit']}")
    else:
        print('Eu não gosto de fruta')
        
my_func(fruit='abacate')
my_func(fruta='abacate')

