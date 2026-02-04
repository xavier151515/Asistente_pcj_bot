import os
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler
from telegram.ext import filters

# ⚠️⚠️⚠️ REEMPLAZA ESTO CON TU NUEVO TOKEN ⚠️⚠️⚠️
# Obtén un nuevo token de @BotFather después de revocar el anterior
TOKEN = "8555813721:AAGUPCse67ekXW8QsT_xTP3kHJWOQ3zY1_s"

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Saluda a nuevos miembros que se unen al grupo/canal"""
    
    # Verifica si hay nuevos miembros
    for member in update.message.new_chat_members:
        # Evita saludar al bot si es agregado
        if member.is_bot:
            continue
            
        # Mensaje de bienvenida
        welcome_message = (
            f"¡Bienvenido/a {member.first_name}! 👋\n\n"
            f"Gracias por unirte al grupo/canal.\n"
            f"Estamos contentos de tenerte aquí."
        )
        
        # Enviar el mensaje
        await update.message.reply_text(welcome_message)

def main():
    """Inicia el bot"""
    
    # Crear la aplicación
    app = Application.builder().token(TOKEN).build()
    
    # Solo un handler: para detectar nuevos miembros
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
    
    # Iniciar el bot
    print("🤖 Bot iniciado - Esperando nuevos miembros...")
    print("🛡️  Token protegido")
    app.run_polling()

if __name__ == '__main__':
    main()
