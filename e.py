
ANCHO = 800
ALTO = 600


#ProcessImage
    # Ampliar la imagen de la cámara
scale_factor = 800/640
new_width = int(bckgd.get_width() * scale_factor)
new_height = int(bckgd.get_height() * scale_factor)
bckgd = pygame.transform.scale(bckgd, (new_width, new_height))