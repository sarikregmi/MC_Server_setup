print("""By running this server, you agree to the Minecraft End User License Agreement (EULA). 
You can read it here: https://aka.ms/MinecraftEULA""")
import requests
ram=input('Enter ram to be used in MB : ')
name='server'
url = 'https://piston-data.mojang.com/v1/objects/e6ec2f64e6080b9b5d9b471b291c33cc7f509733/server.jar'  # The actual file URL
response = requests.get(url)
def makingfiles():
    #store start up 
    store = f'java -Xmx{ram}M -Xms{ram}M -jar {name}.jar'
    #making bat file to run server
    bat_content = f'''
    @echo off
    {store}

    '''

    # Specify the name of the .bat file
    bat_filename = f'{name}.bat'

    # Write the content to the .bat file
    with open(bat_filename, 'w') as bat_file:
        bat_file.write(bat_content)

    #txt file eula
    eula_content = '''
    #By changing the setting below to TRUE you are indicating your agreement to our EULA (https://aka.ms/MinecraftEULA).
    #Mon Jun 09 15:12:57 NPT 2025
    eula=true

    '''

    # Specify the name of the .bat file
    eula_content_filename = 'eula.txt'

    # Write the content to the .bat file
    with open(eula_content_filename, 'w') as txt_file:
        txt_file.write(eula_content)
makingfiles()
# Save the file as .jar
with open('server.jar', 'wb') as f:
    f.write(response.content)
