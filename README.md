📌 Projeto Par

📖 Descrição
Este projeto tem como objetivo verificar se um número é par ou ímpar, utilizando Python e testes automatizados com pytest. 
Ele também conta com integração contínua via GitHub Actions para garantir a qualidade do código.

🚀 Tecnologias utilizadas
Python 3.10+

pytest (para testes automatizados)

GitHub Actions (para CI/CD)

📂 Estrutura do projeto

bash

Copiar

Editar

📦 meu_projeto

├── 📂 fonte            # Código-fonte do projeto

│   ├── __init__.py

│   ├── matematica.py   # Função que verifica se um número é par

├── 📂 testes           # Testes automatizados

│   ├── __init__.py

│   ├── test_matematica.py

├── 📂 .github/workflows # Configuração do GitHub Actions

│   ├── python-ci.yml

├── README.md           # Documentação do projeto

└── .gitignore          # Arquivos ignorados pelo Git

⚙️ Instalação

Para executar este projeto localmente, siga os passos abaixo:

Clone o repositório

bash

Copiar

Editar

git clone https://github.com/skazinx/Par.git

cd Par

Crie um ambiente virtual (opcional, mas recomendado)

bash

Copiar

Editar

python -m venv venv

source venv/bin/activate  # Linux/macOS

venv\Scripts\activate      # Windows

Instale as dependências

bash

Copiar

Editar

pip install -r requirements.txt

📌 Uso

A função principal está localizada em fonte/matematica.py e pode ser usada da seguinte forma:

python

Copiar

Editar

from fonte.matematica import eh_par

numero = 4

if eh_par(numero):
    print(f"{numero} é um número par!")
    
else:
    print(f"{numero} é um número ímpar!")
    
Saída esperada:

Copiar

Editar

4 é um número par!

✅ Testes

Os testes foram escritos usando pytest. Para executá-los, use o comando:

bash

Copiar

Editar

pytest tests/

Se todos os testes passarem, você verá uma saída semelhante a esta:

bash

Copiar

Editar

============================= test session starts ==============================

platform linux -- Python 3.10.16, pytest-8.3.5, pluggy-1.5.0

collected 2 items

tests/test_matematica.py ..    [100%]

========================== 2 passed in 0.14s ==========================

🔄 Integração Contínua

Este projeto usa GitHub Actions para rodar os testes automaticamente a cada novo commit. O fluxo de trabalho está definido em .github/workflows/python-ci.yml.

📌 Contribuição:

Se você quiser contribuir, siga estes passos:

Faça um fork do projeto

Crie uma nova branch (git checkout -b minha-feature)

Faça as alterações necessárias

Realize o commit das mudanças (git commit -m "Minha nova feature")

Envie para o repositório remoto (git push origin minha-feature)

Crie um Pull Request

📧 Contato

Caso tenha dúvidas ou sugestões, sinta-se à vontade para entrar em contato!

Gmail: leonardomabreu09@gmail.com

🚀 Bons códigos! 🚀
