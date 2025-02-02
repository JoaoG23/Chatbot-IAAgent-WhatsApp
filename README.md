## Chatbot IA - WhatsApp 🤖

<img src="./assets/icon.ico" align="right">

### 1. Introdução  

**Tempo estimado:** 16 horas

Este projeto automatiza a interação com usuários via WhatsApp utilizando IA (Gemini ou Copilot). O sistema captura mensagens recebidas, processa a solicitação através de uma IA selecionada e retorna a resposta ao usuário.

### 2. Tecnologias Utilizadas 📲  

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Google Chrome](https://img.shields.io/badge/Google_Chrome-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://www.google.com/chrome/)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Webdriver Manager](https://img.shields.io/badge/Webdriver_Manager-20232A?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/webdriver-manager/)
[![Gemini AI](https://img.shields.io/badge/Gemini_AI-ff9800?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Copilot](https://img.shields.io/badge/Copilot-24A148?style=for-the-badge&logo=github&logoColor=white)](https://github.com/features/copilot)

### 3. Estrutura do Projeto 📂  

```
├── logs/                 # Armazena logs do sistema
├── src/                  # Código-fonte principal
├── templates/            # Templates de mensagens (se necessário)
├── __init__.py           # Arquivo principal do projeto
├── .env                  # Configurações do ambiente
├── .gitignore            # Arquivos ignorados pelo Git
├── LICENSE               # Licença do projeto
├── README.md             # Documentação do projeto
├── requirements.txt      # Dependências do projeto
```

### 4. Instalação 🛠️  

#### Passos para instalar:  

1. Clone o repositório:  
   ```bash  
   git clone https://github.com/JoaoG23/chatbot-whatsapp-ia.git  
   ```  
2. Instale as dependências:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Crie um arquivo `.env` com o seguinte conteúdo:  
   ```env  
   AI_USERNAME=''  # Se necessário
   AI_PASSWORD=''
   
   PATH_USER_PROFILE_CHROME="C:\\Users\\joaog\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
   IA_MODEL='gemini'  # Modelos suportados: 'gemini', 'copilot'
   
   AI_TOKEN=''  # Token de autenticação da IA
   ```  
4. Execute o sistema:
   ```bash  
   python __init__.py  
   ```  

### 5. Funcionalidades ✔️  

- [x] Acessa o WhatsApp Web.
- [x] Aguarda o usuário fazer login com QR Code.
- [x] Captura mensagens recebidas em tempo real.
- [x] Identifica o questionamento do usuário.
- [x] Verifica qual IA foi selecionada.
- [x] Envia a mensagem para a IA com base no prompt.
- [x] Retorna a resposta ao WhatsApp e finaliza a interação.

### 6. Benefícios e Limitações 🛠️  

#### Benefícios:  
- Automatiza o atendimento via WhatsApp.
- Permite escalabilidade com múltiplos modelos de IA.
- Baixo acoplamento graças ao padrão Adapter.

#### Limitações:  
- Necessário acesso à internet.
- Restrições de segurança do WhatsApp Web podem afetar o funcionamento.

### 7. Autor  

 <img style="border-radius:50%;" src="https://avatars.githubusercontent.com/u/80895578?v=4" width="100px;" alt=""/>  
 <br />  
 <sub><b>Joao Guilherme</b></sub></a> <a href="https://github.com/JoaoG23/">🚀</a>  

Desenvolvido com 🤖 por Joao Guilherme 👋🏽 Entre em contato:  

[![Linkedin Badge](https://shields.io/badge/-Joao%20Guilherme-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/joaog123/)](https://www.linkedin.com/in/joaog123/)  
[![Email Badge](https://shields.io/badge/-joaoguilherme94@live.com-c80?style=flat-square&logo=Microsoft&logoColor=white&link=mailto:joaoguilherme94@live.com)](mailto:joaoguilherme94@live.com)  

## 8. Licença 📄  

[![License](https://shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)  

