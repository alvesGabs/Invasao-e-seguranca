# Segurança em Ambientes Orquestrados com Kubernetes
Este projeto demonstra, na prática, uma vulnerabilidade de segurança crítica classificada no OWASP Top 10: **Security Misconfiguration**. Foi desenvolvido por nosso grupo em sala, com foco na exploração de uma falha de configuração no Redis exposto sem autenticação.

## Objetivo

Simular uma invasão a um serviço Redis mal configurado, exposto publicamente em um cluster Kubernetes local, demonstrando como configurações incorretas podem resultar em **vazamento e manipulação de dados** críticos.

## Tecnologias Utilizadas

- **Kubernetes** (Minikube)
- **Docker**
- **Python + Flask**
- **Redis**
- **redis-py** (client para simulação de ataque)
- **kubectl**

## Estrutura da Arquitetura

- `Flask App`: Interface simples com formulário de entrada de dados.
- `Redis`: Serviço de armazenamento em memória exposto sem autenticação.
- `Script Invasor`: Python script que se conecta diretamente ao Redis exposto.

## Vulnerabilidade Simulada

A falha de segurança está relacionada à **exposição pública do serviço Redis**, sem autenticação e sem restrição de IPs. Isso permite que qualquer ator externo consiga:

- 📥 Consultar chaves (GET)
- 📝 Inserir dados (SET)
- ❌ Deletar entradas (DEL)

A vulnerabilidade demonstra como um pequeno descuido na configuração pode levar a **vazamento, corrupção e perda de integridade dos dados** em uma aplicação.
