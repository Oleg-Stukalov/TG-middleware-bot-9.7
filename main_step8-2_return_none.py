import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers.other import other_router
from handlers.user import user_router
from middlewares.inner import (
    FirstInnerMiddleware,
    SecondInnerMiddleware,
    ThirdInnerMiddleware,
)
from middlewares.outer import (
    FirstOuterMiddleware,
    SecondOuterMiddleware,
    ThirdOuterMiddleware,
)

# Настраиваем базовую конфигурацию логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
           '%(lineno)d - %(name)s - %(message)s'
)

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main() -> None:

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # Регистрируем роутеры в диспетчере
    dp.include_router(user_router)
    dp.include_router(other_router)

    # Здесь будем регистрировать миддлвари
    '''тобы получить поведение, о котором я не договорил в этом шаге -
    вам нужно в вашей миддлвари FirstOuterMiddleware последнюю строчку
    изменить на return # result, то есть вместо result миддлварь будет
    возвращать None, а также поменять ее регистрацию на
    такую: user_router.message.outer_middleware(FirstOuterMiddleware()).
    После этого у вас бот будет реагировать на команду /start, но
    не будет реагировать на любой другой текст, потому что
    хэндлер send_echo зарегистрирован на другом роутере.'''
    ###dp.update.outer_middleware(FirstOuterMiddleware())
    user_router.message.outer_middleware(FirstOuterMiddleware())
    user_router.callback_query.outer_middleware(SecondOuterMiddleware())
    other_router.message.outer_middleware(ThirdOuterMiddleware())
    user_router.message.middleware(FirstInnerMiddleware())
    user_router.callback_query.middleware(SecondInnerMiddleware())
    other_router.message.middleware(ThirdInnerMiddleware())


    # Запускаем polling
    await dp.start_polling(bot)


asyncio.run(main())