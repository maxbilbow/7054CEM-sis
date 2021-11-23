import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {InsuranceQuoteComponent} from "./insurance-quote.component";
import {FormSectionsModule} from "../../form-sections/form-sections.module";


@NgModule({
  declarations: [
    InsuranceQuoteComponent
  ],
  exports: [
    InsuranceQuoteComponent
  ],
  imports: [
    CommonModule,
    FormSectionsModule
  ]
})
export class InsuranceQuoteModule {
}
