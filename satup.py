# devlop no mask
#name tools M.Phish
import os
from time import sleep
from platform import uname
import subprocess
import colorama
from webbrowser import open as get

colorama.init()

try:
    from colorama import Fore as color
    
except ImportError:
    exit(color.RED+'pip insatll colorama')


print(color.YELLOW+'starting tools'.title())
print(color.LIGHTGREEN_EX+'no mask'.title()+'\n')

sleep(1.5)


from banner import Banner
from meno import panel

def main():
    def clears():
        pl=uname()[0]
        if pl =='Windows':
            return os.system('clear')
        else:
            return os.system('cls')
    


    def chack_install_php():
    
        state=subprocess.getoutput('php -v')
    
        if "'php' is not" in state:
            return(color.RED+'sary install php')
        
    
        return(True)

    chack=chack_install_php()




    def chack_install_ngrok():
        ngr=subprocess.getoutput('ngrok',encoding='utf-8')
        
        if 'ngrok - tunnel local ports to public URLs and inspect traffic' in ngr:
        
            return(True)
    
        return(color.YELLOW+'install ngrok')
    

    chack2=chack_install_ngrok()
    
    if chack==True and chack2==True:


        def runs(PR:str):
            port=PR
            local_host=subprocess.Popen(f'php -S localhost:{port}',shell=True)
            
            clears()
            if local_host:
        
                subprocess.Popen(f'ngrok http {port}',shell=True)
                
        x=input(color.YELLOW+"[*] "+color.LIGHTWHITE_EX+'Enter port'+color.GREEN+' >>>: ')
        
        runs(PR=x)


try:
    
    choice=input(color.YELLOW+"[*] "+color.LIGHTBLUE_EX+'Enter choice'+color.GREEN+' >>>: ')
    
    if choice=='1':
        main()
        
    elif choice=='2':
        get('https://www.php.net/')
        
    elif choice=='3':
        get('https://ngrok.com/')
    
    elif choice=='4':
        exit()
        
except KeyboardInterrupt:
    
    pass

