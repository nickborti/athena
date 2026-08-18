import { Module } from '@nestjs/common';
// import { AppController } from './app.controller';
// import { AppService } from './app.service';
import { ConfigModule } from '@nestjs/config';
import { TiingoMarketDataProvider } from './market-data/tiingo.market-data.provider';
import { MARKET_DATA_PROVIDER } from './market-data/market-data.tokens';
import { MarketDataController } from './market-data/market-data.controller';
import { MarketDataService } from './market-data/market-data.service';

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
    }),
  ],
  controllers: [MarketDataController],
  providers: [
    MarketDataService,
    TiingoMarketDataProvider,
    {
      provide: MARKET_DATA_PROVIDER,
      useExisting: TiingoMarketDataProvider,
    },
  ],
})
export class AppModule {}
