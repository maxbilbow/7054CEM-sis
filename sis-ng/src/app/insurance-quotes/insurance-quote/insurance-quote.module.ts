import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {InsuranceQuoteComponent} from "./insurance-quote.component";
import {FormSectionsModule} from "../../form-sections/form-sections.module";
import {QuoteOffersComponent} from "../quote-offers/quote-offers.component";
import {MatProgressBarModule} from "@angular/material/progress-bar";
import {MatProgressSpinnerModule} from "@angular/material/progress-spinner";


@NgModule({
  declarations: [
    InsuranceQuoteComponent,
    QuoteOffersComponent
  ],
  exports: [
    InsuranceQuoteComponent,
    FormSectionsModule
  ],
  imports: [
    CommonModule,
    FormSectionsModule,
    MatProgressBarModule,
    MatProgressSpinnerModule
  ]
})
export class InsuranceQuoteModule {
}
