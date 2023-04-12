playlist = {} # diccionario vacio
playlist['canciones'] = [] # lista vacia de canciones 


def app():
     

     agregar_playlist = True

     while agregar_playlist:
          nombre_playlist = input('Como deseas nombrar la play list?\r\n')

          if nombre_playlist:
               playlist['nombre'] = nombre_playlist
               agregar_playlist = False # desactivar el true 

               # llamar la funcion agregar canciones
               agregar_canciones()

               # print(playlist) para validar si esta trabajando bien
def agregar_canciones():
     # flag hacemos una bandera para que ingrese la cancion 
     agregar_cancion = True


     while agregar_cancion:
     # preguntar que cancion desea agregar 
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\nAgrega canciones para playlist{nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para no agregar mas canciones \r\n'  # si coloco += estoy concatenando con la pregunta anterior
         

        cancion = input(pregunta) 
        if cancion == "X":
             # Dejar de agregar canciones
             agregar_cancion = False
             # mostrar resumen de la play list 
             mostrar_resumen()
        else:
             # agregar canciones a playlist
             playlist['canciones'].append(cancion)# Recordar que .append agrega elementos a una lista 
# mostrar resumen de la playlist         
def mostrar_resumen():
     nombre_playlist = playlist['nombre']
     print(f'playlist:{nombre_playlist}\r\n')
     print('Canciones:\r\n')  
     for cancion in playlist['canciones']:
          print(cancion)   
app()           

    


          
   
