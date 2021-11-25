-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 25, 2021 at 03:12 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sis_data`
--
CREATE DATABASE IF NOT EXISTS `sis_data` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `sis_data`;

-- --------------------------------------------------------

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
CREATE TABLE IF NOT EXISTS `address` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `number_or_name` varchar(50) DEFAULT NULL,
  `street` varchar(100) DEFAULT NULL,
  `town` varchar(100) DEFAULT NULL,
  `county` varchar(100) DEFAULT NULL,
  `postcode` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `address`
--

INSERT INTO `address` (`id`, `number_or_name`, `street`, `town`, `county`, `postcode`) VALUES
(50, 'fsg', 'fgd', 'fgd', 'gfd', 'gf');

-- --------------------------------------------------------

--
-- Table structure for table `driver_details`
--

DROP TABLE IF EXISTS `driver_details`;
CREATE TABLE IF NOT EXISTS `driver_details` (
  `quote_id` int(11) UNSIGNED NOT NULL,
  `driver_history_id` int(11) UNSIGNED NOT NULL,
  `personal_details_id` int(11) UNSIGNED NOT NULL,
  PRIMARY KEY (`quote_id`),
  KEY `driver_history_driver_details` (`driver_history_id`),
  KEY `personal_details_driver_details` (`personal_details_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `driver_details`
--

INSERT INTO `driver_details` (`quote_id`, `driver_history_id`, `personal_details_id`) VALUES
(59, 69, 47);

-- --------------------------------------------------------

--
-- Table structure for table `driver_history`
--

DROP TABLE IF EXISTS `driver_history`;
CREATE TABLE IF NOT EXISTS `driver_history` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `licence_type` enum('Full','Provisional','') DEFAULT '',
  `license_since` date DEFAULT NULL,
  `licence_no` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `driver_history`
--

