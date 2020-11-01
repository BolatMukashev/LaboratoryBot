from .inline_handler import dp
from .admin_handlers import dp
from .handlers import dp
from .instructions_handlers import dp
from .inline_machine_handlers.asfalt import dp
from .inline_machine_handlers.beton import dp
from .inline_machine_handlers.grunt import dp
from .inline_machine_handlers.otsev import dp
from .inline_machine_handlers.sheben import dp
from .inline_machine_handlers.settings import dp
from .inline_machine_handlers.miner_poroshok import dp

# .inline_handlers - это тоже самое что и handlers.inline_handlers (где handlers это папка)


__all__ = ['dp']
