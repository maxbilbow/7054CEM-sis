import {Component, Input, OnInit} from '@angular/core';
import {PersonalDetails} from "./personal-details";

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
  }

  save(): void {

  }

}
