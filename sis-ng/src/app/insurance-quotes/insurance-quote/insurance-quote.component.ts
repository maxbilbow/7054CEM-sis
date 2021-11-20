import {Component, Input, OnInit} from '@angular/core';
import {InsuranceQuote} from "../insurance-quote";
import {ActivatedRoute} from "@angular/router";
import {QuoteService} from "../quote.service";

@Component({
  selector: 'app-insurance-quote',
  templateUrl: './insurance-quote.component.html',
  styleUrls: ['./insurance-quote.component.less']
})
export class InsuranceQuoteComponent implements OnInit {

  quote!: InsuranceQuote;

  constructor(private readonly route: ActivatedRoute, private readonly quoteService: QuoteService) {

  }

  ngOnInit(): void {
    this.route.queryParams.subscribe({
      next: async (params) => {
        const id = params["quote_id"] as number;
        console.log(id)
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
}
