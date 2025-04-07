# 📲 Notificador do Fechamento do Mercado do Cartola FC

Projeto que **envia automaticamente uma notificação no WhatsApp** avisando sobre a primeira partida da rodada do Brasileirão, ajudando a lembrar que o **Mercado do Cartola FC fecha 1 minuto antes do jogo inicial da rodada**.

A notificação é enviada de forma automática e personalizada, contendo times, data, horário, estádio e quanto tempo falta para o fechamento.

🔗 Repositório: [https://github.com/liugoncalves/notificador-cartola](https://github.com/liugoncalves/notificador-cartola)

---

## ⚙️ Como funciona?

1. O script acessa a página oficial do Brasileirão no site do ge.globo.com.
2. Extrai as informações da rodada atual e a próxima partida agendada.
3. Calcula quanto tempo falta até o jogo.
4. Envia uma mensagem formatada via WhatsApp usando a API do Twilio.

---

## 🧰 Tecnologias utilizadas

- **Python 3.10+** – linguagem principal do projeto.
- `requests` – para fazer requisições HTTP à página do Brasileirão.
- `beautifulsoup4` – para extrair e parsear dados HTML da página.
- `twilio` – para enviar mensagens via WhatsApp.
- `python-dotenv` – para carregar variáveis sensíveis (como tokens) de forma segura a partir de um arquivo `.env`.

---

## ✅ Instalação

### Crie um ambiente virtual (opcional):

```bash
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
```

### Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração

Crie um arquivo `.env` na raiz com as seguintes variáveis:

```ini
TWILIO_SID=seu_twilio_sid
TWILIO_AUTH_TOKEN=seu_twilio_auth_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
TWILIO_WHATSAPP_TO=whatsapp:+55SEUNUMERO
```

---

## ▶️ Execução

Execute o script principal:

```bash
python scrap-brasileirao.py
```

A notificação será enviada automaticamente para o número de WhatsApp configurado.

---

## 💬 Exemplo de mensagem

```swift
🏆 Brasileirão - Rodada 3

📅 Primeira partida: Bragantino 🆚 Botafogo  
⏰ Horário: 12/04/2025 às 16:00  
🏟️ Estádio: Nabi Abi Chedid  

⌛ Faltam 2 dias e 4 horas para o fechamento do Mercado do Cartola!
```

---

## 📂 Arquivo requirements.txt

```txt
requests        # Usado para fazer requisições HTTP ao site do ge.globo  
beautifulsoup4   # Usado para extrair informações do HTML da página  
twilio          # Usado para enviar mensagens via API do WhatsApp  
python-dotenv     # Usado para carregar variáveis do arquivo .env  
```

---

## 🤝 Contribuições

Contribuições são muito bem-vindas!  
Se quiser sugerir melhorias, reportar bugs ou adicionar novas funcionalidades, sinta-se à vontade para abrir uma issue ou um pull request.
