import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {PersonalDetailsComponent} from './personal-details/personal-details.component';
import {AddressComponent} from './address/address.component';
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatButtonModule} from "@angular/material/button";
import {FormsModule} from "@angular/forms";
import {MatInputModule} from "@angular/material/input";
import {DriverHistoryComponent} from './driver-history/driver-history.component';
import {PreviousClaimsComponent} from './driver-history/previous-claims/previous-claims.component';
import {MatCardModule} from "@angular/material/card";


@NgModule({
  declarations: [
    PersonalDetailsComponent,
    AddressComponent,
    DriverHistoryComponent,
    PreviousClaimsComponent
  ],
  imports: [
    CommonModule,
    MatFormFieldModule,
    MatButtonModule,
    FormsModule,
    MatInputModule,
    MatCardModule
  ],
  exports: [
    MatFormFieldModule,
    MatButtonModule,
    FormsModule,
    MatInputModule,
    PersonalDetailsComponent,
    AddressComponent,
    DriverHistoryComponent,
    MatCardModule
  ]
})
export class FormSectionsModule { }
