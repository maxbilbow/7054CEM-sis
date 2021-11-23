SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


DROP TABLE IF EXISTS `address`;
CREATE TABLE IF NOT EXISTS `address` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `number_or_name` varchar(50) DEFAULT NULL,
  `street` varchar(100) DEFAULT NULL,
  `town` varchar(100) DEFAULT NULL,
  `county` varchar(100) DEFAULT NULL,
  `postcode` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `driver_history`;
CREATE TABLE IF NOT EXISTS `driver_history` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `licence_type` enum('Full','Provisional','') NOT NULL DEFAULT '',
  `license_since` date DEFAULT NULL,
  `licence_no` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `insurance_package`;
CREATE TABLE IF NOT EXISTS `insurance_package` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` enum('Home','Motor') NOT NULL,
  `name` varchar(50) NOT NULL,
  `details` text NOT NULL,
  `base_annual_price` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `insurance_policy`;
CREATE TABLE IF NOT EXISTS `insurance_policy` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` int(11) UNSIGNED NOT NULL,
  `package_id` int(11) UNSIGNED NOT NULL,
  `start_date` date NOT NULL DEFAULT current_timestamp(),
  `end_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `insurance_package_insurance_policy` (`package_id`),
  KEY `user_insurance_policy` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `membership`;
CREATE TABLE IF NOT EXISTS `membership` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` int(11) UNSIGNED NOT NULL,
  `start_date` date NOT NULL DEFAULT current_timestamp(),
  `end_date` date NOT NULL,
  `type` enum('Smart','Silver','Gold') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_membership` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `personal_details`;
CREATE TABLE IF NOT EXISTS `personal_details` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `full_name` text NOT NULL DEFAULT '',
  `address_id` int(11) UNSIGNED DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `relationship_status` enum('Single','Married','') NOT NULL DEFAULT '',
  `home_owner` tinyint(1) DEFAULT NULL,
  `dependents` tinyint(4) DEFAULT NULL,
  `employment_status` enum('FullTime','PartTime','Unemployed','Retired','Student','') NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `personal_details_address` (`address_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `previous_claim`;
CREATE TABLE IF NOT EXISTS `previous_claim` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `driver_history_id` int(11) UNSIGNED NOT NULL,
  `date` date NOT NULL,
  `fault` enum('Self','ThirdParty') NOT NULL,
  `claim_type` enum('Accident','Theft') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `driver_history_previous_claim` (`driver_history_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `quote`;
CREATE TABLE IF NOT EXISTS `quote` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` int(11) UNSIGNED NOT NULL,
  `type` enum('Home','Motor') NOT NULL,
  `created` bigint(20) NOT NULL,
  `updated` bigint(20) NOT NULL,
  `is_complete` tinyint(1) NOT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_quote` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `email` varchar(30) NOT NULL,
  `password_hash` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `user_profile`;
CREATE TABLE IF NOT EXISTS `user_profile` (
  `user_id` int(11) UNSIGNED NOT NULL,
  `personal_details_id` int(11) UNSIGNED DEFAULT NULL,
  `driver_history_id` int(11) UNSIGNED DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


ALTER TABLE `insurance_policy`
  ADD CONSTRAINT `insurance_package_insurance_policy` FOREIGN KEY (`package_id`) REFERENCES `insurance_package` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `user_insurance_policy` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `membership`
  ADD CONSTRAINT `user_membership` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON UPDATE CASCADE;

ALTER TABLE `personal_details`
  ADD CONSTRAINT `personal_details_address` FOREIGN KEY (`address_id`) REFERENCES `address` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE `previous_claim`
  ADD CONSTRAINT `driver_history_previous_claim` FOREIGN KEY (`driver_history_id`) REFERENCES `driver_history` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `quote`
  ADD CONSTRAINT `user_quote` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `user_profile`
  ADD CONSTRAINT `user_user_profile` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
