import pygame, os, sys, time, random
from pygame.locals import *

#lista de imagens
b1feitico = ['Bruxa1feitico1.png','Bruxa1feitico2.png']
b1walk = ['Bruxa1walk1.png','Bruxa1walk2.png']
b1neutra = ['Bruxa1neutra.png']
b1tiro = ['tiro1b1.png','tiro2b1.png']

b2feitico = ['Bruxa2feitico1.png','Bruxa2feitico2.png']
b2walk = ['Bruxa2walk1.png','Bruxa2walk2.png']
b2neutra = ['Bruxa2neutra.png']
b2tiro = ['tiro1b2.png','tiro2b2.png']

b3feitico = ['Bruxonafeitico1.png','Bruxonafeitico2.png']
b3walk = ['Bruxonawalk1.png','Bruxonawalk2.png']
b3neutra = ['Bruxonaneutra.png']
b3tiro = ['tiro1b3.png','tiro2b3.png']

armario = ['BruxaArmario1.png','BruxaArmario2.png','BruxaArmario3.png','BruxaArmario4.png','BruxaArmario5.png','BruxaArmario6.png','BruxaArmario7.png']
neve = ['BruxaBonecoNeve1.png','BruxaBonecoNeve2.png','BruxaBonecoNeve3.png']
guarda = ['BruxaKnightAndando1.png','BruxaKnightAndando2.png','BruxaKnightAndando3.png','BruxaKnightAndando4.png','BruxaKnightAndando5.png','BruxaKnightAndando6.png']
livro = ['livro.png']
pocoes = ['pocao1.png','pocao2.png','pocao3.png','pocao4.png','pocao5.png']

class Pocao(pygame.sprite.Sprite):
    def __init__(self, xpo, ypo, itemType, pocao, p): #sound=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pocao[p]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=xpo
        self.rect.y=ypo
        self.itemType = itemType

class NossoLivro(pygame.sprite.Sprite):
	def __init__(self, xlivro, ylivro,image):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x += xlivro
		self.rect.y += ylivro

pygame.init()

largura = 567
altura = 1201

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode((956, 560))

pygame.display.set_caption('Jogo da Bruxa')
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
	def __init__ (self,listaplay,posplay):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(listaplay[posplay])).convert()
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.rect.x = largura/2
		self.rect.y = altura/2-200
		

class Item(pygame.sprite.Sprite):
	def __init__(self, xpoc, ypoc,image):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('pocao1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x += xpoc
		self.rect.y += ypoc
		self.vida = 3

	def tiravida(self):
		if self.vida > 0:
			if self.vida == 1:	
				self.vida -= 1
				print('Voce morreu')
			if self.vida == 2:
				self.vida -=1
				imagpocao = 'pocao1.png'
				items = pygame.sprite.Group()
				pocao = Item(50, 40, imagpocao)
				items.add(pocao)
				items.blit(screen)
			if self.vida == 3:
				self.vida -=1
				imagpocao = 'pocao1.png'
				items = pygame.sprite.Group()
				pocao = Item(50, 40, imagpocao)
				items.add(pocao)
				items.draw(screen)
				pocaoo = Item(50 + self.rect.size[0], 40, imagpocao)
				items.add(pocaoo)
				items.draw(screen)
				screen = pygame.display.set_mode((50,40))
				pocaoo = Item(50 + self.rect.size[0], 40, imagpocao)
				screen.blit(pocaoo, (70,40))    

		else:
			print('Ta morta faz tempo')
			quit()

class PocaoVida(pygame.sprite.Sprite):
	def __init__ (self,xvida,yvida):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(pocoes[0])).convert()
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.rect.x = xvida
		self.rect.y = yvida

	def tiravida(self):
		if self.vida > 0:
			self.vida -= 1
		else:
			self.vida = 0


class Pocao(pygame.sprite.Sprite):
	def __init__ (self,xvida,yvida):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(pocoes[0])).convert()
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.rect.x = xvida
		self.rect.y = yvida


