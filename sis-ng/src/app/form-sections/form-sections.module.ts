import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {PersonalDetailsComponent} from './personal-details/personal-details.component';
import {AddressComponent} from './address/address.component';
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatButtonModule} from "@angular/material/button";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {MatInputModule} from "@angular/material/input";
import {DriverHistoryComponent} from './driver-history/driver-history.component';
import {PreviousClaimsComponent} from './driver-history/previous-claims/previous-claims.component';
import {MatCardModule} from "@angular/material/card";
import {MAT_DATE_LOCALE, MatCommonModule, MatNativeDateModule} from "@angular/material/core";
import {MatTableModule} from "@angular/material/table";
import {MatDatepickerModule} from "@angular/material/datepicker";
import {MatGridListModule} from "@angular/material/grid-list";
import {MatIconModule} from "@angular/material/icon";
import {MatExpansionModule} from "@angular/material/expansion";
import {MatSlideToggleModule} from "@angular/material/slide-toggle";
import {MatButtonToggleModule} from "@angular/material/button-toggle";


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
    MatCardModule,
    MatNativeDateModule,
    MatTableModule,
    ReactiveFormsModule,
    MatDatepickerModule,
    MatCommonModule,
    MatGridListModule,
    MatIconModule,
    MatExpansionModule,
    MatSlideToggleModule,
    MatButtonToggleModule
  ],
  exports: [
    PersonalDetailsComponent,
    AddressComponent,
    DriverHistoryComponent,

    MatFormFieldModule,
    MatButtonModule,
    FormsModule,
    MatInputModule,
    MatCardModule,
    MatNativeDateModule,
    MatTableModule,
    ReactiveFormsModule,
    MatDatepickerModule,
    MatCommonModule,
    MatGridListModule,
    MatIconModule,
    MatExpansionModule,

    MatSlideToggleModule,
    MatButtonToggleModule,
  ],
  providers: [
    {provide: MAT_DATE_LOCALE, useValue: 'en-GB'}
  ]
})
export class FormSectionsModule {
}
