export type Candle = {
  symbol: string;
  timestamp: string;
  timeframe: '1m' | '5m';
  open: number;
  high: number;
  low: number;
  close: number;
  volume: number | null;
};
