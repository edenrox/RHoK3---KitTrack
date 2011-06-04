-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 04, 2011 at 11:08 PM
-- Server version: 5.1.36
-- PHP Version: 5.3.0

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `rhok3`
--

-- --------------------------------------------------------

--
-- Table structure for table `carton_contents`
--

CREATE TABLE IF NOT EXISTS `carton_contents` (
  `carton_id` int(11) NOT NULL,
  `supply_item_id` int(11) NOT NULL,
  `quantity` double NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `carton_contents`
--


-- --------------------------------------------------------

--
-- Table structure for table `carton_types`
--

CREATE TABLE IF NOT EXISTS `carton_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kit_type_id` int(11) NOT NULL,
  `name` varchar(31) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=37 ;

--
-- Dumping data for table `carton_types`
--

INSERT INTO `carton_types` (`id`, `kit_type_id`, `name`) VALUES
(1, 1, '1'),
(2, 1, '2'),
(3, 1, '3'),
(4, 1, '4'),
(5, 1, '5'),
(6, 1, '6'),
(7, 1, '7'),
(8, 1, '8'),
(9, 1, '9'),
(10, 1, '10'),
(11, 1, '11'),
(12, 1, '12'),
(13, 1, '13'),
(14, 1, '14'),
(15, 1, '15'),
(16, 1, '16'),
(17, 1, '17'),
(18, 1, '18'),
(19, 1, '19'),
(20, 1, '20'),
(21, 1, '21'),
(22, 1, '22'),
(23, 1, '23'),
(24, 1, '24'),
(25, 1, '25'),
(26, 1, '26'),
(27, 1, '27'),
(28, 1, '28'),
(29, 1, '29'),
(30, 1, '30'),
(31, 1, '31'),
(32, 1, '32'),
(33, 1, '33'),
(34, 1, '34'),
(35, 1, '35'),
(36, 1, '36');

-- --------------------------------------------------------

--
-- Table structure for table `carton_uses`
--

CREATE TABLE IF NOT EXISTS `carton_uses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kit_id` int(11) NOT NULL,
  `carton_type_id` int(11) NOT NULL,
  `date_openned` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `carton_uses`
--


-- --------------------------------------------------------

--
-- Table structure for table `kits`
--

CREATE TABLE IF NOT EXISTS `kits` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `destination_location_id` int(11) NOT NULL,
  `kit_type_id` int(11) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `destination_location_id` (`destination_location_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `kits`
--


-- --------------------------------------------------------

--
-- Table structure for table `kit_histories`
--

CREATE TABLE IF NOT EXISTS `kit_histories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kit_id` int(11) NOT NULL,
  `location_id` int(11) NOT NULL,
  `kit_state_id` int(11) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kit_id` (`kit_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `kit_histories`
--


-- --------------------------------------------------------

--
-- Table structure for table `kit_states`
--

CREATE TABLE IF NOT EXISTS `kit_states` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(31) NOT NULL,
  `ordinal` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `kit_states`
--

INSERT INTO `kit_states` (`id`, `name`, `ordinal`) VALUES
(1, 'Preparation', 1),
(2, 'International Shipment', 2),
(3, 'Customs', 3),
(4, 'Local Delivery', 4),
(5, 'Use', 5);

-- --------------------------------------------------------

--
-- Table structure for table `kit_types`
--

CREATE TABLE IF NOT EXISTS `kit_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(63) NOT NULL,
  `created` datetime NOT NULL,
  `url` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `kit_types`
--

INSERT INTO `kit_types` (`id`, `name`, `created`, `url`) VALUES
(1, 'Interagency Emergency Health Kit', '2011-06-04 16:39:45', 'http://www.missionpharma.com/content/us/products/medical_kits/interagency_emergency_health_kit');

-- --------------------------------------------------------

--
-- Table structure for table `locations`
--

CREATE TABLE IF NOT EXISTS `locations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(31) NOT NULL,
  `lat` double NOT NULL,
  `lng` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `locations`
--

INSERT INTO `locations` (`id`, `name`, `lat`, `lng`) VALUES
(1, 'Calgary, AB', 51.01, 114.01),
(2, 'Edmonton, AB', 53.24, 113.28),
(3, 'Kingston, ON', 44.15, 76.3),
(4, 'Montreal, QC', 45.3, 73.35),
(5, 'Moose Jaw, SK', 50.37, 105.31),
(6, 'Ottawa, ON', 45.24, 75.43),
(7, 'Quebec, QC', 46.49, 71.11),
(8, 'St. John, NB', 45.18, 66.1),
(9, 'Toronto, ON', 43.4, 79.24),
(10, 'Vancouver, BC', 49.13, 123.06),
(11, 'Victoria, BC', 48.25, 123.21),
(12, 'Winnipeg, MB', 49.54, 97.07);

-- --------------------------------------------------------

--
-- Table structure for table `supply_items`
--

CREATE TABLE IF NOT EXISTS `supply_items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(31) NOT NULL,
  `supply_item_type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `supply_items`
--


-- --------------------------------------------------------

--
-- Table structure for table `supply_item_types`
--

CREATE TABLE IF NOT EXISTS `supply_item_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(31) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `supply_item_types`
--


