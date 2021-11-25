import {Component, OnInit} from '@angular/core';
import {QuoteService} from "../quote.service";
import {InsuranceType} from "../../model/insuranceType";


@Component({
  selector: 'app-new-quote',
  templateUrl: './new-quote.component.html',
  styleUrls: ['./new-quote.component.less']
})
export class NewQuoteComponent implements OnInit {

  constructor(private readonly quoteService: QuoteService) {
  }

  ngOnInit(): void {
  }

  startHome() {
    this.quoteService.newQuote(InsuranceType.Home);
  }

  startMotor() {
    this.quoteService.newQuote(InsuranceType.Motor);
  }
}
