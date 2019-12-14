from gemini_bot.cli.commands.public import (
    Symbols,
    GetTicker,
    GetCurrentOrderBook,
    GetTradeHistory,
    GetAuctionHistory,
)

from gemini_bot.cli.commands.private import (
    GetBalance
)

from gemini_bot.cli.commands.status import Status

commands = [
    Symbols,
    GetTicker,
    GetCurrentOrderBook,
    GetTradeHistory,
    GetAuctionHistory,
    Status,
    GetBalance,
]
