import {Component, Input, OnInit} from '@angular/core';
import {PersonalDetails} from "../../model/personalDetails";

@Component({
  selector: 'app-personal-details',
  templateUrl: './personal-details.component.html',
  styleUrls: ['./personal-details.component.less']
})
export class PersonalDetailsComponent implements OnInit {

  @Input() personalDetails!: PersonalDetails

  constructor() {
  }

  ngOnInit(): void {
    if (this.personalDetails.fullName === undefined) {
      this.personalDetails.fullName = ""
    }
  }

  save(): void {

  }

}