class Inimigo(pygame.sprite.Sprite):
	def __init__ (self,listaini,xinimigo,yinimigo):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(listaini[0])).convert()
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.rect.x = xinimigo
		self.rect.y = yinimigo
		self.x_speed = 4
		self.gperna = 0
		self.nperna = 0
		self.aperna = 0
		self.vida = 2
		self.lanca_feitico = 0
		self.tiro_ativado = 0
		self.tiro_andando = 0
		self.xdotiro = largura/2 + 70
		self.ydotiro = altura/2-200 + 50

	def tiravida(self):
		if self.vida > 0:
			self.vida -= 1
		else:
			self.vida = 0

	def zigzaginimigo(self, xini, h):
		self.rect.x += self.x_speed
		if self.rect.right > xini[h] + 100:
			self.x_speed = -5
		if self.rect.left < xini[h] - 100:
			self.x_speed = 5

	def guardaparado(self):
		self.x_speed = 0

	def guarda_andando(self,posguarda1,posguarda2):           #MUDAR A PERNA
		if self.gperna < 7:
			self.image = pygame.image.load(os.path.join(guarda[posguarda1])).convert()
			self.image.set_colorkey(black)
		if self.gperna >= 7:
			self.image = pygame.image.load(os.path.join(guarda[posguarda2])).convert()
			self.image.set_colorkey(black)
		if self.gperna > 14:
			self.gperna = 0
		self.gperna += 1

	def neve_mexendo(self,posneve1,posneve2):                     #MUDAR A PERNA
		if self.nperna < 10:
			self.image = pygame.image.load(os.path.join(neve[posneve1])).convert()
			self.image.set_colorkey(black)
		if self.nperna >= 10:
			self.image = pygame.image.load(os.path.join(neve[posneve2])).convert()
			self.image.set_colorkey(black)
		if self.nperna > 20:
			self.nperna = 0
		self.nperna += 1

	def armario_mexendo(self,posarmario1,posarmario2,posarmario3,posarmario4,posarmario5,posarmario6,posarmario7):
		if self.aperna < 10:
			self.image = pygame.image.load(os.path.join(armario[posarmario1])).convert()
			self.image.set_colorkey(black)
		if self.aperna >= 10 and self.aperna < 20:
			self.image = pygame.image.load(os.path.join(armario[posarmario2])).convert()
			self.image.set_colorkey(black)
		if self.aperna >= 20 and self.aperna < 30:
			self.image = pygame.image.load(os.path.join(armario[posarmario3])).convert()
			self.image.set_colorkey(black)
		if self.aperna >= 30 and self.aperna < 40:
			self.image = pygame.image.load(os.path.join(armario[posarmario4])).convert()
			self.image.set_colorkey(black)
		if self.aperna >= 40 and self.aperna < 50:
			self.image = pygame.image.load(os.path.join(armario[posarmario5])).convert()
			self.image.set_colorkey(black)
		if self.aperna >= 50 and self.aperna < 60:
			self.image = pygame.image.load(os.path.join(armario[posarmario6])).convert()
			self.image.set_colorkey(black)
		if self.aperna >= 60 and self.aperna < 70:
			self.image = pygame.image.load(os.path.join(armario[posarmario7])).convert()
			self.image.set_colorkey(black)
		if self.aperna >= 70:
			self.aperna = 0
		self.aperna += 1

	def GuardaLancaFeitico(self,posguarda3,posguarda4,posguarda5):
		if self.lanca_feitico < 5+10:
			self.image = pygame.image.load(os.path.join(guarda[posguarda3])).convert()
			self.image.set_colorkey(black)
		if self.lanca_feitico >= 5+10 and self.lanca_feitico<10+10:
			self.image = pygame.image.load(os.path.join(guarda[posguarda4])).convert()
			self.image.set_colorkey(black)
		if self.lanca_feitico >= 10+10:
			self.image = pygame.image.load(os.path.join(guarda[posguarda5])).convert()
			self.image.set_colorkey(black)
			self.tiro_ativado = 1
		if self.lanca_feitico > 15+10:
			self.lanca_feitico = 0
		self.lanca_feitico += 1

	def NeveLancaFeitico(self,posneve3,posneve4):
		if self.lanca_feitico < 5+10:
			self.image = pygame.image.load(os.path.join(neve[posneve3])).convert()
			self.image.set_colorkey(black)
		if self.lanca_feitico >= 5+10:
			self.image = pygame.image.load(os.path.join(neve[posneve4])).convert()
			self.image.set_colorkey(black)
		if self.lanca_feitico >10+10:
			self.lanca_feitico = 0
		self.lanca_feitico += 1

	def InimTiro(self,tiro):
		if self.tiro_andando < 40 and self.tiro_andando!= 0:
			screen.blit(pygame.image.load(tiro), (self.xdotiro,self.ydotiro))
			self.xdotiro -= 2
		if self.tiro_andando >= 40:
			self.xdotiro = largura/2 + 70
			self.tiro_andando = -1
		self.tiro_andando +=1

