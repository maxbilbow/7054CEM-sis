import {InsurancePackageType, InsuranceQuote} from './insurance-quote';

describe('InsuranceQuote', () => {
  it('should create an instance', () => {
    expect(new InsuranceQuote(InsurancePackageType.Motor)).toBeTruthy();
  });
});
