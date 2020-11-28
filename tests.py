
# import modules 
import winapps 
  
try: 
# get each application with list_installed() 
    for item in winapps.list_installed(): 
        print(item)
        break
           
except Exception: 
    pass
