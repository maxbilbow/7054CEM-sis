import {Component, OnInit} from '@angular/core';
import {Membership} from "../model/membership";
import {MembershipService} from "./membership.service";

@Component({
  selector: 'app-my-membership',
  templateUrl: './my-membership.component.html',
  styleUrls: ['./my-membership.component.less']
})
export class MyMembershipComponent implements OnInit {

  membership?: Membership
  endDate = new Date().toISOString().split('T')[0];
  eligibleType = ""

  constructor(private readonly membershipService: MembershipService) {
  }

  ngOnInit(): void {
    this.membershipService.getEligibleType()
      .then((eligibleType) => {
        this.eligibleType = eligibleType;
      })
    this.membershipService.fetch()
      .then(membership => {
        this.membership = membership
      })
  }

  create() {
    this.membershipService.create({end_date: this.endDate})
      .then(membership => {
        this.membership = membership
      })
  }

  save() {
    this.membershipService.update(this.membership!)
      .then(membership => {
        this.membership = membership
      })
  }

  cancel() {
    this.membershipService.cancel()
      .then(membership => {
        this.membership = membership;
      })
  }
}
