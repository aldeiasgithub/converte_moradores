import pandas as pd
import csv
import codecs
import datetime

class LeitorCSV:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def ler_csv(self):
        dados = []
        with codecs.open(self.nome_arquivo, 'r', encoding='utf-8-sig') as arquivo:
            leitor = csv.reader(arquivo, delimiter=';')
            # Pular a primeira linha
            next(leitor)
            for linha in leitor:
                # Excluir a última coluna
                linha = linha[:-1]
                dados.append(linha)
        return dados

class GravadorCSV:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        
    def manipular_string(self, string):
    # Remover ponto e vírgula e as aspas
        string_sem_ponto_virgula = string.replace(';', '').replace('"', '')
        # Obter os 4 últimos caracteres
        quatro_ultimos = string_sem_ponto_virgula[-4:]
        # Obter os dois primeiros caracteres
        dois_primeiros = string_sem_ponto_virgula[:2]
        # Concatenar as partes
        nova_string = f'"{quatro_ultimos + string_sem_ponto_virgula[2:-4] + dois_primeiros}";'
        return nova_string

    def gravar_csv(self, dados):
        with open(self.nome_arquivo, 'w', encoding='utf-8', newline='') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', quoting=csv.QUOTE_NONE, quotechar='', escapechar='\\')
            for linha in dados:
                linha = [campo.replace('"', '') for campo in linha]
                linha_formatada = ['"' + campo + '";' for campo in linha]
                linha_formatada[1] = self.manipular_string(linha_formatada[1])
                linha_formatada[7] = self.manipular_string(linha_formatada[7])
                linha_formatada[0] = linha_formatada[0][1:]  # Remover aspas no início do primeiro campo
                #linha_formatada[-1] = linha_formatada[-1][:-2]  # Remover aspas e ponto e vírgula do último campo
                linha_formatada[-1] = linha_formatada[-1][:-2] + '"'  # Adicionar aspas no final da última coluna
                linha_formatada = ''.join(linha_formatada)
                linha_formatada = '"' + linha_formatada[:-1] + '"\n'
                arquivo.write(linha_formatada)

def main():
    nome_arquivo_entrada = 'morador.csv'
    
    data_hora_atual = datetime.datetime.now()
    data_atual = data_hora_atual.strftime("%Y%m%d")
    hora_atual = data_hora_atual.strftime("%H")
    minutos_atual = data_hora_atual.strftime("%M")
    
    nome_arquivo_saida = f'MORADORES_{data_atual}{hora_atual}{minutos_atual}.csv'

    # Leitura do CSV
    leitor = LeitorCSV(nome_arquivo_entrada)
    dados = leitor.ler_csv()

    # Gravação do CSV
    gravador = GravadorCSV(nome_arquivo_saida)
    gravador.gravar_csv(dados)

    print("Arquivo gravado com sucesso!")

if __name__ == "__main__":
    main()
