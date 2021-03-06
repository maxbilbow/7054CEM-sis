import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {UserProfile} from "../model/userProfile";

@Injectable({
  providedIn: 'root'
})
export class UserProfileService {

  constructor(private httpClient: HttpClient) {
  }

  fetchProfile(): Promise<UserProfile> {
    return new Promise<UserProfile>((resolve, reject) =>
      this.httpClient.get<UserProfile>("api/profile", {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .subscribe({next: resolve, error: reject})
    );
  }

  updateProfile(profile: UserProfile) {
    return new Promise<UserProfile>((resolve, reject) =>
      this.httpClient.post<UserProfile>("api/profile", profile)
        .subscribe({next: resolve, error: reject})
    );
  }
}
