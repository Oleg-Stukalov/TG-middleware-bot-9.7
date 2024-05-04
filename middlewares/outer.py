import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

logger = logging.getLogger(__name__)


class FirstOuterMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        logger.debug(
            'Вошли в миддлварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )

        result = await handler(event, data)

        logger.debug('Выходим из миддлвари  %s', __class__.__name__)

        '''При этом, если вы выведите на мечать в миддлвари result,
        то вы увидите None. Но return None, как оказывается, не то же самое,
        что return result. В общем, не совсем очевидное поведение.'''

        print('RESULT!!!: ', result)
        ###return #result
        return result
        ###return None


class SecondOuterMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        logger.debug(
            'Вошли в миддлварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )

        result = await handler(event, data)

        logger.debug('Выходим из миддлвари  %s', __class__.__name__)

        return result


class ThirdOuterMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        logger.debug(
            'Вошли в миддлварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )

        result = await handler(event, data)

        logger.debug('Выходим из миддлвари  %s', __class__.__name__)

        return result