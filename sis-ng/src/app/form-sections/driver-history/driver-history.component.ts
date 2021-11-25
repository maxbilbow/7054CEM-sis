import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {DriverHistory} from "../../model/driverHistory";
import {FormBuilder} from "@angular/forms";

@Component({
  selector: 'app-driver-history',
  templateUrl: './driver-history.component.html',
  styleUrls: ['./driver-history.component.less']
})
export class DriverHistoryComponent implements OnInit {


  @Input() driverHistory!: DriverHistory
  @Output() private readonly onSave = new EventEmitter<void>()
  @Output() private readonly onEdit = new EventEmitter<string>()

  form = this.fb.group({
    // aliases: this.fb.array([
    //   this.fb.control('')
    // ])
  });

  constructor(private readonly fb: FormBuilder) {
  }

  ngOnInit(): void {
    this.updateForm()
  }

  edit() {
    this.form.enable()
  }
  save(): void {
    const driverHistory = {...this.form.value}
    Object.assign(this.form, driverHistory)

    this.onSave.emit()
    this.form.disable()
  }

  @Input() onSubmit!: () => void

  updateForm() {
    this.form.patchValue(this.driverHistory)
  }
}
