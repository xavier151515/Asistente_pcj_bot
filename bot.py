import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Configurar logging para ver errores
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# El token se tomará de la variable de entorno
TOKEN = os.environ.get("8555813721:AAGUPCse67ekXW8QsT_xTP3kHJWOQ3zY1_s")

def welcome(update: Update, context: CallbackContext):
    """Envía mensaje cuando alguien nuevo se une"""
    try:
        for member in update.message.new_chat_members:
            # Mensaje de bienvenida - ¡PERSONALIZA ESTO!
            welcome_message = (
                f"🤖 ¡BIENVENIDO/A {member.first_name} AL CANAL DE ROBÓTICA! 🚀\n\n"
                f"🔧 **Somos una comunidad apasionada por la robótica**\n"
                f"📌 **Revisa los mensajes fijados** para información importante\n"
                f"💡 **Comparte** tus proyectos y preguntas\n"
                f"👥 **Conéctate** con otros entusiastas\n\n"
                f"¡Disfruta tu estadía! ⚡"
            )
            
            # Enviar el mensaje
            update.message.reply_text(welcome_message)
            
            # Log para debugging
            logger.info(f"Nuevo miembro: {member.first_name} (ID: {member.id})")
            
    except Exception as e:
        logger.error(f"Error en welcome: {e}")

def start(update: Update, context: CallbackContext):
    """Comando /start para probar el bot"""
    update.message.reply_text("✅ Bot activo y funcionando correctamente!")

def error(update: Update, context: CallbackContext):
    """Manejo de errores"""
    logger.warning(f'Update {update} causó error {context.error}')

def main():
    """Función principal"""
    if not TOKEN:
        logger.error("❌ ERROR: No se encontró TOKEN_BOT en variables de entorno")
        return
    
    # Crear el updater
    updater = Updater(TOKEN, use_context=True)
    
    # Obtener el dispatcher para registrar handlers
    dp = updater.dispatcher
    
    # Comandos
    dp.add_handler(CommandHandler("start", start))
    
    # Mensajes de bienvenida
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
    
    # Errores
    dp.add_error_handler(error)
    
    # Iniciar el bot
    logger.info("🤖 Bot iniciado correctamente...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
