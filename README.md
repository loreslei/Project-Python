<a id="instalacao"></a>
## 🚀 Instalação (Windows)

### Pré-requisitos

#### Instalações via Navegador:
1. **Python 3.8+**: 
   - Baixe do [site oficial do Python](https://www.python.org/downloads/)
   - Durante a instalação, marque a opção "Add Python to PATH"

2. **Git**: 
   - Baixe do [site oficial do Git](https://git-scm.com/downloads)

3. **Visual Studio Code** (ou outro editor de código):
   - Baixe do [site oficial do VS Code](https://code.visualstudio.com/download)


#### Instalações via Terminal:
Após instalar o Python e acessar o diretório clonado, abra o terminal no VS Code (ou outro editor de código) e execute:

1. **Instalar pip**:
```sh
python -m pip install --upgrade pip
```

2. **Instalar virtualenv**:
```sh
python -m pip install virtualenv
```

3. **Criar ambiente virtual**:
```sh
python -m venv venv
```

4. **Ativar ambiente virtual**:
```sh
venv/Scripts/activate
```

5. **Instalar dependências do projeto**:
```sh
pip install -r requirements.txt
```
