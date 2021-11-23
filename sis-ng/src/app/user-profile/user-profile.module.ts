import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {UserProfileComponent} from "./user-profile.component";
import {FormSectionsModule} from "../form-sections/form-sections.module";


@NgModule({
  declarations: [UserProfileComponent],
  exports: [UserProfileComponent],
  imports: [
    CommonModule,
    FormSectionsModule
  ]
})
export class UserProfileModule {
}
