import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {InsurancePackageType, InsuranceQuote} from "./insurance-quote";
import {Router} from "@angular/router";

@Injectable({
  providedIn: 'root'
})
export class QuoteService {

  constructor(private readonly http: HttpClient,
              private readonly router: Router) {
  }

  newQuote(type: InsurancePackageType): Promise<boolean> {
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

  get(): Promise<InsuranceQuote[]>
  get(id: number): Promise<InsuranceQuote>
  get(id?: number): Promise<InsuranceQuote> | Promise<InsuranceQuote[]> {
    const f = <T>(path: string): Promise<T> => new Promise((resolve, reject) => this.http.get<T>(path)
      .subscribe({
        next: resolve,
        error: reject
      })
    );
    if (id === undefined) {
      return f<InsuranceQuote[]>("/api/quote");
    } else {
      return f<InsuranceQuote>(`/api/quote/${id}`);
    }
  }

  save(quote: InsuranceQuote): Promise<InsuranceQuote> {
    return new Promise((resolve, reject) => this.http.put<InsuranceQuote>(`/api/quote`, quote)
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
