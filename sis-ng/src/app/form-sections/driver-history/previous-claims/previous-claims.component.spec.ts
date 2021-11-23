import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PreviousClaimsComponent } from './previous-claims.component';

describe('PreviousClaimsComponent', () => {
  let component: PreviousClaimsComponent;
  let fixture: ComponentFixture<PreviousClaimsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PreviousClaimsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PreviousClaimsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
