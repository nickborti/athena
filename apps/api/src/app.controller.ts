import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';
import type { MarketData } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get('api/market')
  getMarket(): MarketData {
    return this.appService.getMarket();
  }
}
