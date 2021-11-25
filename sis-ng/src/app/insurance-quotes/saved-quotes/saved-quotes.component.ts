import {Component, OnInit} from '@angular/core';
import {QuoteService} from "../quote.service";
import {Quotes} from "../../model/quotes";
import {Quote} from "../../model/quote";

@Component({
  selector: 'app-saved-quotes',
  templateUrl: './saved-quotes.component.html',
  styleUrls: ['./saved-quotes.component.less']
})
export class SavedQuotesComponent implements OnInit {
  readonly displayedColumns = ['type', 'created', 'updated', 'price', 'actions'];
  quotes: Quotes = []

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

  open({id}: Quote) {
    this.quoteService.open(id!).catch(console.error)
  }

  delete({id}: Quote) {
    this.quoteService.delete(id!).catch(console.error)
      .then(() => this.loadQuotes())
  }
}
