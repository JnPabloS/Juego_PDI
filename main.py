from ProcessImages import *
from game import *
from window import *

#################################################################################
#                       INICIALIZACION DE VARIABLES
#################################################################################

# Inicializar Pygame
pygame.init()

# Definir la resolución de la ventana
ANCHO = 640
ALTO = 480
screen_width, screen_height = ANCHO, ALTO

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Crear ventana de start
startScreen = pygame.display.set_mode((screen_width, screen_height))

# Crear ventana de juego
screen = pygame.display.set_mode((screen_width, screen_height))

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

# Titulo de la ventana
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


#################################################################################
#                               INICIO DEL JUEGO
#################################################################################

while True:
    #Mostrar ventana de inicio si apenas se abre el juego
    if inicio:
        ShowStart(fondo,logo, startScreen, boton_rect, fuente, AZUL, BLANCO)
        inicio = False

    elif jugando:
        # Obtener un fotograma de la cámara
        ret, frame = cap.read()
        
        # Identifica objetos de color amarillo
        objects = BuscarColor(frame)
    
        # Poner la imagen de la cámara en el fondo de la ventana
        SetBackground(frame, screen)
        
        # Verificar tiempo de juego
        jugando, tiempo_transcurrido = ItsOver(tiempo_finalizacion)
        
        # Mostrar tiempo y puntaje en pantalla
        ShowText(screen, AZUL, tiempo_transcurrido, points)
        
        # Actualizar la ventana
        UpdateWindow(ball, screen, screen_height)
        
        # Verificar si hay colision para actualizar los puntos
        points = Col(points, frame, objects, ball, rebote)

    #Mostrar pantalla de juego finalizado
    elif ~jugando and tiempo_inicial != 0 and ~finalizado:  
        # Poner la imagen de la cámara en el fondo de la ventana
        SetBackground(frame, screen) 
        finalizado = ShowFinal(screen, ball, points)
        tiempo_inicial = 0
    
    # Obtener eventos de teclas o botones
    for event in pygame.event.get():
          
        # Salir del programa si se cierra la ventana
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Detectar si se hace clic en el botón start
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if boton_rect.collidepoint(event.pos):
                start.play()  
                      
                points, ball, tiempo, tiempo_inicial, tiempo_finalizacion, jugando, playing_music = StartGame(playing_music)

        #Detectar que se presiona una tecla
        elif event.type == pygame.KEYDOWN:
            # Cierra el juego cuando se presiona la letra "q"
            if event.key == pygame.K_q:
                cap.release()
                pygame.quit()
                quit()
            
            # Reinicia el juego con la letra "r" si ya se termino de jugar
            elif event.key == pygame.K_r and finalizado:
                finalizado = False
                points, ball, tiempo, tiempo_inicial, tiempo_finalizacion, jugando, playing_music = StartGame(playing_music) 
    