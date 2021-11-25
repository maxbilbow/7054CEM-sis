import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {QuoteService} from "../quote.service";
import {Quote} from "../../model/quote";
import {HomeQuoteSections} from "../../model/homeQuoteSections";

@Component({
  selector: 'app-insurance-quote',
  templateUrl: './insurance-quote.component.html',
  styleUrls: ['./insurance-quote.component.less']
})
export class InsuranceQuoteComponent implements OnInit {

  quote!: Quote;

  constructor(private readonly route: ActivatedRoute, private readonly quoteService: QuoteService) {

  }

  ngOnInit(): void {
    this.route.params.subscribe({
      next: async (params) => {
        const id = Number(params["quote_id"]);
        this.quote = await this.quoteService.get(id)
      }
    })

  }

  show() {
    if (!this.quote) {
      return "Nothing to show yet";
    }
    return JSON.stringify(this.quote);
  }

  hasPersonalDetails() {
    return (this.quote.sections as HomeQuoteSections)?.personalDetails
  }
}
