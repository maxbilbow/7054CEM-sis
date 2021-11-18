import { Component, OnInit } from '@angular/core';
import {UserProfileService} from "./user-profile.service";

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.less']
})
export class UserProfileComponent implements OnInit {

  constructor(private readonly userProfileService: UserProfileService) { }

  ngOnInit(): void {
    this.userProfileService.fetchProfile().then(console.log);
  }

}
