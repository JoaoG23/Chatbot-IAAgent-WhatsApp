# Chatbot-IAAgent-WhatsApp-To-Copilot 🤖💬

## Introdução

Este projeto automatiza o envio e recebimento de mensagens via WhatsApp Web, utilizando inteligência artificial para gerar respostas. A comunicação com a IA ocorre via integração com a plataforma Copilot.

Time: 14 hs
---

## Tecnologias Utilizadas 🛠️

- **Python**
- **Selenium**
- **webdriver-manager**
- **Google Chrome**

---

## Configuração ✨

### Arquivo `.env`
Antes de iniciar, crie o arquivo `.env` com as seguintes variáveis:

```env
AI_USERNAME=''
AI_PASSWORD=''
PATH_USER_PROFILE_CHROME="C:\\Users\\joaog\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
```

---

## Tarefas Implementadas ✔️

1. **Login no WhatsApp Web**
   - A automação realiza o login no WhatsApp utilizando o perfil do usuário já configurado no Chrome.

2. **Verificação de Mensagens**
   - Detecta mensagens não lidas no WhatsApp.

3. **Login na IA (Copilot)**
   - Faz login na plataforma Copilot com as credenciais fornecidas.

4. **Interação com Mensagens**
   - Envia uma mensagem de boas-vindas ao contato.
   - Captura a última pergunta recebida.
   - Gera uma resposta através da IA.

5. **Envio de Respostas**
   - Retorna a resposta gerada pela IA ao contato no WhatsApp.

6. **Controle FIFO**
   - Gerencia a ordem de resposta das mensagens, priorizando a ordem de chegada.

7. **Intervalo de Respostas**
   - Define um intervalo randômico entre 5 a 10 segundos entre cada resposta.

8. **Ignorar Alertas**
   - Pula qualquer alerta ou quadro pop-up para garantir a fluidez do processo.

---

## Observações

1. Nunca escreva o seu prompt entre ""

---

## Requisitos

1. **Google Chrome**  
   Certifique-se de que o navegador está instalado e configurado com o perfil correto.

2. **Dependências Python**  
   Instale os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execução**
   Rode o script principal:
   ```bash
   python __init__.py
   ```

---

## Benefícios 💡

- **Automatização Completa:** Gerencia mensagens do WhatsApp automaticamente, com respostas geradas por IA.
- **Otimização de Tempo:** Processa várias mensagens simultaneamente, respeitando a ordem de chegada.
- **Integração Direta com Copilot:** Garante respostas rápidas e inteligentes.

---

## Possíveis Melhorias 🚀

- Implementar logs detalhados para auditoria de mensagens enviadas e recebidas.
- Adicionar tratamento de erros para conexões instáveis ou interrupções no login.
- Incluir suporte para personalização de mensagens de boas-vindas e respostas.


## Autor  

 <img style="border-radius:50%;" src="https://avatars.githubusercontent.com/u/80895578?v=4" width="100px;" alt=""/>  
 <br />  
 <sub><b>Joao Guilherme</b></sub></a> <a href="https://github.com/JoaoG23/">🚀</a>  

Developed with 🤖 by Joao Guilherme 👋🏽 Contact me via:  

[![Linkedin Badge](https://shields.io/badge/-Joao%20Guilherme-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/joaog123/)](https://www.linkedin.com/in/joaog123/)  
[![Email Badge](https://shields.io/badge/-joaoguilherme94@live.com-c80?style=flat-square&logo=Microsoft&logoColor=white&link=mailto:joaoguilherme94@live.com)](mailto:joaoguilherme94@live.com)  

## License 📄  

[![License](https://shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENCE)
