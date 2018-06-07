
# coding: utf-8

# Arquivos
# 

# In[1]:


get_ipython().run_cell_magic('writefile', 'test.txt', 'este é só um arquivinho de teste')


# In[2]:


myfile = open('NaoExiste.txt')


# In[3]:


pwd


# In[4]:


myfile= open('test.txt')


# In[5]:


myfile.read()


# In[8]:


myfile.seek(0)


# In[10]:


myfile.read()


# In[11]:


myfile.close()


# In[12]:


#Escrevendo em um arquivo


# In[13]:


#truncando o arquivo
myfile= open('text.txt', 'w+')


# In[14]:


#escrvendo
myfile.write('Esta é a linha 1.')


# In[19]:


myfile.write('\n Esta é a linha 2')


# In[16]:


myfile.read()


# In[24]:


myfile.seek(0)


# In[22]:


myfile.read()


# In[25]:


myfile.readline()


# In[26]:


#adcionando Linhas
myfile = open('test.txt', 'a+')


# In[27]:


myfile.write('\nLinha 3.')
myfile.write('\n Linha Final.')


# In[28]:


myfile.seek(0)


# In[29]:


myfile.read()


# In[30]:


myfile.close()


# In[32]:


for line in open('test.txt'):
    print(line)

