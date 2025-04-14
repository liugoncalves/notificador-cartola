import os
import re
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def send_whatsapp_message(message):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    message = client.messages.create(
        from_=os.getenv("TWILIO_WHATSAPP_FROM"),
        body=message,
        to=os.getenv("TWILIO_WHATSAPP_TO")
    )
    print(f"Mensagem enviada: {message.sid}")

def get_proxima_partida(indice):
    url = "https://ge.globo.com/futebol/brasileirao-serie-a/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    script = soup.find("script", id="scriptReact")
    if not script:
        print("Script com os dados não encontrado.")
        return None

    script_content = script.string
    match = re.search(r"listaJogos\s*=\s*(\[\{.*?\}\]);", script_content, re.DOTALL)
    if not match:
        print("Não foi possível extrair listaJogos.")
        return None

    try:
        jogos_json = json.loads(match.group(1))
        partidas_futuras = []

        for jogo in jogos_json:
            data_str = jogo.get("data_realizacao")
            if data_str:
                data_jogo = datetime.strptime(data_str, "%Y-%m-%dT%H:%M")
                if data_jogo > datetime.now():
                    partidas_futuras.append({
                        "data": data_jogo,
                        "mandante": jogo["equipes"]["mandante"]["nome_popular"],
                        "visitante": jogo["equipes"]["visitante"]["nome_popular"],
                        "estadio": jogo["sede"]["nome_popular"]
                    })
                
        if len(partidas_futuras) > indice:
            return partidas_futuras[indice]
        else:
            print(f"Não há partida no índice {indice}.")
            return None
                
    except Exception as e:
        print(f"Erro ao processar JSON: {e}")
        return None

    return None

def check_jogo(indice):
    partida = get_proxima_partida(indice)
    if not partida:
        print("Nenhuma partida futura encontrada.")
        return

    agora = datetime.now()
    diff = partida["data"] - agora

    horas_restantes = int(diff.total_seconds() // 3600)
    minutos_restantes = int((diff.total_seconds() % 3600) // 60)

    data_formatada = partida["data"].strftime("%d/%m/%Y às %H:%M")

    if(horas_restantes >= 1):
        mensagem = (
            f"⚠️ ATENÇÃO ⚠️\n\n"
            f"🏆 Brasileirão - Rodada 4\n\n"
            f"📅 Primeira partida: *{partida['mandante']} 🆚 {partida['visitante']}*\n"
            f"⏰ Horário: {data_formatada}\n"
            f"🏟️ Estádio: {partida['estadio']}\n\n"
            f"⌛ Faltam *{horas_restantes} horas* e *{minutos_restantes} minutos* para o fechamento do Mercado do Cartola!"
        )
    
    elif(horas_restantes == 0 ):
        mensagem = (
            f"⚠️ ATENÇÃO ⚠️\n\n"
            f"🏆 Brasileirão - Rodada 4\n\n"
            f"📅 Primeira partida: *{partida['mandante']} 🆚 {partida['visitante']}*\n"
            f"⏰ Horário: {data_formatada}\n"
            f"🏟️ Estádio: {partida['estadio']}\n\n"
            f"⌛ Faltam *{minutos_restantes} minutos* para o fechamento do Mercado do Cartola!"
        )

    send_whatsapp_message(mensagem)

# Executa ao rodar
check_jogo(1)