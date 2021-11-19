import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Membership} from "../model/membership";

@Injectable({
  providedIn: 'root'
})
export class MembershipService {

  constructor(private httpClient: HttpClient) {
  }

  fetch(): Promise<Membership> {
    return new Promise<Membership>((resolve, reject) =>
      this.httpClient.get<Membership>("api/membership")
        .subscribe({next: resolve, error: reject})
    );
  }

  create({end_date}: Partial<Membership>) {
    return new Promise<Membership>((resolve, reject) =>
      this.httpClient.post<Membership>("api/membership", {end_date})
        .subscribe({next: resolve, error: reject})
    );
  }

  update(membership: Membership) {
    return new Promise<Membership>((resolve, reject) =>
      this.httpClient.put<Membership>("api/membership", membership)
        .subscribe({next: resolve, error: reject})
    );
  }

  cancel() {
    return new Promise<Membership>((resolve, reject) =>
      this.httpClient.delete<Membership>("api/membership")
        .subscribe({next: resolve, error: reject})
    );
  }

  async getEligibleType() {
    const response = await fetch("/api/membership/get_eligible_type");
    if (response.ok) {
      return response.text()
    } else {
      return ""
    }
  }
}
