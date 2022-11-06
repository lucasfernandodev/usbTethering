# usbTethering

Script Linux para ativar automaticamente o tethering de internet no s3 note.


### Requisitos

- adb
- usb debug ativo no android
- Testado no s3 note com android 5.0

### Baixando projeto

```
git clone git@github.com:lucasfernandodev/usbTethering.git && cd usbTethering/
```

### Instalado dependências

```
pip install pipenv
sudo pip install pipenv-shebang

pipenv install
```

### Configurando

Crie um arquivo .env e add: 

```
PHONE_PASSWORD=
PHONE_SERIAL=
```

* PHONE_PASSWORD : Senha pincode para desbloquear o celular usando adb
* PHONE_SERIAL : Serial do celular no Linux (use "adb devices -l" para pegar o code serial )

### Iniciando projeto

Tornando o script executável e inciando

```
chmod +x usbTethering.sh && ./usbTethering.sh
```


### Referência
- <a href="https://pipenv.readthedocs.io/">Documentação do pipenv</a>