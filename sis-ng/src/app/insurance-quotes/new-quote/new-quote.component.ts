import {Component, OnInit} from '@angular/core';
import {InsurancePackageType} from "../insurance-quote";
import {QuoteService} from "../quote.service";


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
    this.quoteService.newQuote(InsurancePackageType.Home);
  }

  startMotor() {
    this.quoteService.newQuote(InsurancePackageType.Motor);
  }
}
