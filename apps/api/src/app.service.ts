import { Injectable } from '@nestjs/common';

export type MarketData = {
  symbol: string;
  price: number;
  change: number;
  status: string;
};

@Injectable()
export class AppService {
  getMarket(): MarketData {
    return {
      symbol: 'EUR/USD',
      price: 1.1234,
      change: 0.25,
      status: 'OPEN',
    };
  }
}
