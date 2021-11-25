import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {UserProfileModule} from "./user-profile/user-profile.module";
import {PageHeaderModule} from "./page-header/page-header.module";
import {MyMembershipModule} from "./my-membership/my-membership.module";
import {MyPoliciesModule} from "./my-policies/my-policies.module";
import {InsuranceQuotesModule} from "./insurance-quotes/insurance-quotes.module";
import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import {AuthenticationInterceptor} from "./authentication.interceptor";

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    PageHeaderModule,
    UserProfileModule,
    MyMembershipModule,
    MyPoliciesModule,
    InsuranceQuotesModule,
    HttpClientModule
  ],
  providers: [AuthenticationInterceptor,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthenticationInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {

}
