import {Component, EventEmitter, OnDestroy, OnInit, Output} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {QuoteService} from "../quote.service";
import {Quote} from "../../model/quote";
import {HomeQuoteSections} from "../../model/homeQuoteSections";
import {VehicleQuoteSections} from "../../model/vehicleQuoteSections";
import {InsuranceType} from "../../model/insuranceType";
import {Subscription} from "rxjs";
import {DriverDetails} from "../../model/driverDetails";

@Component({
  selector: 'app-insurance-quote',
  templateUrl: './insurance-quote.component.html',
  styleUrls: ['./insurance-quote.component.less']
})
export class InsuranceQuoteComponent implements OnInit, OnDestroy {

  activeSection = ""
  quote!: Quote;
  subscription?: Subscription;
  step = 0;

  get sections() {
    const sections = this.quote.sections as VehicleQuoteSections & HomeQuoteSections
    return {
      ...sections,
      ...sections.driverDetails ?? {}
    } as VehicleQuoteSections & HomeQuoteSections & DriverDetails
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

  ngOnDestroy() {
    this.subscription?.unsubscribe()
  }

  show() {
    if (!this.quote) {
      return "Nothing to show yet";
    }
    return JSON.stringify(this.quote, null, 2);
  }

  isMotor() {
    return this.quote?.type === InsuranceType.Motor
  }

  isHome() {
    return this.quote?.type === InsuranceType.Home
  }

  save() {
    this.quoteService.save(this.quote)
      .then((q) => {
        this.quote = q;
        this.step++
      })
      .catch(console.error)
  }

  setStep(number: number) {
    this.step = number
  }

  isComplete() {
    return this.step > 4
  }
}
