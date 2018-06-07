
# coding: utf-8

# In[1]:


my_list=[1,2,3]


# In[2]:


my_list


# In[15]:


my_list = ['uma String', 23, 1003232, 'o']


# In[4]:


my_list


# In[5]:


len(my_list)


# In[6]:


my_list[0]


# In[7]:


my_list[:3]


# In[8]:


my_list + ['novo item']


# In[9]:


my_list


# In[16]:


my_list += ['novo item']


# In[11]:


my_list


# In[17]:


my_list = my_list + ['um outro novo item']


# In[18]:


my_list


# In[19]:


my_list * 2


# In[20]:


list1 = [1, 2, 3]


# In[21]:


list1.append(4)


# In[22]:


list1


# In[23]:


list1.pop(0)


# In[24]:


list1


# In[26]:


#insere um valor na posição indicada
list1.insert(2,2)


# In[27]:


list1


# In[28]:


popped =  list1.pop(2)


# In[29]:


popped


# In[30]:


list1


# In[31]:


list1.pop()


# In[33]:


outra_lista = ['a', 'x', 'e', 'b', 'c']


# In[34]:


outra_lista.sort()


# In[35]:


outra_lista


# In[36]:


outra_lista.reverse()


# In[37]:


outra_lista


# In[40]:


lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]
matriz = [lst1, lst2, lst3]


# In[41]:


matriz


# In[42]:


matriz[0]


# In[43]:


col1 = [row[0] for row in matriz]


# In[44]:


col1


# In[45]:


col1 = [row[1] for row in matriz]


# In[46]:


col1

