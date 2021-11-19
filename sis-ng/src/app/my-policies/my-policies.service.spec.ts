import { TestBed } from '@angular/core/testing';

import { MyPoliciesService } from './my-policies.service';

describe('MyPoliciesService', () => {
  let service: MyPoliciesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MyPoliciesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
