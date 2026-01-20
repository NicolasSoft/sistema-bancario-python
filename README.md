# 🏦 Sistema Bancário em Python (V2)

Projeto desenvolvido como parte do desafio da **Digital Innovation One (DIO)**, com o objetivo de evoluir um sistema bancário simples para uma versão **modular, orientada a objetos, com persistência de dados e testes automatizados**.

Este projeto simula operações bancárias básicas, aplicando boas práticas de engenharia de software utilizadas no mercado.

---

## 🚀 Funcionalidades

✔ Cadastro de clientes  
✔ Criação de múltiplas contas bancárias  
✔ Depósitos com validação  
✔ Saques com regras de negócio:
- Limite de 3 saques diários
- Limite de R$ 500,00 por saque
- Bloqueio por saldo insuficiente  

✔ Emissão de extrato bancário  
✔ Persistência de dados em arquivo JSON  
✔ Testes unitários com Pytest  

---

## 🧠 Conceitos Aplicados

- Programação Orientada a Objetos (POO)
- Separação de responsabilidades (Models / Services)
- Regras de negócio isoladas
- Persistência de dados
- Testes automatizados
- Organização de projeto em camadas
- Boas práticas de versionamento com Git

---

## 📁 Estrutura do Projeto

````
sistema-bancario-v2/
│
├── app.py
├── models/
│ ├── cliente.py
│ └── conta.py
│
├── services/
│ └── banco.py
│
├── data/
│ └── banco.json
│
├── tests/
│ └── test_conta.py
│
├── README.md
└── requirements.txt
````

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Pytest
- JSON (persistência de dados)
- Git & GitHub

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/NicolasSoft/sistema-bancario-v2.git
cd sistema-bancario-v2
```

## 🧪 Executando os Testes
````
Instale o Pytest (caso não tenha):

pip install pytest
````

Execute os testes:
````
pytest
````

## 🔮 Melhorias Futuras

- Interface gráfica ou Web

- API REST com FastAPI ou Flask

- Autenticação de usuários

- Persistência em banco de dados (SQLite / PostgreSQL)

- Relatórios financeiros

- Logs e tratamento avançado de erros

## 👨‍💻 Autor

Desenvolvido por Nicolas Daniel Santos
📌 Desenvolvedor de Software
🔗 GitHub: https://github.com/NicolasSoft