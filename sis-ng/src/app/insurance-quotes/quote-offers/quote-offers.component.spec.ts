import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QuoteOffersComponent } from './quote-offers.component';

describe('QuoteOffersComponent', () => {
  let component: QuoteOffersComponent;
  let fixture: ComponentFixture<QuoteOffersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ QuoteOffersComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(QuoteOffersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
