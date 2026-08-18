import { BadRequestException, Inject, Injectable } from '@nestjs/common';
import type { MarketDataProvider } from './market-data.provider';
import type { Candle } from 'src/types/candle';
import { MARKET_DATA_PROVIDER } from './market-data.tokens';

@Injectable()
export class MarketDataService {
  constructor(
    @Inject(MARKET_DATA_PROVIDER)
    private readonly marketDataProvider: MarketDataProvider,
  ) {}
  getCandles(
    symbol: string,
    timeframe: '1m' | '5m',
    from: string,
    to: string,
  ): Promise<Candle[]> {
    const fromDate = new Date(from);
    const toDate = new Date(to);

    if (fromDate >= toDate) {
      throw new BadRequestException('`from` must be earlier than `to`');
    }
    return this.marketDataProvider.getCandles(symbol, timeframe, from, to);
  }
}
