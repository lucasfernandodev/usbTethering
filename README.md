# usbTethering

Script Linux para ativar automaticamente o tethering de internet do s3 note.

## Como usar?

### Requisitos

- adb
- usb debug ativo no android
- Testado no s3 note com android 5.0

### Baixando projeto

```
  git clone git@github.com:lucasfernandodev/usbTethering.git && cd usbTethering/
```

### Dependências

```
  pip install pipenv
  sudo pip install pipenv-shebang

  pipenv install
```

### Iniciando script

Crie um arquivo .env e add: 

```
PHONE_PASSWORD=
PHONE_SERIAL=
```

* PHONE_PASSWORD : Senha pincode para desbloquear o celular usando adb
* PHONE_SERIAL : Serial do celular no Linux (use "adb devices -l" para pegar o code serial )



Torne o script executável:

```
chmod +x usbTethering.sh
```

Inicie o script

```
./usbTethering.sh
```


### Referência
- <a href="https://pipenv.readthedocs.io/">Documentação do pipenv</a>