                                         
import os                                                                 
                                                                          
path=input("Enter the folder path")                                       
current_ext=input("Enter the current extention")                          
new_ext=input("Enter the new entention")                                  
                                                                          
for filename in os.listdir(path):                                         
    if filename.endswith(f".{current_ext}"):                              
        new_name=filename.replace(f".{current_ext}",f".{new_ext}")        
        os.rename(os.path.join(path,filename),os.path.join(path,new_name))
                                                                          
print("Renaming complete.")           
