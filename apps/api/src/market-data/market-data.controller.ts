import { Controller, Get, Query } from '@nestjs/common';
import { MarketDataService } from './market-data.service';

@Controller()
export class MarketDataController {
  constructor(private readonly marketDataService: MarketDataService) {}

  @Get('api/market-data/candles')
  getCandles(
    @Query('symbol') symbol: string,
    @Query('timeframe') timeframe: '1m' | '5m',
    @Query('from') from: string,
    @Query('to') to: string,
  ) {
    return this.marketDataService.getCandles(symbol, timeframe, from, to);
  }
}
