import {Component, Input, OnInit} from '@angular/core';
import {PreviousClaim} from "../../../model/previousClaim";

@Component({
  selector: 'app-previous-claims',
  templateUrl: './previous-claims.component.html',
  styleUrls: ['./previous-claims.component.less']
})
export class PreviousClaimsComponent implements OnInit {

  @Input() previousClaims: PreviousClaim[] = []

  constructor() { }

  ngOnInit(): void {
  }

}
