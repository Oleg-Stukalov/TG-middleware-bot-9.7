import logging

from aiogram import Router
from aiogram.types import Message
from filters.filters import MyTrueFilter, MyFalseFilter

logger = logging.getLogger(__name__)

# Инициализируем роутер уровня модуля
other_router = Router()

# Теперь этот хэндлер не будет срабатывать вообще
### @other_router.message(MyFalseFilter())
# Этот хэндлер будет срабатывать на любые сообщения,
# кроме тех, для которых есть отдельные хэндлеры
@other_router.message(MyTrueFilter())
async def send_echo(message: Message, i18n: dict[str, str]):
    logger.debug('Вошли в эхо-хэндлер')
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        #await message.reply(text=LEXICON_RU['no_echo'])
        await message.reply(text=i18n.get('no_echo'))
    logger.debug('Выходим из эхо-хэндлера')