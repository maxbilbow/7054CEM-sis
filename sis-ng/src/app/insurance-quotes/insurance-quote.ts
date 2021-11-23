import {PersonalDetails} from "../form-sections/personal-details/personal-details";

export enum InsurancePackageType {
  Motor = "Motor",
  Home = "Home"
}

export interface InsuranceQuote {
  id: number;
  user_id: number;
  type: InsurancePackageType;
  created: number;
  updated: number;
  is_complete: boolean;
  price?: number;

  // TODO
  start_date: string;

  personal_details: PersonalDetails
  details: MotorDetails | HomeDetails
}

export interface MotorQuote extends InsuranceQuote {
  type: InsurancePackageType.Motor
  summary: MotorQuoteSummary
}

export interface HomeQuote extends InsuranceQuote {
  type: InsurancePackageType.Home
  summary: HomeQuoteSummary
}

interface MotorQuoteSummary {
  main_driver: string
  additional_drivers: string[]
}

interface HomeQuoteSummary {

}

interface MotorDetails {
  vehicle_details: {
    alarm_fitter: boolean
    immobilizer_fitted: boolean
    tracking_device_fitted: boolean
    is_import: boolean
    off_side_drive: boolean
    number_of_seats: number
    current_value: number
    is_modified: boolean
  }
  vehicle_usage: {}
}

interface HomeDetails {

}