class Platform(pygame.sprite.Sprite):
	def __init__ (self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join('tijolo.png')).convert()
		self.image.set_colorkey(white)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
platforms = pygame.sprite.Group()
p1 = Platform(600, altura/2 - 600)
p2 = Platform(700, altura/2 - 600)
p3 = Platform(780, altura/2 - 600)
p4 = Platform(820, altura/2 - 600)
p5 = Platform(950, altura/2 - 600)
platforms.add(p1)
platforms.add(p2)
platforms.add(p3)
platforms.add(p4)
platforms.add(p5)


def colisao(x2,y2,w2,h2):
	if x2+w2 >= largura/2 >= x2 and y2+h2 >= altura/2-200 >= y2:
		return True
	elif x2+w2 >= largura/2+player.rect.size[0] >= x2 and y2+h2 >= altura/2-200 >= y2:
		return True
	elif x2+w2 >= largura/2 >= x2 and y2+h2 >= altura/2-200+player.rect.size[1] >= y2:
		return True
	elif x2+w2 >= largura/2+player.rect.size[0] >= x2 and y2+h2 >= altura/2-200+player.rect.size[1] >= y2:
		return True
	else:
		return False

def colisaoini(x1,y1,w1,h1,x2,y2,w2,h2):
	if x2+w2 >= x1 >= x2 and y2+h2 >= y1 >= y2:
		return True
	elif x2+w2 >= x1+w1 >= x2 and y2+h2 >= y1 >= y2:
		return True
	elif x2+w2 >= x1 >= x2 and y2+h2 >= y1+h1 >= y2:
		return True
	elif x2+w2 >= x1+w1 >= x2 and y2+h2 >= y1+h1 >= y2:
		return True
	else:
		return False

tamback = 1701

def background(x,y):
	for k in range(-10,25):
		screen.blit(backgroundload,(x+k*tamback,y))

def tijolo(xplat,yplat):
	screen.blit(tijoloload,(xplat,yplat))

def pocaovidal(xvida,yvida):
	screen.blit(pocaovida.image,(xvida,yvida))

def pocaoloload(xpo,ypo):
	screen.blit(pocaoload,(xpo,ypo))

def gameoverr(xplat,yplat):
	screen.blit(gameoverload,(xplat,yplat))

def inimigoo(listaini,h,xi,yi):
	screen.blit(listaini[h].image,(xi,yi))

def playerl(xplay, yplay):
	screen.blit(player.image,(xplay, yplay))

