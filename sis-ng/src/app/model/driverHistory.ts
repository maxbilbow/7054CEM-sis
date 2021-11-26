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
import { PreviousClaim } from './previousClaim';

export interface DriverHistory {
    id?: number;
    licenceType?: DriverHistory.LicenceTypeEnum;
    licenseSince?: string|Date;
    licenceNo?: string;
    previousClaims?: Array<PreviousClaim>;
}
export namespace DriverHistory {
    export type LicenceTypeEnum = 'Full' | 'Provisional' | 'null';
    export const LicenceTypeEnum = {
        Full: 'Full' as LicenceTypeEnum,
        Provisional: 'Provisional' as LicenceTypeEnum,
        Null: 'null' as LicenceTypeEnum
    };
}
