#!/bin/bash

# --- PREPARAÇÃO DO SISTEMA (PYTHON) ---
if ! command -v pip &> /dev/null; then
    echo "📦 Instalando ferramentas de sistema..."
    apt update && apt install -y python3-pip python3-dev build-essential libpq-dev
fi

echo "🚀 Instalando dependências do Agente (Python)..."
pip install --no-cache-dir -r /code/agente/requirements.txt || pip install --no-cache-dir -r /code/agente/requirements.txt --break-system-packages

# --- INICIA O AGENTE ---
echo "✅ Iniciando IA Betina..."
cd /code/agente
python3 agent.py dev
