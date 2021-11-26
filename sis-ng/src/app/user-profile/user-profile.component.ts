import {Component, OnInit, ViewChild} from '@angular/core';
import {UserProfileService} from "./user-profile.service";
import {UserProfile} from "../model/userProfile";
import {MatAccordion} from "@angular/material/expansion";

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.less'],
})
export class UserProfileComponent implements OnInit {
  profile!: UserProfile
  @ViewChild(MatAccordion) accordion!: MatAccordion;

  constructor(private readonly userProfileService: UserProfileService) {
  }

  ngOnInit(): void {
    this.userProfileService.fetchProfile()
      .then(profile => {
        this.profile = profile
      })
  }

  save(): void {
    this.userProfileService.updateProfile(this.profile!)
      .then(profile => {
        this.profile = profile
      })
  }
}
