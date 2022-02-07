from colorama import Fore, Back, Style
from datetime import datetime
import requests
import colorama
import argparse
import time
import os

colorama.init()
os.system("clear")
print(Fore.GREEN)


def attack(url='http://127.0.0.1',wordlist='/usr/share/dirb/wordlists/common.txt',cookie=0,output=0):
	try:
		directoriesFile = open(wordlist,"r",encoding='utf-8')	
		dr_content = directoriesFile.read()			
		directoriesFile.close()
	except Exception as e:
		print(Fore.RED)
		print(f"\nError! error code: {e}")
	except KeyboardInterrupt:
		print(Fore.GREEN)
		print("\nbye bye")
	try:
		founds = []
		for directories in dr_content.split("\n"):	
			targetUrl = url + "/" + str(directories)
			result = requests.get(url=targetUrl,headers=cookie)
			if "200" in str(result.status_code):
				status_code = str(result.status_code)
				print(Fore.GREEN)
				web = f"[+] http://{url}/{directories} 			|> (Code:{status_code})"
				print(f"\nFound >> {web}")
				founds = str(web)
				if output != 0 or output != " ":
					with open(output,"a",encoding="utf-8") as file:
						file.write(founds + "\n")
						file.close()
						print(Fore.RED)
				else:
					pass
			else:
				status_code = str(result.status_code)
				web = f"[+] http://{url}/{directories} 		|> (Code:{status_code}"
				with open("otherSituations.txt","a",encoding="utf-8") as file:
					file.write(web + "\n")
					file.close()
						

				pass

	except KeyboardInterrupt:
		print(Fore.GREEN)
		print("\nbye bye")
	except Exception as e:
		print(Fore.RED)
		print(f"\nError! error code: {e}")
	info = datetime.today()
	time = datetime.ctime(info)
	print(Fore.RED)
	end_time = f"End Time: {time}".center(50,"=")
	print(end_time)
	
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", required=True, help="Target url\nhttp://test.com")
ap.add_argument("-w", "--wordlist", required=True, help="Directories or files wordlist\ndefault: /usr/share/dirb/wordlists/common.txt")
ap.add_argument("-c", "--cookie", required=False, help="Ör:\n 'Cookie': 'PHPSESSID=d143rj8718t2fl67a4jv4tb2s7; security=low'")
ap.add_argument("-o", "--output", required=False, help="Save to file")
args = vars(ap.parse_args())


url = args["url"] 				
wordlist = args["wordlist"] 	
cookie = args["cookie"]			
output = args["output"]		

print(Fore.BLUE)
print("""
                                                                                                                                                       
                                                                                                      .                                                   
                                                   ...'',,.                                         .''''.....                                            
                                              .'''''''''....                     .'''.              .......''.....                                        
                                         ..''.','...''....     '.     ...  .''. .:ddl.               .................                                    
                                       ..','',,''...''''...''',,.    ,od:..:dd:..;dd;  .:cccc:,.      ..'......'''......                                  
                                    ...'','..''.....'...  ..',,''::. ;ddc. ;dd:..'od;.,odc''::c;..,:;'...........,'..'.....                               
                                 ...'''..''..''.........';'':;::';o, .coo:;cdl.  'od,.'lo:.......,:lcclc'........,'..'.........                           
                              ...'...............,cooolc,..lc.:d;.cl...;c;,'',....;l,...,c:::;..lxo::lod;..,;....'...............                         
                              ....''...........;lol,.;odo' 'c:,,,,;c,........ ..................,::::loc'.cddl:,'.....'...........                        
                             .......'.........:dl'.   ;dd;  .',''.,c,....   .;:;'.,:.  .....'....  ..;;..cddl;,col,....''......'....                      
                          ...........'.'.... 'ddo:....ldo;     ''',..       ;olcooc;.     ....          'dd:. .,ldo....','.....'...'..                    
                        .................'.   ,ooollol:'..                 .co:;ll;,.      .            .''. .cddl.  ..........'..'''....                 
                     .............''.   ...    ....';.                      ,llolcc:'                       .cdc'.   ..   .........'.......               
                     .. ..   ......                                           ...'::.                        ..             ................              
                     ......  .                                              .;:cldc,.                                                ......               
                 .........                                                 .lxoccl,                                                   .''......           
                .......                                                     .,;:coo:.                                                   .',...'.          
              .......                                                            .;;.                                                     ........        
            ..'...                                                          ..     .'.                                                       ....'.       
           .....                                                           .;.      ;;'.                                                       ...''.     
          .....                                                            .;,     .;...                                                        ....'.    
         ....                                                               .,;;;;,,.                                                             .....   
        ...                                                                   ...,;'                                                                ....  
                                                                            ..,;cll:.                                                                     
                                                                           .cdocll,                                                                       
                                                                           .,clcloc,.                                                                     
                                                                              ...;cc.                                                                     
                                                                           .,'.  .,:'                                                                     
                                                                           .;ol;;cl;.                       Oğulcan KAÇAR                                             
                                                                            .;oddl;'.                       github.com/OgulcanKacarr                                              
                                                                           .:lloolc:'.                                                                    
                         .....'...'.......''..'.. .''.                       ......                      ..'....'...'.......'.........                    
                                                                           .........                                                                      
                                                                           ..........                                                                     
                                                                           ..........                                                                     
                                                                           .''....'..                                                                     
        """)

info = datetime.today()
start_time = datetime.ctime(info)
_cookie = cookie
print(Fore.BLUE)
print("".center(50,"_"))
print(Fore.RED)
print(f"Start Time: {start_time}\nUrl: {url}\nWordlist: {wordlist}\nCookie: {_cookie}")
print(Fore.BLUE)
print("".center(50,"_"))
a = os.path.exists(output)
if a == True:
	c = f"rm {output}" 
	os.system(c)		
b = os.path.exists("otherSituations.txt")
if b == True:
	os.system("rm otherSituations.txt")
attack(url,wordlist,cookie,output)