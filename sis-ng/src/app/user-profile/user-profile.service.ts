import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {UserProfile} from "./user-profile";

@Injectable({
  providedIn: 'root'
})
export class UserProfileService {

  constructor(private httpClient: HttpClient) { }

  fetchProfile(): Promise<UserProfile> {
    return new Promise<UserProfile>((resolve, reject) =>
      this.httpClient.get<UserProfile>("api/profile")
        .subscribe(next => resolve(next))
    );
  }
}
