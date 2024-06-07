class Veiculo:
    def __init__(self,valor=0,modelo=0,quilometragem=0):
        self.valor = valor
        self.modelo = modelo
        self.quilometragem = quilometragem
    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print("Valor inconsistente")
    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    def get_quilometragem(self):
        return self.quilometragem
    def set_quilometragem(self):
        return self.quilometragem
    def atualiza_vl(self,vl):
        if vl > 0:
            if type(vl) == int:
                self.valor += vl
            elif type(vl) == float:
                self.valor += vl
            else:
                print("Dados inconsistentes")
    def atualiza_valor_pct(self,pct):
        self.valor += self.valor*(pct/100)
    def situacao(self):
        if self.quilometragem == 0:
            return f"O veículo é zero quilômetros"
        elif self.quilometragem <= 20000:
            return f"O veículo é seminovo"
        else:
            return f"O carro é usado"
    def situacao2(self):
        nome_classe = self.__class__.__name__
        if self.quilometragem == 0:
            return f"{nome_classe}, zero"
        elif self.quilometragem <= 20000:
            return f"{nome_classe}, seminovo"
        else:
            return f"{nome_classe}, usado"
    def calculo_ipva(self):
        nome_classe = self.__class__.__name__
        if len(nome_classe) == 5:
            ipva = (self.valor * 0.03) + 100
            return ipva
        else:
            ipva = self.valor * 0.02
            return ipva





class Carro(Veiculo):
    def __init__(self,valor,modelo,quilometragem=0,qtd_portas=4):
        super().__init__(valor,modelo,quilometragem)
        self.qtd_portas = qtd_portas
    def __str__(self):
        return f"{self.valor}, {self.modelo}, {self.quilometragem}, {self.qtd_portas}"
    def get_qtd_portas(self):
        return self.qtd_portas
    def set_qtd_portas(self,nova_qtd_portas):
        self.qtd_portas = nova_qtd_portas
    def calculo_ipva(self):
        ipva = (self.valor * 0.03) + 100
        return ipva
class Moto(Veiculo):
    def __init__(self,valor,modelo,quilometragem,cilindradas=0):
        super().__init__(valor,modelo,quilometragem)
        self.cilindradas = cilindradas
    def get_cilindradas(self):
        return self.cilindradas
    def set_cilindradas(self,nova_cilindradas):
        self.cilindradas = nova_cilindradas
    def calculo_ipva(self):
        ipva = self.valor * 0.02
        return ipva



if __name__ == '__main__':
    veiculo = Veiculo('classe B', 2005, 10000)
    carro1 = Carro(60000,'Corolla', 2003, 13000)
    carro2 = Carro(150000,'Ferrari', 1981)
    carro3 = Carro(4000,'Opala')
    moto = Moto(8000,'XJ',20000,100)
    moto2 = Moto(10000,'gareli',500)
print("Modelo:",carro1.get_modelo())
carro1.set_modelo('Fusca')
print("Modelo atualizado:",carro1.get_modelo())
print("Valor: $",carro1.get_valor())
carro1.set_valor(35000)
print("Valor atualizado: $",carro1.get_valor())
print(carro1.get_quilometragem())
print(carro1.get_qtd_portas())
print(vars(carro1)), print(vars(moto))
print(carro1.__dict__), print(moto.__dict__)
carro1.atualiza_vl(500)
print(carro1.get_valor())
carro1.atualiza_valor_pct(5)
print(carro1.get_valor())
print(carro1.situacao())
print(moto.situacao2())
print(carro1.calculo_ipva())
print(carro2.calculo_ipva())



