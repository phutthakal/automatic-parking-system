-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 08, 2023 at 06:57 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `carlot`
--

-- --------------------------------------------------------

--
-- Table structure for table `card`
--

CREATE TABLE `card` (
  `card_id` int(100) NOT NULL,
  `user_height` varchar(100) NOT NULL,
  `user_license_plate` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `id` int(11) NOT NULL,
  `bay` varchar(10) NOT NULL,
  `noplate` varchar(100) NOT NULL,
  `zone` varchar(100) NOT NULL,
  `nolot` varchar(100) NOT NULL,
  `status` varchar(2) NOT NULL,
  `time` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`id`, `bay`, `noplate`, `zone`, `nolot`, `status`, `time`) VALUES
(1, 'A', 'กข1150', '1', 'A100', 'F', '2023-08-13 19:06:21'),
(2, 'B', 'ad1244', '1', 'B101', 'F', '2023-08-13 16:32:30'),
(3, 'C', 'นก1150', '2', 'C705', 'N', '2023-08-13 19:03:04'),
(4, 'D', 'ปสด123', '2', 'D302', 'F', '2023-08-13 16:11:40'),
(5, 'E', 'จน1250', '2', 'E705', 'N', '2023-08-24 16:33:21'),
(6, 'A', 'gr12', '1', 'A501', 'N', '2023-09-06 20:19:55'),
(7, 'D', 'asd444', '1', 'A705', 'N', '2023-09-06 20:20:10'),
(8, 'A', 'asd55', '1', 'A604', 'N', '2023-09-06 20:23:11'),
(9, '', '', '', '', '', '0000-00-00 00:00:00'),
(10, '', '', '', '', '', '0000-00-00 00:00:00'),
(11, '', '', '', '', '', '0000-00-00 00:00:00'),
(12, '', '', '', '', '', '0000-00-00 00:00:00'),
(13, '', '', '', '', '', '0000-00-00 00:00:00'),
(14, '', '', '', '', '', '0000-00-00 00:00:00'),
(15, '', '', '', '', '', '0000-00-00 00:00:00'),
(16, '', '', '', '', '', '0000-00-00 00:00:00'),
(17, '', '', '', '', '', '2023-07-16 20:26:42'),
(18, '', '', '', '', '', '2023-07-16 20:26:35'),
(19, '', '', '', '', '', '0000-00-00 00:00:00'),
(20, '', '', '', '', '', '2023-07-16 20:26:33'),
(21, '', '', '', '', '', '2023-07-16 20:26:13'),
(22, '', '', '', '', '', '2023-07-16 20:26:43');

-- --------------------------------------------------------

--
-- Table structure for table `lot`
--

CREATE TABLE `lot` (
  `lot_id` int(100) NOT NULL,
  `number` varchar(1000) NOT NULL,
  `status_id` int(10) NOT NULL,
  `bay` char(100) NOT NULL,
  `parking_zone_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lot`
--

INSERT INTO `lot` (`lot_id`, `number`, `status_id`, `bay`, `parking_zone_id`) VALUES
(1, 'A101', 1, 'A', 1),
(2, 'A102', 1, 'A', 1),
(3, 'A103', 1, 'A', 1),
(4, 'A104', 1, 'A', 1),
(5, 'A201', 1, 'A', 0),
(6, 'A202', 1, 'A', 0),
(7, 'A203', 1, 'A', 0),
(8, 'A204', 1, 'A', 0),
(9, 'A301', 1, 'A', 0),
(10, 'A302', 1, 'A', 0),
(11, 'A303', 1, 'A', 0),
(12, 'A304', 1, 'A', 0),
(13, 'A401', 1, 'A', 0),
(14, 'A402', 1, 'A', 0),
(15, 'A403', 1, 'A', 0),
(16, 'A404', 1, 'A', 0),
(17, 'A501', 1, 'A', 0),
(18, 'A502', 1, 'A', 0),
(19, 'A503', 1, 'A', 0),
(20, 'A504', 1, 'A', 0),
(21, 'A601', 1, 'A', 0),
(22, 'A602', 1, 'A', 0),
(23, 'A603', 1, 'A', 0),
(24, 'A604', 1, 'A', 0),
(25, 'A701', 1, 'A', 0),
(26, 'A702', 1, '', 0),
(27, 'A703', 1, '', 0),
(28, 'A704', 1, '', 0),
(29, 'A705', 1, '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `parking_store`
--

CREATE TABLE `parking_store` (
  `id` bigint(100) NOT NULL,
  `lot_id` int(10) NOT NULL,
  `time_in` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `parking_store`
--

INSERT INTO `parking_store` (`id`, `lot_id`, `time_in`) VALUES
(1, 1, '2023-09-05 19:13:36');

-- --------------------------------------------------------

--
-- Table structure for table `parking_zone`
--

CREATE TABLE `parking_zone` (
  `parking_zone_id` int(10) NOT NULL,
  `name_zone` char(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `parking_zone`
--

INSERT INTO `parking_zone` (`parking_zone_id`, `name_zone`) VALUES
(0, 'normal_zone'),
(1, 'over_zone');

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `status_id` int(10) NOT NULL,
  `name_status` char(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`status_id`, `name_status`) VALUES
(1, 'empty'),
(2, 'full'),
(3, 'new');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `card`
--
ALTER TABLE `card`
  ADD PRIMARY KEY (`card_id`);

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `lot`
--
ALTER TABLE `lot`
  ADD PRIMARY KEY (`lot_id`),
  ADD KEY `status_id` (`status_id`),
  ADD KEY `parking_zone_id` (`parking_zone_id`);

--
-- Indexes for table `parking_store`
--
ALTER TABLE `parking_store`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lot_id` (`lot_id`);

--
-- Indexes for table `parking_zone`
--
ALTER TABLE `parking_zone`
  ADD PRIMARY KEY (`parking_zone_id`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`status_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data`
--
ALTER TABLE `data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `lot`
--
ALTER TABLE `lot`
  ADD CONSTRAINT `lot_ibfk_1` FOREIGN KEY (`status_id`) REFERENCES `status` (`status_id`),
  ADD CONSTRAINT `lot_ibfk_2` FOREIGN KEY (`parking_zone_id`) REFERENCES `parking_zone` (`parking_zone_id`);

--
-- Constraints for table `parking_store`
--
ALTER TABLE `parking_store`
  ADD CONSTRAINT `parking_store_ibfk_1` FOREIGN KEY (`lot_id`) REFERENCES `lot` (`lot_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
