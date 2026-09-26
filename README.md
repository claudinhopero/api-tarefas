# API de Tarefas

API REST para gerenciamento de tarefas, desenvolvida em Python.

## Tecnologias

- Python

## Ferramentas

- pip
- git

## Funcionalidades

- [ ] Criar uma tarefa
- [ ] Listar tarefas
- [ ] Buscar tarefa por ID
- [ ] Atualizar uma tarefa
- [ ] Marcar tarefa como concluída
- [ ] Excluir tarefa

## Estrutura do Projeto

```text
api-tarefas/
│
├──app/
│ ├──__init__.py
│ ├──main.py
│ |
│ ├──routers/
│ │ ├──__init__.py
│ │ └──tarefas.py
│ │ 
│ ├──schemas/
│ │ ├──__init__.py
│ │ └──tarefa.py
│ |
│ ├──services/
│ │ ├──__init__.py
│ │ └──tarefa_service.py
│ |
│ └──database/
│   ├──__init__.py
│   └──memoria.py
|
├──tests/
│ ├──__init__.py
│ └──test_tarefas.py
|
├──requirements.txt
├──.gitignore
└──README.md



