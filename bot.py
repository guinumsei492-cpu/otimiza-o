import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# --- SISTEMA PARA O RENDER NÃO DORMIR ---
app = Flask('')
@app.route('/')
def home(): 
    return "Souza Supply Bot Online!"

def run(): 
    app.run(host='0.0.0.0', port=8080)

def keep_alive(): 
    Thread(target=run).start()

# --- CONFIGURAÇÃO ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# ID da Categoria que você mandou para os Tickets
ID_CATEGORIA_TICKETS = 1496994652472086719 

@bot.event
async def on_ready():
    print(f'✅ Logado com sucesso como {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="Souza Supply | !loja"))

# --- SISTEMA DE TICKET (VENDAS) ---
class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🛒 Comprar / Abrir Ticket", style=discord.ButtonStyle.green, custom_id="ticket_btn")
    async def open_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        categoria = guild.get_channel(ID_CATEGORIA_TICKETS)
        
        if not categoria:
            await interaction.response.send_message("❌ Erro: Categoria não encontrada. Fale com o Souza!", ephemeral=True)
            return

        # Cria o canal privado
        ticket_channel = await guild.create_text_channel(
            name=f"pedido-{interaction.user.name}",
            category=categoria
        )

        # Permissões: Ninguém vê, só o cliente e quem tem cargo de Staff/ADM
        await ticket_channel.set_permissions(guild.default_role, read_messages=False)
        await ticket_channel.set_permissions(interaction.user, read_messages=True, send_messages=True)

        await interaction.response.send_message(f"✅ Ticket aberto! Vá em {ticket_channel.mention} para fechar seu pedido.", ephemeral=True)

        embed = discord.Embed(
            title="📦 Souza Supply - Novo Pedido",
            description=f"Olá {interaction.user.mention}!\n\nEnvie o nome do produto e o comprovante do Pix aqui para finalizarmos sua compra.",
            color=0xA020F0
        )
        await ticket_channel.send(embed=embed)

@bot.command()
async def loja(ctx):
    embed = discord.Embed(
        title="🛍️ SOUZA SUPPLY - STREETWEAR",
        description="Escolha sua peça e clique no botão abaixo para comprar!",
        color=0xA020F0
    )
    embed.add_field(name="👕 Camiseta Blessed Angel", value="R$ 89,90", inline=False)
    embed.add_field(name="🧥 Conjunto Syna World", value="R$ 249,90", inline=False)
    await ctx.send(embed=embed, view=TicketView())

# --- COMANDOS DE OTIMIZAÇÃO ---
@bot.command()
async def otimizar(ctx):
    embed = discord.Embed(
        title="🚀 MK OTIMIZAÇÃO",
        description="Use `!fps` para comandos de registro ou `!ping` para rede.",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command()
async def fps(ctx):
    await ctx.send("**CMD (Adm):**\n```cmd\nreg add \"HKCU\\System\\GameConfigStore\" /v \"GameDVR_Enabled\" /t REG_DWORD /d 0 /f```")

@bot.command()
async def ping(ctx):
    await ctx.send("**Reset de Rede:**\n```cmd\nipconfig /flushdns\nnetsh winsock reset```")

# --- LIGANDO O BOT ---
keep_alive() # Mantém o Render acordado
TOKEN_NOVO = "COLOQUE_O_NOVO_TOKEN_AQUI" # COLOQUE O TOKEN QUE VOCÊ RESETOU AQUI
bot.run(TOKEN_NOVO)
