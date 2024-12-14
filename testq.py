# try - catch exception handling 
file = open('youtube.txt', 'w')
try:
    file.write('chhai aur code')
finally:
    file.close()
    
with open('youtube.txt', 'w') as file:
    file.write('chai aur python') 