def mainmenu():
	# o que aparecera no menu
	hist1 = pygame.image.load('historia13.png')
	hist2 = pygame.image.load('historia2.png')
	back = pygame.image.load('background.jpg')
	logo = pygame.image.load('logo.png')
	fonte = pygame.font.Font('freesansbold.ttf',30) #chamada da fonte
	op1 = fonte.render("Novo Jogo",1,(0,0,0)) 
	op2 = fonte.render("Ajustes",1,(0,0,0))
	op3 = fonte.render("Sair",1,(0,0,0))
	op1Selec = fonte.render("Novo Jogo",1,(148,0,211))
	op2Selec = fonte.render("Ajustes",1,(148,0,211))
	op3Selec = fonte.render("Sair",1,(148,0,211))

	a = op1Selec
	b = op2
	c = op3

	#musica do menu		
	pygame.mixer.init()
	pygame.mixer.music.load('menu.mp3')
	pygame.mixer.music.play()

	h = 0
	if (h ==0):
		screen.fill(white)
		screen.blit(hist1,[0,-26])
		pygame.display.update()
		time.sleep(5)

		screen.fill(white)
		screen.blit(hist2,[0,-26])
		pygame.display.update()
		time.sleep(5)

		h +=1

	tela = 1

	if (h == 1):
		saída = False
		while not saída:
			if(tela==1):
				screen.fill([245,245,245])
				screen.blit(back,[-10,-150])
				screen.blit(logo,[70,-100])
				screen.blit(a, [380,300])
				screen.blit(b, [380,400])
				screen.blit(c, [380,500])
			else:
				settings()
				
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.KEYDOWN:
					if event.key == K_ESCAPE:
						sys.exit()
					elif b == op2Selec and event.key == K_DOWN:
						a = op1
						b = op2
						c = op3Selec
					elif c == op3Selec and event.key == K_UP:
						a = op1
						b = op2Selec
						c = op3
					elif c == op3Selec and event.key == K_DOWN:
						a = op1Selec
						b = op2
						c = op3
					elif a == op1Selec and event.key == K_UP:
						a = op1
						b = op2
						c = op3Selec
					elif b == op2Selec and event.key == K_UP:
						a = op1Selec
						b = op2
						c = op3
					elif event.key == K_DOWN:
						a = op1
						b = op2Selec
						c = op3

					if a == op1Selec and event.key == K_RETURN:
						pygame.mixer.music.stop()
						pygame.mixer.music.load('jogo.mp3')
						pygame.mixer.music.play()
						g = game_loop(p1,p2,p3,p4,p5)
						saída = True
					elif b == op2Selec and event.key == K_RETURN:
						settings()
						tela = 2
					elif c == op3Selec and event.key == K_RETURN:  #sai, mas nao aparece a imagem
						sair()

			pygame.display.update()

#funcao que sai do jogo
def sair():
	#pygame.init()
	screen.fill(white)
	screen.blit(pygame.image.load('sair.png'),[150,150])
	pygame.display.update()
	time.sleep(2)
	pygame.quit()
	sys.exit()

#funcao ajustes do menu
def settings():
	#o que aparece no ajustes
	pygame.init()
	fonte = pygame.font.Font('freesansbold.ttf',30)
	som = fonte.render('Audio ligado',1,(0,0,0))
	somon = fonte.render('Audio ligado',1,(148,0,211))
	som2 = fonte.render('Audio desligado',1,(0,0,0))
	som2off = fonte.render('Audio desligado',1,(148,0,211))
	volta = fonte.render('Voltar',1,(0,0,0))
	volta2 = fonte.render('Voltar',1,(148,0,211))
	logo2 = pygame.image.load('logo2.png')

	a = somon
	b = som2
	c = volta

	while True:
		screen.fill(white)
		screen.blit(logo2,[150,60])
		screen.blit(a, [380,300])
		screen.blit(b, [380,400])
		screen.blit(c,[380,500])

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if b == som2off and event.key == K_DOWN:
					a = som
					b = som2
					c = volta2
				elif b == som2off and event.key == K_UP:
					a = somon
					b = som2
					c = volta
				elif a == somon and event.key == K_UP:
					a = som
					b = som2
					c = volta2
				elif a == somon and event.key == K_DOWN:
					a = som
					b = som2off
					c = volta
				elif c == volta2 and event.key == K_UP:
					a = som
					b = som2off
					c = volta
				elif c == volta2 and event.key == K_DOWN:
					a = somon
					b = som2
					c = volta

				if c == volta2 and event.key == K_RETURN:
					h = 1
					mainmenu()
				elif b == somon and event.key == K_RETURN:
					pygame.mixer.music.pause()
				elif a == somon and event.key == K_RETURN:
					pygame.mixer.music.rewind()

		pygame.display.update()

def jump(self):
	self.y_change = 1/2 * 10 *self.vel

