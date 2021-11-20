import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {MyPoliciesComponent} from "./my-policies.component";
import {HttpClientModule} from "@angular/common/http";
import {MatNativeDateModule} from "@angular/material/core";
import {MatTableModule} from "@angular/material/table";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";



@NgModule({
  declarations: [MyPoliciesComponent],
  exports: [MyPoliciesComponent],
  imports: [
    CommonModule,
    HttpClientModule,
    MatNativeDateModule,
    MatTableModule,
    ReactiveFormsModule,
    FormsModule,
  ]
})
export class MyPoliciesModule { }
