/**
 * Smart Insurance System
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
import { Address } from './address';

export interface VehicleUsage { 
    quoteId?: number;
    usageType?: VehicleUsage.UsageTypeEnum;
    annualMilage?: number;
    dayStorage?: VehicleUsage.DayStorageEnum;
    nightStorage?: VehicleUsage.NightStorageEnum;
    nightStorageAtHome?: boolean;
    nightStorageAddress?: Address;
}
export namespace VehicleUsage {
    export type UsageTypeEnum = 'SDP' | 'SDPC' | 'SDPCB';
    export const UsageTypeEnum = {
        SDP: 'SDP' as UsageTypeEnum,
        SDPC: 'SDPC' as UsageTypeEnum,
        SDPCB: 'SDPCB' as UsageTypeEnum
    };
    export type DayStorageEnum = 'Home' | 'CarParkOffice' | 'CarParkPublic' | 'StreetAwayFromHome';
    export const DayStorageEnum = {
        Home: 'Home' as DayStorageEnum,
        CarParkOffice: 'CarParkOffice' as DayStorageEnum,
        CarParkPublic: 'CarParkPublic' as DayStorageEnum,
        StreetAwayFromHome: 'StreetAwayFromHome' as DayStorageEnum
    };
    export type NightStorageEnum = 'Drive' | 'StreetOutsideHome' | 'StreetAwayFromHome' | 'Garage';
    export const NightStorageEnum = {
        Drive: 'Drive' as NightStorageEnum,
        StreetOutsideHome: 'StreetOutsideHome' as NightStorageEnum,
        StreetAwayFromHome: 'StreetAwayFromHome' as NightStorageEnum,
        Garage: 'Garage' as NightStorageEnum
    };
}