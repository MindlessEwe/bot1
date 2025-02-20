import discord
from discord.ext import commands
import asyncio
from discord.ui import Button, View

# Configuración
TOKEN = 'NzI1NjA1MzM3Njg3OTE2NjA0.GmcHay.mG2cbwEqTQm1tYPKmquKNhdKRjFBjR0VkJ_ePw'  # Reemplaza con el token de tu bot
TICKET_CATEGORY_ID = 1342005188587950121  # Reemplaza con el ID de la categoría donde se crearán los tickets
ROLE_ID = 1342029145445629972


# Intents (permisos para el bot)
intents = discord.Intents.default()
intents.message_content = True  # Necesario para leer el contenido de los mensajes

# Crear el bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Diccionario para almacenar respuestas temporales
ticket_data = {}

# Comando para eliminar mensajes (purge)
@bot.command(name="purge", help="Elimina un número específico de mensajes.")
@commands.has_permissions(manage_messages=True)  # Solo los usuarios con permiso de gestionar mensajes pueden usar este comando
async def purge(ctx, amount: int):
    if amount < 1 or amount > 100:
        await ctx.send("Por favor, especifica un número de mensajes entre 1 y 100.")
        return
    
    deleted = await ctx.channel.purge(limit=amount)  # Elimina los mensajes
    await ctx.send(f"Se han *eliminado {len(deleted)} mensajes*.", delete_after=5)  # Responde y borra el mensaje después de 5 segundos

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Bot listo como {bot.user.name}')

@bot.command()
async def pedidos(ctx):
    await ctx.send("¡Puedes realizar tu pedido en <#1342060366032801864>!")

@bot.command()
async def precios(ctx):
    await ctx.send("¡`Si quieres información de los costos de proyecto visita el canal de` https://discord.com/channels/352928362056122369/701037886887165982 !")
# Iniciar el bot
bot.run(TOKEN)
