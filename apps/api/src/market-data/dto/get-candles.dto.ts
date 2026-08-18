import { IsDateString, IsIn, IsNotEmpty, IsString } from 'class-validator';

export class GetCandlesDto {
  @IsString()
  @IsNotEmpty()
  symbol!: string;

  @IsIn(['1m', '5m'])
  timeframe!: '1m' | '5m';

  @IsDateString()
  from!: string;

  @IsDateString()
  to!: string;
}
