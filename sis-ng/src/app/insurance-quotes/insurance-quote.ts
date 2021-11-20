export enum InsurancePackageType {
  Motor = "Motor",
  Home = "Home"
}
export class InsuranceQuote {
  constructor(readonly type: InsurancePackageType) {
  }
}
