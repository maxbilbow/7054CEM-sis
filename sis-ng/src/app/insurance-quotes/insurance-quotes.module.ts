import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {SavedQuotesComponent} from './saved-quotes/saved-quotes.component';
import {NewQuoteComponent} from './new-quote/new-quote.component';
import {InsuranceQuoteModule} from "./insurance-quote/insurance-quote.module";
import {RouterModule} from "@angular/router";
import {MatProgressBarModule} from "@angular/material/progress-bar";


@NgModule({
  declarations: [
    SavedQuotesComponent,
    NewQuoteComponent,
  ],
  exports: [
    SavedQuotesComponent,
    NewQuoteComponent,
  ],
  imports: [
    CommonModule,
    InsuranceQuoteModule,
    RouterModule
  ]
})
export class InsuranceQuotesModule {
}
