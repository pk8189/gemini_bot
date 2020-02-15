from gemini_bot.cli.commands.public import (
    Symbols,
    GetTicker,
    GetCurrentOrderBook,
    GetLast500Trades,
    GetAuctionHistory,
)

from gemini_bot.cli.commands.private import (
    GetBalance,
    NewOrder,
)

from gemini_bot.cli.commands.status import Status

commands = [
    Symbols,
    GetTicker,
    GetCurrentOrderBook,
    GetLast500Trades,
    GetAuctionHistory,
    Status,
    GetBalance,
    NewOrder,
]
