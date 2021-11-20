export enum InsurancePackageType {
  Motor = "Motor",
  Home = "Home"
}
export interface InsuranceQuote {
  id: number;
  user_id: number;
  type: InsurancePackageType;
  created: number;
  updated: number;
  is_complete: boolean;
  price?: number;
}
