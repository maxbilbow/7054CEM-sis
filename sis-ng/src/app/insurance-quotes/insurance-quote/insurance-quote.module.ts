import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {InsuranceQuoteComponent} from "./insurance-quote.component";


@NgModule({
  declarations: [
    InsuranceQuoteComponent
  ],
  exports:[
    InsuranceQuoteComponent
  ],
  imports: [
    CommonModule
  ]
})
export class InsuranceQuoteModule { }
