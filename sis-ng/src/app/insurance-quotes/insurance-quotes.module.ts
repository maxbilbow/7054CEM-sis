import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {SavedQuotesComponent} from './saved-quotes/saved-quotes.component';
import {NewQuoteComponent} from './new-quote/new-quote.component';
import {MatGridListModule} from "@angular/material/grid-list";
import {MatIconModule} from "@angular/material/icon";
import {InsuranceQuoteModule} from "./insurance-quote/insurance-quote.module";
import {RouterModule} from "@angular/router";
import {MatNativeDateModule} from "@angular/material/core";
import {MatTableModule} from "@angular/material/table";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";


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
