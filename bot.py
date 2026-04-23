import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# --- SISTEMA PARA O RENDER NÃO DORMIR ---
app = Flask('')
@app.route('/')
def home(): return "Bot Souza Supply & Otimização Online!"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive(): Thread(target=run).start()

# --- CONFIGURAÇÃO ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# ID da Categoria que você mandou
ID_CATEGORIA_TICKETS = 1496994652472086719 

@bot.event
async def on_ready():
    print(f'✅ Tudo pronto! Bot logado como {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="Souza Supply | !loja"))

# --- SISTEMA DE TICKET (VENDAS) ---

class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None) # Botão nunca expira

    @discord.ui.button(label="🛒 Comprar / Abrir Ticket", style=discord.ButtonStyle.green, custom_id="ticket_button")
    async def open_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        categoria = guild.get_channel(ID_CATEGORIA_TICKETS)
        
        if not categoria:
            await interaction.response.send_message("❌ Erro: Categoria de tickets não encontrada.", ephemeral=True)
            return

        # Cria o canal privado
        ticket_channel = await guild.create_text_channel(
            name=f"pedido-{interaction.user.name}",
            category=categoria
        )

        # Permissões: Ninguém vê, só o cliente e quem tem cargo de Staff/ADM
        await ticket_channel.set_permissions(guild.default_role, read_messages=False)
        await ticket_channel.set_permissions(interaction.user, read_messages=True, send_messages=True)

        await interaction.response.send_message(f"✅ Ticket aberto! Vá em {ticket_channel.mention} para finalizar.", ephemeral=True)

        # Mensagem de boas-vindas no ticket
        embed = discord.Embed(
            title="📦 Novo Pedido - Souza Supply",
            description=f"Olá {interaction.user.mention}, bem-vindo ao suporte de vendas!\n\n**O que fazer agora?**\n1. Mande o nome do produto que você quer.\n2. Aguarde o retorno para o pagamento via Pix.\n3. Mande o comprovante aqui mesmo.",
            color=0xA020F0
        )
        await ticket_channel.send(embed=embed)

@bot.command()
async def loja(ctx):
    embed = discord.Embed(
        title="🛍️ SOUZA SUPPLY - STREETWEAR",
        description="As melhores peças com o estilo de Lauro de Freitas.\n\n🔥 **Catálogo:**\n- Camiseta Blessed Angel: R$ 89,90\n- Conjunto Syna World: R$ 249,90\n- Boné Souza Brand: R$ 59,90",
        color=0xA020F0
    )
    await ctx.send(embed=embed, view=TicketView())

# --- COMANDOS DE OTIMIZAÇÃO (FPS BOOST) ---

@bot.command()
async def otimizar(ctx):
    embed = discord.Embed(
        title="🚀 MK OTIMIZAÇÃO - HUB",
        description="Comandos para aumentar o FPS no seu Ryzen ou PC Gamer!",
        color=0x00FF00
    )
    embed.add_field(name="⚡ !fps", value="Melhora a resposta do sistema.", inline=True)
    embed.add_field(name="📶 !ping", value="Limpa o cache da internet.", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def fps(ctx):
    msg = (
        "**Comando de Registro (GameDVR Off):**\n"
        "```cmd\nreg add \"HKCU\\System\\GameConfigStore\" /v \"GameDVR_Enabled\" /t REG_DWORD /d 0 /f```\n"
        "Use no CMD como Administrador!"
    )
    await ctx.send(msg)

@bot.command()
async def ping(ctx):
    await ctx.send("📡 **Resetando Rede:**\n```cmd\nipconfig /flushdns\nnetsh winsock reset```")

# --- START ---
keep_alive()
bot.run('SEU_TOKEN_AQUI')
