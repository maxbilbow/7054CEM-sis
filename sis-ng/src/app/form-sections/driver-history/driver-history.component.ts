import {Component, Input, OnInit} from '@angular/core';
import {DriverHistory} from "./driver-history";

@Component({
  selector: 'app-driver-history',
  templateUrl: './driver-history.component.html',
  styleUrls: ['./driver-history.component.less']
})
export class DriverHistoryComponent implements OnInit {

  @Input() driverHistory!: DriverHistory

  constructor() { }

  ngOnInit(): void {
  }

}
