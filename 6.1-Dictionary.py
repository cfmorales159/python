# Del libro Python Crash Course
# Capítulo 6.1 - Diccionarios
alien_0={'color':'green','points':6}
print(alien_0['color'])
print(alien_0['points'])
new_points=alien_0['points']
print(f"You earned {new_points} points!!!")
alien_0={}
alien_0['color']='red'
alien_0['points']=10 
print(alien_0)
print(alien_0['points'])
print(type(alien_0['points']))
print(type(alien_0['color']))
