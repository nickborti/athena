import { Controller, Get, Query } from '@nestjs/common';
import { MarketDataService } from './market-data.service';
import { GetCandlesDto } from './dto/get-candles.dto';

@Controller()
export class MarketDataController {
  constructor(private readonly marketDataService: MarketDataService) {}

  @Get('api/market-data/candles')
  getCandles(@Query() query: GetCandlesDto) {
    const { symbol, timeframe, from, to } = query;
    return this.marketDataService.getCandles(symbol, timeframe, from, to);
  }
}
