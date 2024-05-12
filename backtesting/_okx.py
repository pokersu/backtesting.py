from common import get_candles, get_history_candles


def _get_candles(symbol: str, timeframe: str, limit: int = 600):
    candles = get_candles(symbol, timeframe, limit)
    candles = candles.rename(
        columns={'datetime': 'Datetime', 'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close',
                 'volume': 'Volume', 'confirm': 'Confirm'})
    return candles


def _get_history_candles(symbol: str, timeframe: str, limit: int = 600):
    candles = get_history_candles(symbol, timeframe, limit)
    candles = candles.rename(
        columns={'datetime': 'Datetime', 'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close',
                 'volume': 'Volume', 'confirm': 'Confirm'})
    return candles