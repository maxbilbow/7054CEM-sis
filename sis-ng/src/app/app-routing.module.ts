import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {UserProfileComponent} from "./user-profile/user-profile.component";
import {MyPoliciesComponent} from "./my-policies/my-policies.component";
import {MyMembershipComponent} from "./my-membership/my-membership.component";
import {NewQuoteComponent} from "./insurance-quotes/new-quote/new-quote.component";
import {SavedQuotesComponent} from "./insurance-quotes/saved-quotes/saved-quotes.component";
import {InsuranceQuoteComponent} from "./insurance-quotes/insurance-quote/insurance-quote.component";

const routes: Routes = [
  {
    path: '', redirectTo: 'new-quote', pathMatch: 'full'
  },
  {
    path: "new-quote", component: NewQuoteComponent
  },
  {
    path: "saved-quotes", component: SavedQuotesComponent
  },
  {
    path: "saved-quote/:quote_id", component: InsuranceQuoteComponent,
  },
  {
    path: "profile", component: UserProfileComponent
  },
  {
    path: "my-policies", component: MyPoliciesComponent
  },
  {
    path: "my-membership", component: MyMembershipComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
