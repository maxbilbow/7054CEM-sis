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
        .subscribe(next => resolve(next))
    );
  }

  create({end_date}: Partial<Membership>) {
    return new Promise<Membership>((resolve, reject) =>
      this.httpClient.post<Membership>("api/membership", {end_date})
        .subscribe(next => resolve(next))
    );
  }

  update(membership: Membership) {
    return new Promise<Membership>((resolve, reject) =>
      this.httpClient.put<Membership>("api/membership", membership)
        .subscribe(next => resolve(next))
    );
  }

  cancel() {
    return new Promise<Membership>((resolve, reject) =>
      this.httpClient.delete<Membership>("api/membership")
        .subscribe(next => resolve(next))
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
