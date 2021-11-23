import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DriverHistoryComponent } from './driver-history.component';

describe('DriverHistoryComponent', () => {
  let component: DriverHistoryComponent;
  let fixture: ComponentFixture<DriverHistoryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DriverHistoryComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DriverHistoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
