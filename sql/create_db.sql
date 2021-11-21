-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 22, 2021 at 12:23 AM
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
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `membership`
--

INSERT INTO `membership` (`id`, `user_id`, `start_date`, `end_date`, `type`) VALUES
(16, 9, '2021-11-27', '2021-11-27', 'Smart'),
(17, 9, '2021-11-30', '2021-11-30', 'Smart'),
(18, 9, '2021-11-28', '2021-11-28', 'Smart'),
(22, 9, '2021-11-21', '2030-02-23', 'Smart');

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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `quote`
--

INSERT INTO `quote` (`id`, `user_id`, `type`, `created`, `updated`, `is_complete`, `price`) VALUES
(19, 9, 'Home', 1637447797825, 1637447797825, 0, NULL),
(20, 9, 'Home', 1637461939132, 1637461939132, 0, NULL);

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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `password_hash`) VALUES
(9, 'a@a.a', '$pbkdf2-sha256$29000$aG1NqZUSAqC0FgIAwFiLMQ$Aq3DYDBkeVYcH5nc0sQjuaQhqhMn3qli7imh/eOKOvs'),
(11, 'bob@bob.bob', '$pbkdf2-sha256$29000$fa815tx7jxEiBGAMgZDSeg$mFOE0G2d0xpEJx6kISDF3zpmflid6ysacsZLRDWIdzY');

-- --------------------------------------------------------

--
-- Table structure for table `user_profile`
--

DROP TABLE IF EXISTS `user_profile`;
CREATE TABLE IF NOT EXISTS `user_profile` (
  `user_id` int(11) UNSIGNED NOT NULL,
  `name` varchar(60) NOT NULL,
  `points` int(11) NOT NULL DEFAULT 0,
  `role` enum('Member','Advisor') NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_profile`
--

INSERT INTO `user_profile` (`user_id`, `name`, `points`, `role`) VALUES
(9, 'Bobby Bob', 0, 'Member');

--
-- Constraints for dumped tables
--

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
  ADD CONSTRAINT `user_membership` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `quote`
--
ALTER TABLE `quote`
  ADD CONSTRAINT `user_quote` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `user_profile`
--
ALTER TABLE `user_profile`
  ADD CONSTRAINT `user_user_profile` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
