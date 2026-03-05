# AWS Lambda Python API

## Descrição

Este projeto consiste em uma API backend desenvolvida em Python e hospedada na AWS utilizando AWS Lambda.  

O objetivo foi criar uma aplicação serverless com deploy automatizado utilizando CI/CD via GitHub Actions.

A API é exposta através do API Gateway e utiliza formato JSON para comunicação.

## Tecnologias Utilizadas

- Python
- AWS Lambda
- API Gateway
- GitHub
- GitHub Actions (CI/CD)
- JSON

## Como funciona

A aplicação é executada como uma função Lambda na AWS.  
Quando uma requisição é feita via API Gateway, a função é acionada e retorna uma resposta em JSON.

## CI/CD

O projeto possui pipeline automatizada configurada no GitHub Actions:

- Execução de testes automatizados
- Validação do código antes do deploy
- Deploy automático na AWS Lambda
- Uso de secrets para autenticação segura

## Testes

O projeto conta com testes automatizados para validar o funcionamento da função Lambda antes do deploy.

## Deploy

O deploy é realizado automaticamente via GitHub Actions sempre que há push na branch principal de desenvolvimento.

## Autor

Gabriel Chaves Winques
Projeto desenvolvido como prática de backend com AWS, CI/CD e arquitetura serverless.