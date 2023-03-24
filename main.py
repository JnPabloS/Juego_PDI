from ProcessImages import *
from window import *

def Col(points):
      
    if(IntersectionMasks(frame, faces, ball) and ball.vy > 0):
        #Mostrar el puntaje
        points = points + 1
        ball.vy = -random.randint(25, 40)
        ball.vx = random.randint(-19, 19)
        rebote.play()
        
    return points
        
# Inicializar Pygame
pygame.init()

# Definir la resolución de la ventana
ANCHO = 640
ALTO = 480
screen_width, screen_height = ANCHO, ALTO

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Crear una ventana de Pygame
startScreen = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.display.set_mode((screen_width, screen_height))

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

pygame.init()

# Crear una ventana
pygame.display.set_caption("Yelow Ball")

# Crear un objeto Font
fuente = pygame.font.Font('fonts/ARCO.ttf', 50)

# Crear un rectángulo para el botón de "start"
boton_rect = pygame.Rect(ANCHO/2 - 100, ALTO/2 + 20, 200, 100)
inicio = True
jugando = False  # Variable de estado para indicar si se está jugando o no
finalizado = False
tiempo_inicial = 0

#sonidos e imagenes
start = pygame.mixer.Sound('sounds/start.mp3')
rebote = pygame.mixer.Sound('sounds/rebote.mp3')
sounstrack = pygame.mixer.music.load('sounds/soundtrack.mp3')
logo = pygame.image.load('images/logo.png') #logo
fondo = pygame.image.load('images/fondo.jpg')
playing_music = False

#contador de puntos
points = 0

while True:
    
    # Obtener eventos
    for evento in pygame.event.get():
    # Salir del programa si se cierra la ventana
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Detectar si se hace clic en el botón
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_rect.collidepoint(evento.pos):
                start.play()  
                      
                points, ball, tiempo, tiempo_inicial, tiempo_finalizacion, jugando, playing_music = StartGame(playing_music)

        if inicio:
            ShowStart(fondo,logo, startScreen, boton_rect, fuente, AZUL, BLANCO)
            inicio = False

    if jugando == True:
        # Obtener un fotograma de la cámara
        ret, frame = cap.read()
        
        # Identifica objetos de color amarillo
        faces = BuscarColor(frame)
    
        # Poner la imagen de la cámara en el fondo de la ventana
        SetBackground(frame, screen)
        
        # Verificar tiempo de juego
        jugando, tiempo_transcurrido = ItsOver(tiempo_finalizacion)
        
        # Mostrar tiempo y puntaje en pantalla
        ShowText(screen, AZUL, tiempo_transcurrido, points)
        
        # Actualizar la ventana
        UpdateWindow(ball, screen, screen_height)
        
        # Actualizar los puntos
        points = Col(points)

    elif ~jugando and tiempo_inicial != 0 and ~finalizado:  
        # Poner la imagen de la cámara en el fondo de la ventana
        SetBackground(frame, screen) 
        finalizado = ShowFinal(screen, ball, points)
        tiempo_inicial = 0
    
    # Esperar a que el usuario presione una tecla para salir
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                cap.release()
                pygame.quit()
                quit()
            elif event.key == pygame.K_r and finalizado:
                finalizado = False
                points, ball, tiempo, tiempo_inicial, tiempo_finalizacion, jugando, playing_music = StartGame(playing_music) 
    