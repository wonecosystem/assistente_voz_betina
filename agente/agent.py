from dotenv import load_dotenv
import os

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import noise_cancellation
from prompts import get_agent_instruction, SESSION_INSTRUCTION

load_dotenv()

AGENT_NAME = os.getenv("AGENT_NAME", "Betina")
USER_NAME = os.getenv("USER_NAME", "")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "google").lower()
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-2.0-flash-live-001")
AGENT_VOICE = os.getenv("AGENT_VOICE", "Kore")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.6"))


def create_llm():
    if LLM_PROVIDER == "openai":
        from livekit.plugins import openai as lk_openai
        return lk_openai.realtime.RealtimeModel(
            model=LLM_MODEL,
            voice=AGENT_VOICE,
            temperature=LLM_TEMPERATURE,
        )
    else:
        from livekit.plugins import google as lk_google
        return lk_google.beta.realtime.RealtimeModel(
            model=LLM_MODEL,
            voice=AGENT_VOICE,
            temperature=LLM_TEMPERATURE,
        )


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=get_agent_instruction(AGENT_NAME, USER_NAME),
            llm=create_llm(),
        )
        


async def entrypoint(ctx: agents.JobContext): # Função de entrada assíncrona para o agente
    session = AgentSession(
        
    )

    await session.start( 
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(# Configurações de entrada da sala
            video_enabled=True, # Habilita vídeo na sala
            noise_cancellation=noise_cancellation.BVC(),#@ Habilita o cancelamento de ruído usando o plugin BVC
        ),
    )

    await ctx.connect()

    await session.generate_reply( 
        instructions=SESSION_INSTRUCTION, # Instruções específicas para a sessão
    )


if __name__ == "__main__":# Ponto de entrada do script
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))# Executa o aplicativo de agente com a função de entrada definida