def gravidade(self):
	if self.y > 5:
		self.y_change -= 0.9
	else:
		self.y_change = 0
		self.yplat = altura/2 - 400

def andando(self):
	if self.x_change!=0:               #MUDAR A PERNA
		if self.perna < 10:
			player.image = pygame.image.load(os.path.join(walk_da_bruxa[0])).convert()
			player.image.set_colorkey(black)
		if self.perna >= 10:
			player.image = pygame.image.load(os.path.join(walk_da_bruxa[1])).convert()
			player.image.set_colorkey(black)
		if self.perna > 20:
			self.perna = 0
		self.perna += 1
	if self.x_change == 0:
		player.image = pygame.image.load(os.path.join(neutra_da_bruxa[0])).convert()
		player.image.set_colorkey(black)

backgroundload = pygame.image.load('background2.png')
tijoloload = pygame.image.load('tijolo.png')
pocaovidaload = pygame.image.load(pocoes[0])
pocaoload = pygame.image.load(pocoes[0])
gameoverload = pygame.image.load('gameover.png')

xvida = 0
yvida = 0
var = 0
imagpocao = pocoes[0]
aini = []
xini = []
listaini = []
for t in range(0,10):                    #Espalhar os inimigos 
	i = random.randint(0,2)
	if i == 0:
		a = guarda
		print('guarda')
	if i == 1:
		a = neve
		print('neve')
	if i == 2:
		a = armario
		print('armario')
	xini.append(random.randint(500,5000))
	aini.append(a)
	inim = Inimigo(aini[t],xini[t],400.5)
	listaini.append(inim)

plataformas = []
for t in range(0,15):
	random_xplat = random.randint(600,700)
	random_yplat = random.randint(200,300)
	plataformas.append((random_xplat,random_yplat))

def livromagico(xlivro, ylivro):
	livro = pygame.image.load('livro.png')
	screen.blit(livro,[xlivro,ylivro])
	pygame.display.update()


bruxa_escolhida = 1
if bruxa_escolhida == 1:
	walk_da_bruxa = b1walk
	neutra_da_bruxa = b1neutra
	feitico_da_bruxa = b1feitico
	tiro_da_bruxa = b1tiro
if bruxa_escolhida == 2:
	walk_da_bruxa = b2walk
	neutra_da_bruxa = b2neutra
	feitico_da_bruxa = b2feitico
	tiro_da_bruxa = b2tiro
player = Player(walk_da_bruxa,0)
pocaovida = PocaoVida(xvida,yvida)



