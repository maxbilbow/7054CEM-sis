import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InsuranceQuoteComponent } from './insurance-quote.component';

describe('InsuranceQuoteComponent', () => {
  let component: InsuranceQuoteComponent;
  let fixture: ComponentFixture<InsuranceQuoteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InsuranceQuoteComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(InsuranceQuoteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
