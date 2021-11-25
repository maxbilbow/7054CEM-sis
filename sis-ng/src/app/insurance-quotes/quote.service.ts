import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Router} from "@angular/router";
import {InsuranceType} from "../model/insuranceType";
import {Quote} from "../model/quote";

@Injectable({
  providedIn: 'root'
})
export class QuoteService {

  constructor(private readonly http: HttpClient,
              private readonly router: Router) {
  }

  newQuote(type: InsuranceType): Promise<boolean> {
    return new Promise((resolve, reject) => this.http.post<{ quote_id: number }>(`/api/quote`, {type})
      .subscribe({
        next: ({quote_id}) => resolve(this.open(quote_id)),
        error: reject
      })
    );
  }

  open(id: number): Promise<boolean> {
    return this.router.navigate(["saved-quote", id]);
  }

  get(): Promise<Quote[]>
  get(id: number): Promise<Quote>
  get(id?: number): Promise<Quote> | Promise<Quote[]> {
    const f = <T>(path: string): Promise<T> => new Promise((resolve, reject) => this.http.get<T>(path)
      .subscribe({
        next: resolve,
        error: reject
      })
    );
    if (id === undefined) {
      return f<Quote[]>("/api/quote");
    } else {
      return f<Quote>(`/api/quote/${id}`);
    }
  }

  save(quote: Quote): Promise<Quote> {
    return new Promise((resolve, reject) => this.http.put<Quote>(`/api/quote`, quote)
      .subscribe({
        next: resolve,
        error: reject
      })
    );
  }

  delete(id: number): Promise<boolean> {
    return new Promise((resolve, reject) => this.http.delete<boolean>(`/api/quote/${id}`)
      .subscribe({
        next: resolve,
        error: reject
      })
    );
  }
}
