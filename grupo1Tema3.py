#Celso Comuniam Pereira
#Ruylis Bialta

class Diario_de_bordo: #Criação da classe Diario_de_bordo
    def __init__(self, viagens, datas, locais): #Criado a definições para viagens, data e locais  
        try: #Faz a tentativa de inserção dos comandos abaixo
            self.viagens = viagens  
            self.datas = datas      
            self.locais = locais   
            print("Informações cadastradas com sucesso!") #Exibe informação de cadastros realizados com sucesso
        except ValueError as e: #Faz o tratamento em caso de erro
            print(f"Erro ao cadastrar: {e}")

    def cadastro(self, experiencia, foto): #Crado definições para experiência e foto
        self.experiencia = experiencia  
        self.__foto = foto
        #Abaixo criado um return para exibir as informações dos dados das definições              
        return f"Viagem número {self.viagens}, em {self.datas}, para {self.locais}, experiência {self.experiencia}, cod das fotos {self.__foto}"

    def resumo_viagem(self):  # Método sobrescrito - polimorfismo
        return f"Resumo: Viagem para {self.locais} na data {self.datas}."

class ViagemInternacional(Diario_de_bordo): #Classe filha que herda de Diario_de_bordo
    def __init__(self, viagens, datas, locais, idioma): #Novo atributo criado: idioma
        super().__init__(viagens, datas, locais) #Chama o construtor da classe mãe
        self.idioma = idioma  

    def resumo_viagem(self): #Sobrescrevendo o método da classe mãe - polimorfismo
        return f"[Internacional] Viagem para {self.locais}, em {self.datas}, idioma local: {self.idioma}."

#Atribuição das informações para exibição 
print("\nCriando viagem nacional")
viagem_nacional = Diario_de_bordo(1, "10/02/2025", "João Pessoa")
print(viagem_nacional.cadastro("Boa", 101))
print(viagem_nacional.resumo_viagem())

print("\nCriando viagem internacional")
viagem_internacional = ViagemInternacional(2, "23/01/2025", "Lisboa", "Portugal")
print(viagem_internacional.cadastro("Muito Boa", 202))
print(viagem_internacional.resumo_viagem())
