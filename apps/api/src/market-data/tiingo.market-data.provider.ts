import type { Candle } from 'src/types/candle';
import { MarketDataProvider } from './market-data.provider';
import { ConfigService } from '@nestjs/config';
import { Injectable } from '@nestjs/common';
import { TiingoCandleResponse } from './types/tiingo-candle-response';

@Injectable()
export class TiingoMarketDataProvider implements MarketDataProvider {
  constructor(private readonly configService: ConfigService) {}
  async getCandles(
    symbol: string,
    timeframe: '1m' | '5m',
    from: string,
    to: string,
  ): Promise<Candle[]> {
    const apiKey = this.configService.getOrThrow<string>('TIINGO_API_KEY');

    const url = new URL(`https://api.tiingo.com/tiingo/fx/${symbol}/prices`);

    url.searchParams.set('startDate', from);
    url.searchParams.set('endDate', to);
    url.searchParams.set('resampleFreq', timeframe === '1m' ? '1min' : '5min');

    console.log('Tiingo URL:', url.toString());

    const response = await fetch(url, {
      headers: {
        Authorization: `Token ${apiKey}`,
      },
    });

    if (!response.ok) {
      throw new Error(`Tiingo request failed: ${response.status}`);
    }

    const data = await response.json();

    return data.map(
      (item: {
        date: string;
        ticker: string;
        open: number;
        high: number;
        low: number;
        close: number;
      }) => this.mapCandle(item, timeframe),
    );
  }

  private mapCandle(
    data: TiingoCandleResponse,
    timeframe: '1m' | '5m',
  ): Candle {
    return {
      symbol: data.ticker.toUpperCase(),
      timestamp: data.date,
      timeframe,
      open: data.open,
      high: data.high,
      low: data.low,
      close: data.close,
      volume: null,
    };
  }
}
