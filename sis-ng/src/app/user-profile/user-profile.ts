import {DriverHistory} from "../form-sections/driver-history/driver-history";
import {PersonalDetails} from "../form-sections/personal-details/personal-details";

export interface UserProfile {
  personal_details: PersonalDetails;
  driver_history: DriverHistory;
}
