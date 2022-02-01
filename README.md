# Instruções para rodar localmente

#### Pré-requisitos: Python3+
<br>

**Passo a Passo**

## 1. Criar um ambiente de python e ativá-lo
```bash
$ python3 -m venv env
$ source /env/bin/activate
```
## 2. Instalar os pacotes necessários para rodar a aplicação
```bash
$ pip3 install -r requirements.txt
```

## 3 Rodar o programa

Aqui, há duas opções de rodar, uma com gunicorn e outra com o servidor flask, você deverá optar por qualquer uma dessas.

### 3.1 Com flask
```bash
$ python3 app.py
```
#### O site estará online no endereço padrão localhost:8050
<br>

### 3.2 Com gunicorn
```bash
$ gunicorn app:server
```
#### O site estará online no endereço padrão localhost:8000