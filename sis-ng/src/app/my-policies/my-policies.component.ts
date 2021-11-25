import {Component, OnInit, ViewChild} from '@angular/core';
import {MyPoliciesService} from "./my-policies.service";
import {MatTableDataSource} from "@angular/material/table";
import {MatSort, Sort} from "@angular/material/sort";
import {LiveAnnouncer} from "@angular/cdk/a11y";
import {InsurancePolicy} from "../model/insurancePolicy";

@Component({
  selector: 'app-my-policies',
  templateUrl: './my-policies.component.html',
  styleUrls: ['./my-policies.component.less']
})
export class MyPoliciesComponent implements OnInit {
  readonly displayedColumns = ['type', 'id', 'start_date', 'end_date', 'is_active'];
  policyList = new MatTableDataSource<InsurancePolicy>();

  @ViewChild(MatSort) sort!: MatSort;

  constructor(private readonly myPolicyService: MyPoliciesService,
              private readonly liveAnnouncer: LiveAnnouncer) {
  }

  getStatus(policy: InsurancePolicy) {
    const end_date = Date.parse(policy.endDate!);
    const today = new Date().setHours(0, 0, 0, 0)
    return end_date > today ? "Active" : "Expired"
  }

  ngAfterViewInit() {
    this.policyList.sort = this.sort;
  }

  ngOnInit(): void {
    this.myPolicyService.fetchAll()
      .then(policyList => {
        this.policyList = new MatTableDataSource(policyList);
      })
  }

  /** Announce the change in sort state for assistive technology. */
  announceSortChange(sortState: Sort) {
    // This example uses English messages. If your application supports
    // multiple language, you would internationalize these strings.
    // Furthermore, you can customize the message to add additional
    // details about the values being sorted.
    if (sortState.direction) {
      this.liveAnnouncer.announce(`Sorted ${sortState.direction}ending`);
    } else {
      this.liveAnnouncer.announce('Sorting cleared');
    }
  }
}
