# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования

from aiogram import executor, Bot
import handlers, logging, os

logging.basicConfig(filename=os.path.dirname(os.path.realpath(__file__))+'\calc.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

with open(os.path.dirname(os.path.realpath(__file__)) + '/token.txt') as file:
        TOKEN = file.readline().strip()

if len(TOKEN) < 1:
    logger.error('Файл токена не обнаружен')
    exit()

bot = Bot(TOKEN)

async def on_start(_):
    # Вывод в консоль информации о запуске
    logger.info('Бот запущен')
    print('Бот запущен')

if __name__ == '__main__':
    
    executor.start_polling(handlers.dp, skip_updates=True, on_startup=on_start)