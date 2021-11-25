import {Component, EventEmitter, Input, OnDestroy, OnInit, Output} from '@angular/core';
import {Quote} from "../../model/quote";

@Component({
  selector: 'app-quote-offers',
  templateUrl: './quote-offers.component.html',
  styleUrls: ['./quote-offers.component.less']
})
export class QuoteOffersComponent implements OnInit, OnDestroy {

  @Input() quote!: Quote

  @Output() onPrice = new EventEmitter<void>()

  constructor() {
  }

  isLoading() {
    return !this.quote.price
  }

  ngOnInit(): void {
    this.getQuotes()
  }

  getQuotes() {
    this.quote.price = undefined
    setTimeout(() => {
      this.quote.price = Math.ceil(Math.random() * 1000) + 0.99
      this.quote.isComplete = true
      this.onPrice.emit()
    }, 5000)
  }

  ngOnDestroy(): void {
    this.quote.price = undefined
  }
}
