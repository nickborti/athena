import type { Candle } from 'src/types/candle';

export interface MarketDataProvider {
  getCandles(
    symbol: string,
    timeframe: '1m' | '5m',
    from: string,
    to: string,
  ): Promise<Candle[]>;
}
