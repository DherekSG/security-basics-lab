# Lab TryHackMe - Introdução ao Nmap

**IP Alvo:** 10.10.10.10  
**Ferramenta:** Nmap  
**Comando usado:** `nmap -sV -sC 10.10.10.10`

## Resultados:
- Porta 22/tcp aberta (SSH)
- Porta 80/tcp aberta (HTTP)

## Possíveis vetores:
- Página web rodando em Apache desatualizado.
- SSH aceitando autenticação por senha.

## Ações sugeridas:
- Realizar brute force na página de login.
- Testar vulnerabilidades conhecidas na versão do Apache.
