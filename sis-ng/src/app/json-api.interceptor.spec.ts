import { TestBed } from '@angular/core/testing';

import { JsonApiInterceptor } from './json-api.interceptor';

describe('JsonApiInterceptor', () => {
  beforeEach(() => TestBed.configureTestingModule({
    providers: [
      JsonApiInterceptor
      ]
  }));

  it('should be created', () => {
    const interceptor: JsonApiInterceptor = TestBed.inject(JsonApiInterceptor);
    expect(interceptor).toBeTruthy();
  });
});