INSERT INTO `driver_history` (`id`, `licence_type`, `license_since`, `licence_no`) VALUES
(42, 'Full', '2000-01-23', 'licence_no'),
(44, 'Full', '2000-01-23', 'licence_no'),
(48, 'Full', '2000-01-23', 'licence_no'),
(51, 'Full', '2000-01-23', 'licence_no'),
(52, 'Full', '2000-01-23', 'licence_no'),
(54, NULL, NULL, NULL),
(55, NULL, NULL, NULL),
(56, NULL, NULL, NULL),
(57, NULL, NULL, NULL),
(58, NULL, NULL, NULL),
(59, NULL, NULL, NULL),
(60, NULL, NULL, NULL),
(61, NULL, NULL, NULL),
(62, NULL, NULL, NULL),
(63, NULL, NULL, NULL),
(64, NULL, NULL, NULL),
(65, NULL, NULL, NULL),
(66, NULL, NULL, NULL),
(67, NULL, NULL, NULL),
(68, NULL, NULL, NULL),
(69, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `home_details`
--

DROP TABLE IF EXISTS `home_details`;
CREATE TABLE IF NOT EXISTS `home_details` (
  `quote_id` int(11) UNSIGNED NOT NULL,
  `address_id` int(11) UNSIGNED NOT NULL,
  PRIMARY KEY (`quote_id`),
  KEY `home_details_address` (`address_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `home_details`
--

INSERT INTO `home_details` (`quote_id`, `address_id`) VALUES
(60, 50),
(61, 50);

-- --------------------------------------------------------

--
-- Table structure for table `insurance_package`
--

DROP TABLE IF EXISTS `insurance_package`;
CREATE TABLE IF NOT EXISTS `insurance_package` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` enum('Home','Motor') NOT NULL,
  `name` varchar(50) NOT NULL,
  `details` text NOT NULL,
  `base_annual_price` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `insurance_package`
--

INSERT INTO `insurance_package` (`id`, `type`, `name`, `details`, `base_annual_price`) VALUES
(1, 'Home', 'Basic', 'Basic stuff', 62);

-- --------------------------------------------------------

--
-- Table structure for table `insurance_policy`
--

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `insurance_policy`
--

INSERT INTO `insurance_policy` (`id`, `user_id`, `package_id`, `start_date`, `end_date`) VALUES
(1, 9, 1, '2021-11-19', '2022-11-01');

-- --------------------------------------------------------

--
-- Table structure for table `membership`
--

DROP TABLE IF EXISTS `membership`;
CREATE TABLE IF NOT EXISTS `membership` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` int(11) UNSIGNED NOT NULL,
  `start_date` date NOT NULL DEFAULT current_timestamp(),
  `end_date` date NOT NULL,
  `type` enum('Smart','Silver','Gold') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_membership` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `membership`
--

INSERT INTO `membership` (`id`, `user_id`, `start_date`, `end_date`, `type`) VALUES
(16, 9, '2021-11-27', '2021-11-27', 'Smart'),
(17, 9, '2021-11-30', '2021-11-30', 'Smart'),
(18, 9, '2021-11-28', '2021-11-28', 'Smart'),
(22, 9, '2021-11-21', '2021-11-22', 'Smart'),
(23, 9, '2021-11-24', '2022-02-18', 'Gold');

-- --------------------------------------------------------

--
-- Table structure for table `personal_details`
--

DROP TABLE IF EXISTS `personal_details`;
CREATE TABLE IF NOT EXISTS `personal_details` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `full_name` text DEFAULT NULL,
  `address_id` int(11) UNSIGNED NOT NULL,
  `dob` date DEFAULT NULL,
  `relationship_status` enum('Single','Married') DEFAULT NULL,
  `home_owner` tinyint(1) DEFAULT NULL,
  `dependents` tinyint(4) DEFAULT NULL,
  `employment_status` enum('FullTime','PartTime','Unemployed','Retired','Student') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `personal_details_address` (`address_id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `personal_details`
--

INSERT INTO `personal_details` (`id`, `full_name`, `address_id`, `dob`, `relationship_status`, `home_owner`, `dependents`, `employment_status`) VALUES
(47, 'vcvxcvvxddad', 50, '2000-09-20', 'Single', 1, 5, 'Unemployed');

-- --------------------------------------------------------

--
-- Table structure for table `previous_claim`
--

DROP TABLE IF EXISTS `previous_claim`;
CREATE TABLE IF NOT EXISTS `previous_claim` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `driver_history_id` int(11) UNSIGNED NOT NULL,
  `date` date NOT NULL,
  `fault` enum('Self','ThirdParty') NOT NULL,
  `claim_type` enum('Accident','Theft') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `driver_history_previous_claim` (`driver_history_id`)
) ENGINE=InnoDB AUTO_INCREMENT=122 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `previous_claim`
--

INSERT INTO `previous_claim` (`id`, `driver_history_id`, `date`, `fault`, `claim_type`) VALUES
(43, 42, '2000-01-23', 'Self', 'Accident'),
(44, 42, '2000-01-23', 'Self', 'Accident'),
(47, 44, '2000-01-23', 'Self', 'Accident'),
(48, 44, '2000-01-23', 'Self', 'Accident'),
(55, 48, '2000-01-23', 'Self', 'Accident'),
(56, 48, '2000-01-23', 'Self', 'Accident'),
(62, 49, '2000-01-23', 'Self', 'Accident'),
(63, 49, '2000-01-23', 'Self', 'Accident'),
(68, 51, '2000-01-23', 'Self', 'Accident'),
(69, 51, '2000-01-23', 'Self', 'Accident'),
(70, 5, '2000-01-23', 'Self', 'Accident'),
(71, 5, '2000-01-23', 'Self', 'Accident'),
(120, 52, '2000-01-23', 'Self', 'Accident'),
(121, 52, '2000-01-23', 'Self', 'Accident');

-- --------------------------------------------------------

--
-- Table structure for table `quote`
--

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
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `quote`
--

INSERT INTO `quote` (`id`, `user_id`, `type`, `created`, `updated`, `is_complete`, `price`) VALUES
(59, 9, 'Motor', 1637837949424, 1637849345641, 1, 948.99),
(60, 9, 'Home', 1637845412195, 1637845412195, 0, NULL),
(61, 9, 'Home', 1637845416681, 1637845416681, 0, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `quote_sections`
--

DROP TABLE IF EXISTS `quote_sections`;
CREATE TABLE IF NOT EXISTS `quote_sections` (
  `quote_id` int(11) UNSIGNED NOT NULL,
  `quote_type` enum('Home','Motor') NOT NULL,
  `personal_details_id` int(11) UNSIGNED DEFAULT NULL,
  `home_details_id` int(11) UNSIGNED DEFAULT NULL,
  PRIMARY KEY (`quote_id`),
  KEY `personal_details_quote_sections` (`personal_details_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `quote_sections`
--

INSERT INTO `quote_sections` (`quote_id`, `quote_type`, `personal_details_id`, `home_details_id`) VALUES
(59, 'Motor', NULL, NULL),
(60, 'Home', NULL, NULL),
(61, 'Home', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `email` varchar(30) NOT NULL,
  `password_hash` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `password_hash`) VALUES
(9, 'a@a.a', '$pbkdf2-sha256$29000$p3SuVSrFuDeGcI4xJuRcKw$6.qkGbAVld9zfHApW3z9OG6aD6oN57nWNMmE30/0sL0'),
(11, 'bob@bob.bob', '$pbkdf2-sha256$29000$fa815tx7jxEiBGAMgZDSeg$mFOE0G2d0xpEJx6kISDF3zpmflid6ysacsZLRDWIdzY');

-- --------------------------------------------------------

--
-- Table structure for table `user_profile`
--

DROP TABLE IF EXISTS `user_profile`;
CREATE TABLE IF NOT EXISTS `user_profile` (
  `user_id` int(11) UNSIGNED NOT NULL,
  `personal_details_id` int(11) UNSIGNED DEFAULT NULL,
  `driver_history_id` int(11) UNSIGNED DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_profile`
--

INSERT INTO `user_profile` (`user_id`, `personal_details_id`, `driver_history_id`) VALUES
(9, 47, 52);

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_details`
--

DROP TABLE IF EXISTS `vehicle_details`;
CREATE TABLE IF NOT EXISTS `vehicle_details` (
  `quote_id` int(11) UNSIGNED NOT NULL,
  `alarm_fitter` tinyint(1) DEFAULT NULL,
  `immobilizer_fitted` tinyint(1) DEFAULT NULL,
  `tracking_device_fitted` tinyint(1) DEFAULT NULL,
  `is_import` tinyint(1) DEFAULT NULL,
  `off_side_drive` tinyint(1) DEFAULT NULL,
  `number_of_seats` tinyint(4) DEFAULT NULL,
  `current_value` decimal(10,0) DEFAULT NULL,
  `is_modified` tinyint(4) DEFAULT NULL,
  `section_complete` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`quote_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_details`
--

INSERT INTO `vehicle_details` (`quote_id`, `alarm_fitter`, `immobilizer_fitted`, `tracking_device_fitted`, `is_import`, `off_side_drive`, `number_of_seats`, `current_value`, `is_modified`, `section_complete`) VALUES
(59, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_usage`
--

DROP TABLE IF EXISTS `vehicle_usage`;
CREATE TABLE IF NOT EXISTS `vehicle_usage` (
  `quote_id` int(11) UNSIGNED NOT NULL,
  `usage_type` enum('SDP','SDPC','SDPCB') DEFAULT NULL,
  `annual_milage` int(11) DEFAULT NULL,
  `day_storage` enum('Home','CarParkOffice','CarParkPublic','StreetAwayFromHome') DEFAULT NULL,
  `night_storage` enum('Drive','StreetOutsideHome','StreetAwayFromHome','Garage') DEFAULT NULL,
  `night_storage_at_home` tinyint(1) DEFAULT NULL,
  `night_storage_address` int(11) UNSIGNED DEFAULT NULL,
  `section_complete` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`quote_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_usage`
--

INSERT INTO `vehicle_usage` (`quote_id`, `usage_type`, `annual_milage`, `day_storage`, `night_storage`, `night_storage_at_home`, `night_storage_address`, `section_complete`) VALUES
(59, NULL, NULL, NULL, NULL, NULL, NULL, 0);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `driver_details`
--
ALTER TABLE `driver_details`
  ADD CONSTRAINT `driver_details_quote` FOREIGN KEY (`quote_id`) REFERENCES `quote` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `driver_history_driver_details` FOREIGN KEY (`driver_history_id`) REFERENCES `driver_history` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `personal_details_driver_details` FOREIGN KEY (`personal_details_id`) REFERENCES `personal_details` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `home_details`
--
ALTER TABLE `home_details`
  ADD CONSTRAINT `home_details_address` FOREIGN KEY (`address_id`) REFERENCES `address` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `quote_home_details` FOREIGN KEY (`quote_id`) REFERENCES `quote` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `insurance_policy`
--
ALTER TABLE `insurance_policy`
  ADD CONSTRAINT `insurance_package_insurance_policy` FOREIGN KEY (`package_id`) REFERENCES `insurance_package` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `user_insurance_policy` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `membership`
--
ALTER TABLE `membership`
  ADD CONSTRAINT `user_membership` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `personal_details`
--
ALTER TABLE `personal_details`
  ADD CONSTRAINT `personal_details_address` FOREIGN KEY (`address_id`) REFERENCES `address` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `quote`
--
ALTER TABLE `quote`
  ADD CONSTRAINT `user_quote` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `quote_sections`
--
ALTER TABLE `quote_sections`
  ADD CONSTRAINT `personal_details_quote_sections` FOREIGN KEY (`personal_details_id`) REFERENCES `personal_details` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `quote_quote_sections` FOREIGN KEY (`quote_id`) REFERENCES `quote` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `user_profile`
--
ALTER TABLE `user_profile`
  ADD CONSTRAINT `user_user_profile` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `vehicle_details`
--
ALTER TABLE `vehicle_details`
  ADD CONSTRAINT `quote_vehicle_details` FOREIGN KEY (`quote_id`) REFERENCES `quote` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `vehicle_usage`
--
ALTER TABLE `vehicle_usage`
  ADD CONSTRAINT `quote_vehicle_usage` FOREIGN KEY (`quote_id`) REFERENCES `quote` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
