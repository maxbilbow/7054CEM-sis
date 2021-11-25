import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {QuoteService} from "../quote.service";
import {Quote} from "../../model/quote";
import {HomeQuoteSections} from "../../model/homeQuoteSections";
import {VehicleQuoteSections} from "../../model/vehicleQuoteSections";
import {InsuranceType} from "../../model/insuranceType";

@Component({
  selector: 'app-insurance-quote',
  templateUrl: './insurance-quote.component.html',
  styleUrls: ['./insurance-quote.component.less']
})
export class InsuranceQuoteComponent implements OnInit {

  quote!: Quote;

  get sections() {
    return this.quote.sections as VehicleQuoteSections & HomeQuoteSections
  }

  constructor(private readonly route: ActivatedRoute, private readonly quoteService: QuoteService) {

  }

  ngOnInit(): void {
    this.route.params.subscribe({
      next: async (params) => {
        const id = Number(params["quoteId"]);
        this.quote = await this.quoteService.get(id)
      }
    })

  }

  show() {
    if (!this.quote) {
      return "Nothing to show yet";
    }
    return JSON.stringify(this.quote, null, 2);
  }

  isMotor() {
    return this.quote.type === InsuranceType.Motor
  }

  isHome() {
    return this.quote.type === InsuranceType.Home
  }

  save() {
    this.quoteService.save(this.quote)
      .then((q) => {
        this.quote = q;
      })
      .catch(console.error)
  }
}
