import {Component, DoCheck, EventEmitter, Input, KeyValueDiffer, KeyValueDiffers, OnInit, Output} from '@angular/core';
import {PersonalDetails} from "../../model/personalDetails";
import {FormBuilder, Validators} from "@angular/forms";
import {add} from "lodash";
import {MatDatepickerInputEvent} from "@angular/material/datepicker";
import {$e} from "@angular/compiler/src/chars";

@Component({
  selector: 'app-personal-details',
  templateUrl: './personal-details.component.html',
  styleUrls: ['./personal-details.component.less']
})
export class PersonalDetailsComponent implements DoCheck {
  private personalDetailsCopy!: PersonalDetails;
  @Input() personalDetails!: PersonalDetails
  @Output() private readonly onSave = new EventEmitter<void>()

  personalDetailsForm = this.fb.group({
    fullName: ['', Validators.required],
    address: this.fb.group({
      numberOrName: [''],
      street: [''],
      town: [''],
      county: [''],
      postcode: ['']
    }),
    dependents: [0],
    dob: [''],
    employmentStatus: [''],
    homeOwner: [false]
    // aliases: this.fb.array([
    //   this.fb.control('')
    // ])
  });

  constructor(private readonly fb: FormBuilder) {
  }

  ngDoCheck(): void {
    if (this.personalDetailsCopy !== this.personalDetails) {
      this.personalDetailsCopy = this.personalDetails
      this.updateForm()
    }
  }

  save(): void {
    // this.personalDetailsForm.disable()
    console.log(this.personalDetailsForm)
    const personalDetails = {...this.personalDetailsForm.value}
    personalDetails.dob = (personalDetails.dob as Date).toISOString().split("T")[0] // FIXME Why is date one day out?
    const address = personalDetails.address
    delete personalDetails.address
    Object.assign(this.personalDetails.address, address)
    Object.assign(this.personalDetails, personalDetails)
    this.onSave.emit()
  }

  updateForm() {
    const pd = {...this.personalDetails};
    pd.dob = new Date(pd.dob!)
    this.personalDetailsForm.patchValue(pd)
  }

  setDob($event: MatDatepickerInputEvent<unknown, unknown | null>) {
    console.log($event)
    console.log(this.personalDetailsForm.value.dob)
    // this.personalDetails.dob = $event.value
  }
}
