import random



class AdvinheONumero:
    def __init__(self):
        self.valorx = 0
        self.valor_minimo = 1 
        self.valor_maximo = 100
        self.tentar_novamente = True
    
    def GerarNumero(self):
        self.valorx = random.randint(self.valor_minimo, self.valor_maximo)


    def chute(self):
        self.chute_numero = input('Chute um numero: ')

    
    def Iniciar(self):
        self.GerarNumero()
        self.chute()
        while self.tentar_novamente == True:
            if self.chute_numero > str(self.valorx):
                print('Muito alto! Chute um numero mais baixo: ')
                self.chute()
            elif self.chute_numero < str(self.valorx):
                print('Muito baixo! Chute um numero mais alto: ')
                self.chute()
            if self.chute_numero == self.valorx:
                self.tentar_novamente = False
                print('PARABENS VOCE ACERTOU!')


comecar = AdvinheONumero()
comecar.Iniciar()
