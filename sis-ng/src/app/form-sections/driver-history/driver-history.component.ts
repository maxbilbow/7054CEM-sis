import {Component, DoCheck, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {DriverHistory} from "../../model/driverHistory";
import {FormBuilder} from "@angular/forms";
import {MatDatepickerInputEvent} from "@angular/material/datepicker";

@Component({
  selector: 'app-driver-history',
  templateUrl: './driver-history.component.html',
  styleUrls: ['./driver-history.component.less']
})
export class DriverHistoryComponent implements DoCheck {
  private modelCopy!: DriverHistory;

  @Input() driverHistory!: DriverHistory
  @Output() private readonly onSave = new EventEmitter<void>()

  form = this.fb.group({
    licenceType: [''],
    licenceNo: [''],
    licenceSince: ['']
    // aliases: this.fb.array([
    //   this.fb.control('')
    // ])
  });

  constructor(private readonly fb: FormBuilder) {
  }

  ngDoCheck(): void {
    if (this.modelCopy !== this.driverHistory) {
      this.modelCopy = this.driverHistory
      this.updateForm()
    }
  }

  @Input() onSubmit!: () => void

  save(): void {
    console.log(this.form)
    const driverHistory = {...this.form.value}
    driverHistory.licenceSince = (driverHistory.licenceSince as Date).toISOString().split("T")[0] // FIXME Why is date one day out?
    const address = driverHistory.previousClaims
    delete driverHistory.previousClaims
    Object.assign(this.driverHistory.previousClaims, address)
    Object.assign(this.driverHistory, driverHistory)
    this.onSave.emit()
  }

  updateForm() {
    const pd = {...this.driverHistory};
    pd.licenseSince = new Date(pd.licenseSince!)
    this.form.patchValue(pd)
  }

  setDob($event: MatDatepickerInputEvent<unknown, unknown | null>) {
    console.log($event)
    console.log(this.form.value.dob)
    // this.personalDetails.dob = $event.value
  }
}
