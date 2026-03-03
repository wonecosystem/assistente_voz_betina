# Betina — Assistente de Voz com IA

Agente de voz inteligente construído com **LiveKit Agents** e modelos de linguagem da **Google (Gemini)** ou **OpenAI (GPT-4o)**. Direta, sarcástica, técnica e leal.

---

## O que é isso?

Este é o agente base (v1) do projeto Betina. Ele roda em tempo real via WebRTC, processa áudio e vídeo do usuário e responde com voz sintetizada, usando o modelo de linguagem configurado.

**Funcionalidades desta versão:**
- Conversa por voz em tempo real
- Suporte a vídeo (câmera do usuário)
- Cancelamento de ruído (plugin BVC da LiveKit)
- Persona customizável via variáveis de ambiente
- Suporte a Google Gemini e OpenAI GPT-4o Realtime

---

## Requisitos

- Python 3.10+
- Conta no LiveKit Cloud (veja abaixo)
- Chave de API do Google Gemini ou OpenAI (veja abaixo)

Dar autorização de escrita e gravação
chmod +x start.sh

./start.sh

---

## Criando as contas e chaves necessárias

### LiveKit — o que é e como criar sua conta

O **LiveKit** é a infraestrutura de comunicação em tempo real que conecta o navegador do usuário ao agente de IA. Ele gerencia o transporte de áudio e vídeo via WebRTC — sem ele, o agente não consegue ouvir nem falar com o usuário.

Em resumo: é o "canal" por onde a voz trafega entre você e a Betina.

1. Acesse [https://cloud.livekit.io/login](https://cloud.livekit.io/login) e crie sua conta gratuita
2. Crie um novo projeto
3. Vá em **Settings → API Keys** e gere uma chave
4. Copie os três valores para o `.env`:
   - `LIVEKIT_URL` — endpoint WebSocket do projeto (ex: `wss://seu-projeto.livekit.cloud`)
   - `LIVEKIT_API_KEY`
   - `LIVEKIT_API_SECRET`

### Google Gemini — chave de API

O **Gemini** é o modelo de linguagem que alimenta a inteligência da Betina — ele processa o que você fala e gera as respostas em tempo real com voz sintetizada.

1. Acesse [https://aistudio.google.com/api-keys](https://aistudio.google.com/api-keys)
2. Clique em **Create API Key**
3. Copie a chave e adicione no `.env` como `GOOGLE_API_KEY`

---

## Infraestrutura recomendada

Este projeto foi hospedado em uma **VPS com [EasyPanel](https://easypanel.io)** — painel de controle simples para gerenciar containers e serviços na sua própria máquina virtual.

> ⚠️ **Requisito mínimo: 10 GB de RAM**
> O agente sozinho consome aproximadamente **5 GB de RAM** em execução. Recomenda-se uma VPS com no mínimo 10 GB para rodar com estabilidade.

---

## Instalação

### 1. Atualizar a VPS

Antes de instalar qualquer coisa, atualize os pacotes do sistema:

```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Instalar o Python 3

Verifique se o Python já está instalado:

```bash
python3 --version
```

Se não estiver instalado:

```bash
sudo apt install -y python3 python3-pip python3-venv
```

### 3. Instalar as dependências do projeto

```bash
pip3 install -r requirements.txt
```

---

## Configuração

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
cp .env.example .env
```

Edite o `.env` com suas chaves:

```env
LIVEKIT_URL=wss://seu-projeto.livekit.cloud
LIVEKIT_API_KEY=sua_api_key
LIVEKIT_API_SECRET=seu_api_secret

LLM_PROVIDER=google   # google ou openai
GOOGLE_API_KEY=       # se usar Google
OPENAI_API_KEY=       # se usar OpenAI

AGENT_NAME=Betina
AGENT_VOICE=Kore
LLM_TEMPERATURE=0.6
```

### Modelos suportados

| Provider | Modelo | Obs |
|---|---|---|
| Google | `gemini-2.5-flash-native-audio-latest` | Melhor qualidade de áudio |
| Google | `gemini-2.0-flash-exp-image-generation` | Suporte a vídeo/câmera |
| OpenAI | `gpt-4o-realtime-preview` | — |

---

## Como rodar

```bash
python3 agent.py dev
```

Para conectar ao agente, use o [LiveKit Agents Playground](https://agents-playground.livekit.io) com as credenciais do seu projeto.

---

## Estrutura do projeto

```
agente/
├── agent.py          # Entrypoint do agente LiveKit
├── prompts.py        # Persona e instruções do agente
├── requirements.txt  # Dependências Python
└── .env              # Credenciais (não versionar)
```

---

## Versão PRO

Esta é a versão gratuita e open source do Betina — sem memória persistente e sem integrações externas.

A **versão PRO** inclui:

- 🧠 **Memória de longo prazo** — o agente lembra de conversas anteriores entre sessões
- 🔗 **Integrações via tools** — consulta de clientes, faturas, WhatsApp, clima, bolsa de valores, câmbio e muito mais
- ⚙️ **Skills customizáveis** — adicione suas próprias integrações com APIs e sistemas internos
- 🎙️ **Persona personalizada** — nome, voz e comportamento adaptados ao seu negócio

Interessado na versão PRO? Entre em contato:

**Glauco Martins**
📱 [(27) 99867-0627](https://wa.me/5527998670627)

---

## Recursos Gratuitos para Rodar o Projeto

Tutoriais em vídeo para montar toda a infraestrutura sem gastar nada:

### Claude Code (IA para desenvolvimento) — Grátis
Crie sua conta gratuita na Anthropic via Bons.ai e ganhe créditos para usar o Claude Code:

- Cadastro gratuito: [https://auth.trybons.ai](https://auth.trybons.ai)
- Tutorial completo: [Como usar o Claude Code de Graça](https://youtu.be/RyjeLQzUaDU?si=mwoujjsYuHpvWSon&t=321)

### Tokens OpenAI Gratuitos
Aprenda a resgatar tokens diários no Playground da OpenAI:

- [Aprenda a Ganhar Tokens Grátis Diários no Playground da OpenAI](https://www.youtube.com/watch?v=Y4e84pzcKfk)

### VPS Gratuita com EasyPanel
Monte seu servidor na nuvem 100% grátis e instale o EasyPanel para gerenciar o agente com facilidade — exatamente como este projeto foi hospedado:

- [Monte sua VPS 100% Grátis](https://www.youtube.com/watch?v=Kks12MBOOdc)

---

## Licença

Uso livre para fins pessoais e educacionais.
