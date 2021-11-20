import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {InsurancePackageType, InsuranceQuote} from "./insurance-quote";
import {ActivatedRoute, Router} from "@angular/router";

@Injectable({
  providedIn: 'root'
})
export class QuoteService {

  constructor(private readonly http: HttpClient,
              private readonly router: Router) {
  }

  newQuote(type: InsurancePackageType): Promise<boolean> {
    return new Promise((resolve, reject) => this.http.post(`/api/quote/${type}`, {})
      .subscribe({
        next: id => resolve(this.router.navigate(['saved-quote', id])),
        error: reject
      })
    );
  }

  open(id: number): Promise<boolean> {
    return this.router.navigate([`/saved-quote/${id}`])
  }

  get(id: number): Promise<InsuranceQuote> {
    return new Promise((resolve, reject) => this.http.get<InsuranceQuote>(`/api/quote/${id}`)
      .subscribe({
        next: resolve,
        error: reject
      })
    );
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
        next: () => resolve(this.router.navigate(['/saved-quotes'])),
        error: reject
      })
    );
  }
}
