
# coding: utf-8

# ### Exemplo stateful

# In[2]:


current_speaker = None
   
def register(name):
   global current_speaker
   current_speaker = name
   
def speak(text):
   print('[%s] %s' % (current_speaker, text))
   
register('João')
speak('hello world')
register('carlos')
speak('foobar')


# ## Objetos tambem são stateful
# 

# In[15]:


class Speaker():
    def __init___(self,name):
        self._name = name
        
    def speak(self,text):
        print('[%s] %s' % (self._name, text))
        
joao = Speaker('João')


# ## Funções stateless geralmente são triviais

# In[6]:


def speak(speaker, text):
    print('[%s] %s ' %(speaker, text))
    
joao = 'Joao'
speak.joao('Hello World.')
carlos = 'Carlos'
speak(carlos, 'foobar')

