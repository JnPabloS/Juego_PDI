import time
from ClassBall import *
from ProcessImages import IntersectionMasks

# Se definen todas las variables para iniciar a jugar
def StartGame(playing_music):  
    count = 0
    tiempo = 20
    tiempo_inicial = time.time()
    tiempo_finalizacion = tiempo_inicial + tiempo
    jugando = True
    
    # Agregar la bola
    ball = Ball()
    
    if not playing_music:
        # Start playing music
        pygame.mixer.music.play(-1)
        playing_music = True
        pygame.mixer.music.set_volume(0.5)
        
    return [count, ball, tiempo, tiempo_inicial, tiempo_finalizacion, jugando, playing_music]

# Si hay colision se actualizan los puntos
def Col(points, frame, faces, ball, rebote):
      
    if(IntersectionMasks(frame, faces, ball) and ball.vy > 0):
        #Mostrar el puntaje
        points = points + 1
        ball.vy = -random.randint(25, 40)
        ball.vx = random.randint(-19, 19)
        rebote.play()
        
    return points

# Se verifica el tiempo de juego
def ItsOver(tiempo_finalizacion):
    
    tiempo_actual = time.time()
    tiempo_transcurrido = int(tiempo_finalizacion - tiempo_actual)
    
    if tiempo_transcurrido >=0:
        return [True, tiempo_transcurrido]
    
    else:
        return [False, 0]
        