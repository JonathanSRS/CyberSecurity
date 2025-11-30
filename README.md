# CyberSecurity
Treinamentos de Cibersegurança
### Ambiente Kali e Metasploitable
![](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/medusa_metasplotable.png)

### Medusa
medusa -h {IP} -U {.txt} -P {.txt} -M {mod} -t {num} -T {num}\
-h Host\
-U Usuário ou lista de usuários\
-P Senha ou lista de senhas\
-M Modúlo\
-t Núméro de logins\
-T Número de hosts\

![](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/medusa.png)

enum4linux -a {IP} | tree {output.txt}

1. Criar Word list\
![](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/Criar%20lista%20de%20palavras.png)
2. Executar medusa\
![](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/Testar%20senha%20ftp.png)
3. Validar senha 
![](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/medusa_ftp.png)

### Keylogger Ransoware
Script ransoware.py que criptografa os dados de um determinado diretorio\
Script keylogger.pyw que captura as informações digitas pelo usuário e as envia para um e-mail

### Instalar packeges
1. pip install secure-smtplib
2. pip install pynput

### Criar arquivo .properties com as variavéis
1. EMAIL_ORIGEM
2. EMAIL_DESTINO
3. SENHA_EMAIL
