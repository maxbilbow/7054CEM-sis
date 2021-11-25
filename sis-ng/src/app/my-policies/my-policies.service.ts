import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {InsurancePolicy} from "../model/insurancePolicy";

@Injectable({
  providedIn: 'root'
})
export class MyPoliciesService {

  constructor(private httpClient: HttpClient) {
  }

  fetchAll(): Promise<InsurancePolicy[]> {
    return new Promise<InsurancePolicy[]>((resolve, reject) => {
      this.httpClient.get<InsurancePolicy[]>("/api/my-policies")
        .subscribe({next: resolve, error: reject})
    })
      .catch(() => [{
        id: 1,
        start_date: "2020-11-01",
        end_date: "2021-11-01",
        type: "Motor"
      },
        {
          id: 1,
          start_date: "2021-12-01",
          end_date: "2022-12-01",
          type: "Motor"
        },
        {
          id: 1,
          start_date: "2022-12-01",
          end_date: "2023-12-01",
          type: "Motor"
        }])
  }
}
