import {Component, OnInit} from '@angular/core';
import {InsuranceQuote} from "../insurance-quote";
import {QuoteService} from "../quote.service";

@Component({
  selector: 'app-saved-quotes',
  templateUrl: './saved-quotes.component.html',
  styleUrls: ['./saved-quotes.component.less']
})
export class SavedQuotesComponent implements OnInit {
  readonly displayedColumns = ['type', 'updated', 'price', 'actions'];
  quotes: InsuranceQuote[] = []

  constructor(private readonly quoteService: QuoteService) {
  }

  ngOnInit(): void {
    this.loadQuotes();
  }

  loadQuotes() {
    this.quoteService.get()
      .then(quotes => {
        this.quotes = quotes;
      })
      .catch(console.error)
  }

  open({id}: InsuranceQuote) {
    this.quoteService.open(id).catch(console.error)
  }

  delete({id}: InsuranceQuote) {
    this.quoteService.delete(id).catch(console.error)
      .then(() => this.loadQuotes())
  }
}