class game_loop():
	def __init__ (self,p1,p2,p3,p4,p5):
		self.x = -16
		self.y = 20.5
		self.vida = 30

		self.xplat1 = 600
		self.yplat1 = altura/2 - 300
		self.xplat2 = 2500
		self.yplat2 = altura/2 - 300
		self.xplat3 = 4800
		self.yplat3 = altura/2 - 300
		self.xplat4 = 6070
		self.yplat4 = altura/2 - 300
		self.xplat5 = 7550
		self.yplat5 = altura/2 - 300


		self.x_change = 0
		self.y_change = 0
		self.vel = 4.5
		self.perna = 0
		self.feitico = 0
		self.lanca_feitico = 0
		self.tiro_ativado = 0
		self.tiro_andando = 0
		self.xdotiro = player.rect.x + 100
		self.ydotiro = player.rect.y + 50

		gameExit = False
		while not gameExit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True

				if event.type == pygame.KEYDOWN:
					if self.feitico == 0:
						if event.key == pygame.K_LEFT:
							self.x_change = 6
						if event.key == pygame.K_RIGHT:
							self.x_change = -6
						if event.key == pygame.K_UP:
							if self.y_change == 0:
								jump(self)
					if event.key == pygame.K_SPACE:
						self.feitico = 1
						if self.tiro_andando!=0:
							self.xdotiro = player.rect.x + 100
							self.ydotiro = player.rect.y + 50
							colidebini = colisaoini(self.xdotiro, self.ydotiro,3, 0.75,listaini[h].rect.x + self.x, listaini[h].rect.y + self.y, listaini[h].rect.size[0], listaini[h].rect.size[1])
							if colidebini:
								listaini[h] = Inimigo(aini[h],xini[h],1400.5)
								print('morre inimigo')
							else:
								print('nao ta morrendo')

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						self.x_change = 0
					if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						self.y_change = 0
					if event.key == pygame.K_SPACE:
						self.feitico = 0
						self.lanca_feitico = 0
			
			def BruxaLancaFeitico():
				if self.lanca_feitico < 5:
					player.image = pygame.image.load(os.path.join(feitico_da_bruxa[0])).convert()
					player.image.set_colorkey(black)
				if self.lanca_feitico >=5:
					player.image = pygame.image.load(os.path.join(feitico_da_bruxa[1])).convert()
					player.image.set_colorkey(black)
					self.tiro_ativado = 1
				self.lanca_feitico += 1
			
			def BruxaTiro():
				if self.tiro_ativado >=1 and self.tiro_ativado<=30:
					if self.tiro_andando < 5:
						screen.blit(pygame.image.load(tiro_da_bruxa[0]), (self.xdotiro,self.ydotiro))
						self.xdotiro += 1
					if self.tiro_andando >= 5:
						screen.blit(pygame.image.load(tiro_da_bruxa[1]), (self.xdotiro,self.ydotiro))
						self.xdotiro += 1
					if self.tiro_andando >= 10:
						self.tiro_andando = 0
					self.tiro_andando += 1
					self.tiro_ativado += 1
				if self.tiro_ativado > 30:
					self.xdotiro = player.rect.x + 100
					self.tiro_ativado = 0

			#colidp = colisao(self.xplat+self.x_change+25, self.yplat+self.y_change, 160-25, 54)

			#if not colidp:
			self.xplat1 += self.x_change
			self.yplat1 += self.y_change
			self.xplat2 += self.x_change
			self.yplat2 += self.y_change
			self.xplat3 += self.x_change
			self.yplat3 += self.y_change
			self.xplat4 += self.x_change
			self.yplat4 += self.y_change
			self.xplat5 += self.x_change
			self.yplat5 += self.y_change


			self.x += self.x_change
			self.y += self.y_change
			if self.tiro_andando!=0:
				self.xdotiro += self.x_change
				self.ydotiro += self.y_change
	
			gravidade(self)

			for h in range(len(listaini)):
				if aini[h] == guarda:
					listaini[h].zigzaginimigo(xini,h)
					listaini[h].guarda_andando(0,1)
				if aini[h] == neve:
					listaini[h].neve_mexendo(0,1)
				if aini[h] == armario:
					listaini[h].armario_mexendo(0,1,2,3,4,5,6)
				

				colidebini = colisaoini(self.xdotiro-100, self.ydotiro, 100, 0.75,listaini[h].rect.x + self.x, listaini[h].rect.y + self.y, listaini[h].rect.size[0], listaini[h].rect.size[1])
				if colidebini:
					listaini[h] = Inimigo(aini[h],xini[h],1400.5)
					print('morre inimigo')
				else:
					print('nao ta morrendo')
				colidi = colisao(listaini[h].rect.x + self.x, listaini[h].rect.y + self.y, listaini[h].rect.size[0], listaini[h].rect.size[1])
				

				#colisao com o efeito:
				colidefeito = colisao(self.xdotiro, self.ydotiro, inim.rect.size[0], inim.rect.size[1])
				if colidefeito or colidi:
					if self.vida > 0:
						if self.vida == 1:	
							self.vida -= 1
							print('Voce morreu')
						if self.vida == 2:
							self.vida -=1
							imagpocao = 'pocao1.png'
							items = pygame.sprite.Group()
							pocao = Item(50, 40, imagpocao)
							items.add(pocao)
							items.blit(screen)
						if self.vida == 3:
							self.vida -=1
							imagpocao = 'pocao1.png'
							items = pygame.sprite.Group()
							pocao = Item(50, 40, imagpocao)
							items.add(pocao)
							items.draw(screen)
							pocaoo = Item(50 + self.rect.size[0], 40, imagpocao)
							items.add(pocaoo)
							items.draw(screen)   

					else:
						print('Ta morta faz tempo')
						quit()
						gameoverr()


				if colidi:
					print('ta morrendo')
					if aini[h] == guarda:
						listaini[h].guardaparado()
						listaini[h].GuardaLancaFeitico(2,3,4)
						listaini[h].InimTiro('tiroguarda.png')
						listaini[h].xdotiro += self.x_change 
					if aini[h] == neve:
						listaini[h].NeveLancaFeitico(1,2)
						listaini[h].InimTiro('tironeve.png')
						listaini[h].xdotiro += self.x_change
					#FUNCAOBATALHA

					print(self.vida)
					if self.vida<=0:
						print('GAME OVER')
						quit()
					else:
						self.vida -= 1


				for f in range(h+1,len(listaini)):
					if h <= len(listaini)-1:
						colidii = colisaoini(listaini[f].rect.x + self.x, listaini[f].rect.y + self.y, listaini[f].rect.size[0]+400, listaini[f].rect.size[1], listaini[h].rect.x + self.x, listaini[h].rect.y + self.y, listaini[h].rect.size[0]+400, listaini[h].rect.size[1])

					if colidii:
						print('ta colidindo!!!!!!!!!!!!')
						listaini[h].rect.x += 500
						xini[h] += 500

				inimigoo(listaini, h, listaini[h].rect.x + self.x, listaini[h].rect.y + self.y)

			if self.feitico == 0:
				andando(self)
			if self.feitico == 1:
				BruxaLancaFeitico()

			BruxaTiro()
			livromagico(-6000,20)

			print('x: {0} , y: {1}'.format(self.x,self.y-400-185))

			pygame.display.update()

			imagpocao = 'pocao1.png'
			items = pygame.sprite.Group()
			pocao = Item(self.x +600, self.y+450, imagpocao)
			pocaoo = Item(50 + 57, 40, imagpocao) #57 = tamanho horicontal do tiro do guarda

			items.add(pocao,pocaoo)
			items.draw(screen)

			imaglivro = 'livro.png'
			livrinho = pygame.sprite.Group()
			livro = NossoLivro(-8000,20.5 , imaglivro)

			livrinho.add(livro)
			livrinho.draw(screen)

			background(self.x,self.y-400-185)

			if self.x<-8000:
				screen.fill(white)
				screen.blit(pygame.image.load('gameover.png'),[70,-100])
				pygame.display.update()
			


			platforms.draw(screen)
			platforms.remove(p1)
			platforms.remove(p2)
			platforms.remove(p3)
			platforms.remove(p4)
			platforms.remove(p5)
			p1 = Platform(self.xplat1, self.yplat1)
			p2 = Platform(self.xplat2, self.yplat2)
			p3 = Platform(self.xplat3, self.yplat3)
			p4 = Platform(self.xplat4, self.yplat4)
			p5 = Platform(self.xplat5, self.yplat5)
			platforms.add(p1)
			platforms.add(p2)
			platforms.add(p3)
			platforms.add(p4)
			platforms.add(p5)
			hits = pygame.sprite.spritecollide(player,platforms,False)
			if hits:
				print('bati')
				self.y_change = 0
				print(p1.rect.bottom)
				if p1.rect.bottom < 414 and p1.rect.bottom >= 402:
					self.y_change = -14

			#tijolo(self.xplat,self.yplat)
			playerl(player.rect.x,player.rect.y)
			
			if self.vida <= 10 and self.vida > 0:
				print('to com uma')
				pocaoloload(50,40)
			elif self.vida <= 20 and self.vida > 10:
				print('to com duas')
				pocaoloload(50,40)
				pocaoloload(50 + pocao.rect.size[0]+10, 40)
			elif self.vida <= 30 and self.vida > 20:
				print('to com tres')
				pocaoloload(50,40)
				pocaoloload(50 + pocao.rect.size[0]+10, 40)
				pocaoloload(50 + pocaoo.rect.size[0]*2+20, 40)			
			clock.tick(60)

mainmenu()
pygame.quit()
quit()