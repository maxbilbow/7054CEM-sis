import {Component, OnInit} from '@angular/core';
import {UserProfileService} from "./user-profile.service";
import {UserProfile} from "../model/userProfile";

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.less'],
})
export class UserProfileComponent implements OnInit {
  profile!: UserProfile
  step = -1;

  constructor(private readonly userProfileService: UserProfileService) {
  }

  ngOnInit(): void {
    this.userProfileService.fetchProfile()
      .then(profile => {
        this.profile = profile
        this.setStep(0)
      })
  }

  save(): void {
    this.userProfileService.updateProfile(this.profile!)
      .then(profile => {
        this.profile = profile
        this.step++
      })
  }

  setStep(number: number) {
    this.step = number
  }
}
