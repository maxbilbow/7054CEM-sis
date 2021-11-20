import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {PageHeaderComponent} from './page-header.component';
import {AppRoutingModule} from "../app-routing.module";
import {MatToolbarModule} from "@angular/material/toolbar";
import {MatIconModule} from "@angular/material/icon";
import {MatMenuModule} from "@angular/material/menu";
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import {MatButtonModule} from "@angular/material/button";


@NgModule({
  declarations: [
    PageHeaderComponent
  ],
  exports:[
    PageHeaderComponent
  ],
  imports: [
    CommonModule,
    MatToolbarModule,
    MatToolbarModule,
    MatToolbarModule,
    MatMenuModule,
    MatIconModule,
    BrowserAnimationsModule,
    MatButtonModule
  ]
})
export class PageHeaderModule { }
