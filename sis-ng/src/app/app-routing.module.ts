import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {UserProfileComponent} from "./user-profile/user-profile.component";
import {MyPoliciesComponent} from "./my-policies/my-policies.component";
import {MyClaimsComponent} from "./my-claims/my-claims.component";
import {MyMembershipComponent} from "./my-membership/my-membership.component";

const routes: Routes = [
  {
    path: "profile", component: UserProfileComponent
  },
  {
    path: "my-policies", component: MyPoliciesComponent
  },
  {
    path: "my-claims", component: MyClaimsComponent
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
