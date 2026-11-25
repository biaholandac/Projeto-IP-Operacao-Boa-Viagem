#recursos 
import os
import pygame

PASTA_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
PASTA_IMAGENS = os.path.join(PASTA_ASSETS, "imagens")
PASTA_SONS = os.path.join(PASTA_ASSETS, "sons")
_imagens = {}
_sons = {}
_fontes = {}
_audio_ok = False
_musica_atual = None 

def carregar_imagem(nome) :
  if nome in _imagens :
    return _imagens[nome]
  caminho = os.path.join(PASTA_IMAGENS, nome)

  if not os.path.exists(caminho) :
    return None 

  try :
    imagem = pygame.image.load(caminho).convert_alpha()
  except pygame.error :
    return None 

  _imagens[nome] = imagem
  return imagem 

def iniciar_audio() :
  global _audio_ok
  if not _audio_ok :
    try :
      pygame.mixer.init()
      _audio_ok = True
    except pygame.error :
      _audio_ok = False 
  return _audio_ok 

def carregar_som(nome) :
  if nome in _sons :
    return _sons[nome]
  if not _audio_ok :
    return None
  
  caminho = os.path.join(PASTA_SONS, nome)

  if not os.path.exists(caminho) :
    return None 

  try :
    som = pygame.mixer.Sound(caminho)
  except pygame.error :
    return None 

  _sons[nome] = som
  return som

def tocar_som(nome, volume=1.0) :
  som = carregar_som(nome)
  if som is not None :
    som.set_volume(volume)  
    som.play()

def tocar_musica(nome, volume=0.5) :
  global _musica_atual
  if not _audio_ok :
    return 
  if _musica_atual == nome :
    return 
  caminho = os.path.join(PASTA_SONS, nome)
  if not os.path.exists(caminho) :
    return 
  try :
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)  
    _musica_atual = nome
  except pygame.error :
    pass

def parar_musica() :
  global _musica_atual
  if not _audio_ok :
    return 
  pygame.mixer.music.stop()
  _musica_atual = None

def fonte(tamanho) :
  if tamanho in _fontes :
    return _fontes[tamanho]
  try :
    fonte = pygame.font.Font(None, tamanho)
  except pygame.error :
    return None 
  _fontes[tamanho] = fonte
  return fonte

def desenhar_texto(tela, texto, tamanho, cor, posicao) :
  fonte_obj = fonte(tamanho)
  if fonte_obj is None :
    return 
  texto_surface = fonte_obj.render(texto, True, cor)
  tela.blit(texto_surface, posicao)

def desenhar_sprite(tela, imagem, x, y, largura, altura, cor) :
  retangulo = pygame.Rect(0, 0, largura, altura)
  retangulo.midbottom = (x, y) #midbottom é o ponto central da parte inferior do retângulo
  if imagem is not None :
    imagem_redimensionada = pygame.transform.scale(imagem, (largura, altura)) #deixa no formato correto
    tela.blit(imagem_redimensionada, retangulo) #desenha a imagem na tela
  else :
    pygame.draw.rect(tela, cor, retangulo) 

  return retangulo
