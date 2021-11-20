import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {SavedQuotesComponent} from './saved-quotes/saved-quotes.component';
import {NewQuoteComponent} from './new-quote/new-quote.component';
import {MatGridListModule} from "@angular/material/grid-list";
import {MatIconModule} from "@angular/material/icon";
import {InsuranceQuoteModule} from "./insurance-quote/insurance-quote.module";
import {HttpClientModule} from "@angular/common/http";
import {RouterModule} from "@angular/router";


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
    MatGridListModule,
    MatIconModule,
    HttpClientModule,
    RouterModule,
  ]
})
export class InsuranceQuotesModule {
}
