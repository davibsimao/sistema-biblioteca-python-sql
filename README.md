# 📚 Sistema de Biblioteca (Python + MySQL)

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![POO](https://img.shields.io/badge/POO-Oriented%20Programming-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 📌 Descrição

Sistema de biblioteca desenvolvido em Python com MySQL, utilizando arquitetura em camadas (Service / Repository).

O projeto simula um sistema real de gerenciamento de biblioteca via terminal, com regras de negócio e controle de empréstimos.

---

## 🚀 Funcionalidades

### 📚 Livros
- Cadastrar livros  
- Listar livros  
- Listar livros disponíveis  
- Remover livros (com validação de histórico)

### 👤 Leitores
- Cadastrar leitores  
- Listar leitores  
- Remover leitores (com validação de histórico)

### 📖 Empréstimos
- Criar empréstimos  
- Listar empréstimos  
- Devolver livros  
- Controle de status (ATIVO / DEVOLVIDO)

---

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/-Python-blue?logo=python)
![MySQL](https://img.shields.io/badge/-MySQL-orange?logo=mysql)

- Python
- MySQL
- mysql-connector-python
- Programação Orientada a Objetos (POO)
- Arquitetura em camadas (Service / Repository)

---

📁 Estrutura do projeto

biblioteca/
├── main.py
├── utils/
│   └── menu.py
├── services/
│   ├── livro_service.py
│   ├── leitor_service.py
│   └── emprestimo_service.py
├── repositories/
│   ├── livro_repository.py
│   ├── leitor_repository.py
│   ├── emprestimo_repository.py
│   └── conexao.py
---

## 📌 Regras do sistema

- Não é possível remover livros com histórico de empréstimos  
- Não é possível remover leitores com histórico de empréstimos  
- Um livro só pode ser emprestado se existir no sistema  
- Empréstimos possuem status: **ATIVO / DEVOLVIDO**  
- Um empréstimo só pode ser devolvido uma única vez  

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar:

- Python com POO  
- Integração com MySQL  
- Arquitetura em camadas  
- Lógica de regras de negócio  
- CRUD completo em sistema de terminal  

---

## 💻 Menu do sistema

1 - Cadastrar livro  
2 - Cadastrar leitor  
3 - Cadastrar empréstimo  
4 - Listar livros  
5 - Listar leitores  
6 - Listar empréstimos  
7 - Devolver empréstimo  
8 - Remover livro  
9 - Remover leitor  
0 - Sair

---
## 🚀 Futuras melhorias

- Implementação de camada de Models (entidades do sistema como Livro, Leitor e Empréstimo)
- Migração para arquitetura com ORM (ex: SQLAlchemy)
- Transformação do sistema em API REST com FastAPI
- Implementação de autenticação de usuários
- Interface gráfica (GUI)

## 👨‍💻 Autor

**Davi Simão**

Projeto desenvolvido para fins de estudo e evolução em backend com Python + MySQL.