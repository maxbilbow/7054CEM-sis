import {Injectable} from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor, HttpResponse
} from '@angular/common/http';
import {Observable, tap} from 'rxjs';
import {keysToCamel, keysToSnake} from "./toCamel";

@Injectable()
export class JsonApiInterceptor implements HttpInterceptor {

  constructor() {
  }

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    if (request.url.includes("api")) {
      (request as any).body = keysToSnake(request.body as Record<string, unknown>)
    }
    return next.handle(request).pipe(
      tap(value => {
          if (request.url.includes("api") && value instanceof HttpResponse) {
            (value as any).body = keysToCamel(value.body as Record<string, unknown>)
          }
          return request
        }
      )
    )
  }
}
