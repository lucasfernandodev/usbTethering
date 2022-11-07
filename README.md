# usbTethering

Script Linux para ativar automaticamente o tethering de internet no s3 note.


## Requisitos

- android tools adb
- USB debugging ativo no android

## Baixando projeto

```shell
git clone git@github.com:lucasfernandodev/usbTethering.git && cd usbTethering/
```

## Instalado dependências

```shell
pip install pipenv
sudo pip install pipenv-shebang

pipenv install
```

## Configurando

Crie um arquivo .env e adicione:

```
PHONE_PASSWORD=
PHONE_SERIAL=
```

* PHONE_PASSWORD : Senha pincode para desbloquear o celular usando adb
* PHONE_SERIAL : Serial do celular no Linux (use "adb devices -l" para pegar o code serial )

## Iniciando projeto

Tornando o script executável e inciando

```shell
chmod +x usbTethering.sh && ./usbTethering.sh
```

<br />
<br />

##### - Testado no Samsung s3 note com android 5.0

### Referência
- <a href="https://pipenv.readthedocs.io/">Documentação do pipenv</a>