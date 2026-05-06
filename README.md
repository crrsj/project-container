# 📦 Client Management - System Container

Este é o repositório principal do sistema **Client Management**, desenvolvido com foco em **Python/Django** e estruturado para rodar inteiramente em containers. O projeto utiliza **Git Submodules** para isolar a interface e **Dev Containers** para garantir um ambiente de desenvolvimento padronizado e profissional.

## 🚀 Tecnologias e Conceitos Aplicados

*   **Backend:** Python 3.x com Django REST Framework.
*   **Frontend:** Interface de gerenciamento (mantida como um submódulo independente).
*   **Infraestrutura:** Docker & Docker Compose.
*   **Ambiente de Dev:** VS Code Dev Containers (Python 3 & Linux).
*   **Arquitetura:** Princípios SOLID, Clean Code e DRY.

---

## 🛠️ Estrutura do Projeto

A arquitetura foi desenhada de forma modular para facilitar a manutenção:

*   `/api`: Lógica de negócio e persistência de dados.
*   `/frontend`: Submódulo vinculado ao repositório de interface.
*   `/.devcontainer`: Configuração do ambiente de desenvolvimento isolado.
*   `/setup`: Configurações globais do projeto Django.

---

## 📡 API Endpoints

A API foi desenhada para ser simples e eficiente, contando com os seguintes endpoints principais:

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| **GET** | `/clients/` | Lista todos os clientes cadastrados. |
| **POST** | `/clients/saving/` | Realiza o cadastro de um novo cliente. |
| **DELETE** | `/clients/deleting/<id>/` | Remove um cliente específico do sistema. |

---

## ⚙️ Como Rodar o Projeto

### 1. Clonando o Repositório
Como este projeto utiliza submódulos, utilize o parâmetro `--recursive`:
```bash
git clone --recursive [https://github.com/crrsj/project-container.git](https://github.com/crrsj/project-container.git)
```

<img width="1920" height="1080" alt="proj1" src="https://github.com/user-attachments/assets/4eaf9a36-4dda-46a4-abe5-ccb42b8121a8" />

<img width="1920" height="1080" alt="proj2" src="https://github.com/user-attachments/assets/ed193b0a-33db-4f4d-b480-f81d1153d704" />

<img width="1920" height="1080" alt="proj3" src="https://github.com/user-attachments/assets/12dd1085-f50b-41af-83cf-5e37c825f9fc" />

<img width="1920" height="1080" alt="proj4" src="https://github.com/user-attachments/assets/48e4063a-0b38-4b9f-ae6d-b9c18e06a2d3" />

<img width="1920" height="1080" alt="proj5" src="https://github.com/user-attachments/assets/62564530-2496-4827-b283-acbc52621ea6" />




