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
-T Número de hosts

![](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/medusa.png)

### Pentest Ftp
1. Criar Word list\
![Ambiente Kali criando word list](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/Criar%20lista%20de%20palavras.png)
2. Executar medusa\
![Ambiente Kali Pentest com medusa protocolo ftp](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/Testar%20senha%20ftp.png)
3. Validar senha 
![Ambiente Kali validar entrada na porta ftp](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/medusa_ftp.png)

### Pentest smb
1. enum4linux -a {IP} | tree {output.txt}\
![Ambiente Kali executar com enum4linux](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/Enumerando.png)\
![Ambiente Kali resultado enum4linux](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/resultado%20enumera%C3%A7%C3%A3o.png)
2. Criar nova word list\
![Ambiente Kali criar nova word list](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/Criar%20novas%20wordlists.png)
3. Executar medusa\
![Ambiente Kali Pentest com medusa protocolo smb](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/Executando%20medusa%20modulo%20smb.png)
4. Resultado do comando medusa\
![Ambiente Kali Resultado smb](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/Sucesso%20smb.png)
5. Acessar smb\
![Ambiente Kali Acesso ao smb](https://github.com/JonathanSRS/CyberSecurity/blob/main/img/Acessar%20smb.png)

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
