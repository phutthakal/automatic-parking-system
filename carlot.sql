-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 03, 2023 at 01:02 PM
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
-- Table structure for table `bay`
--

CREATE TABLE `bay` (
  `bay_id` int(10) NOT NULL,
  `bay_name` char(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bay`
--

INSERT INTO `bay` (`bay_id`, `bay_name`) VALUES
(1, 'A'),
(2, 'B'),
(3, 'C'),
(4, 'D'),
(5, 'E'),
(6, 'F'),
(7, 'G'),
(8, 'H');

-- --------------------------------------------------------

--
-- Table structure for table `card`
--

CREATE TABLE `card` (
  `card_id` int(100) NOT NULL,
  `user_height` varchar(100) NOT NULL,
  `user_license_plate` varchar(100) NOT NULL,
  `lot_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `card`
--

INSERT INTO `card` (`card_id`, `user_height`, `user_license_plate`, `lot_id`) VALUES
(1, '180', 'กจ2880', 1),
(2, '199', 'ดก9999', 232);

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
  `bay_id` int(10) NOT NULL,
  `parking_type_id` int(10) NOT NULL,
  `parked_zone` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lot`
--

INSERT INTO `lot` (`lot_id`, `number`, `status_id`, `bay_id`, `parking_type_id`, `parked_zone`) VALUES
(1, 'A101', 2, 1, 1, 1),
(2, 'A102', 1, 1, 1, 1),
(3, 'A103', 1, 1, 1, 1),
(4, 'A104', 2, 1, 1, 1),
(5, 'A201', 2, 1, 0, 1),
(6, 'A202', 2, 1, 0, 1),
(7, 'A203', 1, 1, 0, 1),
(8, 'A204', 2, 1, 0, 1),
(9, 'A301', 1, 1, 0, 1),
(10, 'A302', 1, 1, 0, 1),
(11, 'A303', 1, 1, 0, 1),
(12, 'A304', 1, 1, 0, 1),
(13, 'A401', 1, 1, 0, 1),
(14, 'A402', 1, 1, 0, 1),
(15, 'A403', 1, 1, 0, 1),
(16, 'A404', 1, 1, 0, 1),
(17, 'A501', 1, 1, 0, 1),
(18, 'A502', 1, 1, 0, 1),
(19, 'A503', 1, 1, 0, 1),
(20, 'A504', 1, 1, 0, 1),
(21, 'A601', 1, 1, 0, 1),
(22, 'A602', 1, 1, 0, 1),
(23, 'A603', 1, 1, 0, 1),
(24, 'A604', 1, 1, 0, 1),
(25, 'A701', 1, 1, 0, 1),
(26, 'A702', 1, 1, 0, 1),
(27, 'A703', 1, 1, 0, 1),
(28, 'A704', 1, 1, 0, 1),
(29, 'A705', 1, 1, 0, 1),
(30, 'B101', 1, 2, 1, 1),
(31, 'B102', 1, 2, 1, 1),
(32, 'B103', 1, 2, 1, 1),
(33, 'B104', 1, 2, 1, 1),
(34, 'B201', 1, 2, 0, 1),
(35, 'B202', 1, 2, 0, 1),
(36, 'B203', 1, 2, 0, 1),
(37, 'B204', 1, 2, 0, 1),
(38, 'B301', 1, 2, 0, 1),
(39, 'B302', 1, 2, 0, 1),
(40, 'B303', 1, 2, 0, 1),
(41, 'B304', 1, 2, 0, 1),
(42, 'B401', 1, 2, 0, 1),
(43, 'B402', 1, 2, 0, 1),
(44, 'B403', 1, 2, 0, 1),
(45, 'B404', 1, 2, 0, 1),
(46, 'B501', 1, 2, 0, 1),
(47, 'B502', 1, 2, 0, 1),
(48, 'B503', 1, 2, 0, 1),
(49, 'B504', 1, 2, 0, 1),
(50, 'B601', 1, 2, 0, 1),
(51, 'B602', 1, 2, 0, 1),
(52, 'B603', 1, 2, 0, 1),
(53, 'B604', 1, 2, 0, 1),
(54, 'B701', 1, 2, 0, 1),
(55, 'B702', 1, 2, 0, 1),
(56, 'B703', 1, 2, 0, 1),
(57, 'B704', 1, 2, 0, 1),
(58, 'B705', 1, 2, 0, 1),
(59, 'C101', 1, 3, 1, 2),
(60, 'C102', 1, 3, 1, 2),
(61, 'C103', 1, 3, 1, 2),
(62, 'C104', 1, 3, 1, 2),
(63, 'C201', 1, 3, 0, 2),
(64, 'C202', 1, 3, 0, 2),
(65, 'C203', 1, 3, 0, 2),
(66, 'C204', 1, 3, 0, 2),
(67, 'C301', 1, 3, 0, 2),
(68, 'C302', 1, 3, 0, 2),
(69, 'C303', 1, 3, 0, 2),
(70, 'C304', 1, 3, 0, 2),
(71, 'C401', 1, 3, 0, 2),
(72, 'C402', 1, 3, 0, 2),
(73, 'C403', 1, 3, 0, 2),
(74, 'C404', 1, 3, 0, 2),
(75, 'C501', 1, 3, 0, 2),
(76, 'C502', 1, 3, 0, 2),
(77, 'C503', 1, 3, 0, 2),
(78, 'C504', 1, 3, 0, 2),
(79, 'C601', 1, 3, 0, 2),
(80, 'C602', 1, 3, 0, 2),
(81, 'C603', 1, 3, 0, 2),
(82, 'C604', 1, 3, 0, 2),
(83, 'C701', 1, 3, 0, 2),
(84, 'C702', 1, 3, 0, 2),
(85, 'C703', 1, 3, 0, 2),
(86, 'C704', 1, 3, 0, 2),
(87, 'C705', 1, 3, 0, 2),
(88, 'D101', 1, 4, 1, 2),
(89, 'D102', 1, 4, 1, 2),
(90, 'D103', 1, 4, 1, 2),
(91, 'D104', 1, 4, 1, 2),
(92, 'D201', 1, 4, 0, 2),
(93, 'D202', 1, 4, 0, 2),
(94, 'D203', 1, 4, 0, 2),
(95, 'D204', 1, 4, 0, 2),
(96, 'D301', 1, 4, 0, 2),
(97, 'D302', 1, 4, 0, 2),
(98, 'D303', 1, 4, 0, 2),
(99, 'D304', 1, 4, 0, 2),
(100, 'D401', 1, 4, 0, 2),
(101, 'D402', 1, 4, 0, 2),
(102, 'D403', 1, 4, 0, 2),
(103, 'D404', 1, 4, 0, 2),
(104, 'D501', 1, 4, 0, 2),
(105, 'D502', 1, 4, 0, 2),
(106, 'D503', 1, 4, 0, 2),
(107, 'D504', 1, 4, 0, 2),
(108, 'D601', 1, 4, 0, 2),
(109, 'D602', 1, 4, 0, 2),
(110, 'D603', 1, 4, 0, 2),
(111, 'D604', 1, 4, 0, 2),
(112, 'D701', 1, 4, 0, 2),
(113, 'D702', 1, 4, 0, 2),
(114, 'D703', 1, 4, 0, 2),
(115, 'D704', 1, 4, 0, 2),
(116, 'D705', 1, 4, 0, 2),
(117, 'E101', 1, 5, 1, 2),
(118, 'E102', 1, 5, 1, 2),
(119, 'E103', 1, 5, 1, 2),
(120, 'E104', 1, 5, 1, 2),
(121, 'E201', 1, 5, 0, 2),
(122, 'E202', 1, 5, 0, 2),
(123, 'E203', 1, 5, 0, 2),
(124, 'E204', 1, 5, 0, 2),
(125, 'E301', 1, 5, 0, 2),
(126, 'E302', 1, 5, 0, 2),
(127, 'E303', 1, 5, 0, 2),
(128, 'E304', 1, 5, 0, 2),
(129, 'E401', 1, 5, 0, 2),
(130, 'E402', 1, 5, 0, 2),
(131, 'E403', 1, 5, 0, 2),
(132, 'E404', 1, 5, 0, 2),
(133, 'E501', 1, 5, 0, 2),
(134, 'E502', 1, 5, 0, 2),
(135, 'E503', 1, 5, 0, 2),
(136, 'E504', 1, 5, 0, 2),
(137, 'E601', 1, 5, 0, 2),
(138, 'E602', 1, 5, 0, 2),
(139, 'E603', 1, 5, 0, 2),
(140, 'E604', 1, 5, 0, 2),
(141, 'E701', 1, 5, 0, 2),
(142, 'E702', 1, 5, 0, 2),
(143, 'E703', 1, 5, 0, 2),
(144, 'E704', 1, 5, 0, 2),
(145, 'E705', 1, 5, 0, 2),
(146, 'F101', 1, 6, 1, 2),
(147, 'F102', 1, 6, 1, 2),
(148, 'F103', 1, 6, 1, 2),
(149, 'F104', 1, 6, 1, 2),
(150, 'F201', 1, 6, 0, 2),
(151, 'F202', 1, 6, 0, 2),
(152, 'F203', 1, 6, 0, 2),
(153, 'F204', 1, 6, 0, 2),
(154, 'F301', 1, 6, 0, 2),
(155, 'F302', 1, 6, 0, 2),
(156, 'F303', 1, 6, 0, 2),
(157, 'F304', 1, 6, 0, 2),
(158, 'F401', 1, 6, 0, 2),
(159, 'F402', 1, 6, 0, 2),
(160, 'F403', 1, 6, 0, 2),
(161, 'F404', 1, 6, 0, 2),
(162, 'F501', 1, 6, 0, 2),
(163, 'F502', 1, 6, 0, 2),
(164, 'F503', 1, 6, 0, 2),
(165, 'F504', 1, 6, 0, 2),
(166, 'F601', 1, 6, 0, 2),
(167, 'F602', 1, 6, 0, 2),
(168, 'F603', 1, 6, 0, 2),
(169, 'F604', 1, 6, 0, 2),
(170, 'F701', 1, 6, 0, 2),
(171, 'F702', 1, 6, 0, 2),
(172, 'F703', 1, 6, 0, 2),
(173, 'F704', 1, 6, 0, 2),
(174, 'F705', 1, 6, 0, 2),
(175, 'G101', 1, 7, 1, 2),
(176, 'G102', 1, 7, 1, 2),
(177, 'G103', 1, 7, 1, 2),
(178, 'G104', 1, 7, 1, 2),
(179, 'G201', 1, 7, 0, 2),
(180, 'G202', 1, 7, 0, 2),
(181, 'G203', 1, 7, 0, 2),
(182, 'G204', 1, 7, 0, 2),
(183, 'G301', 1, 7, 0, 2),
(184, 'G302', 1, 7, 0, 2),
(185, 'G303', 1, 7, 0, 2),
(186, 'G304', 1, 7, 0, 2),
(187, 'G401', 1, 7, 0, 2),
(188, 'G402', 1, 7, 0, 2),
(189, 'G403', 1, 7, 0, 2),
(190, 'G404', 1, 7, 0, 2),
(191, 'G501', 1, 7, 0, 2),
(192, 'G502', 1, 7, 0, 2),
(193, 'G503', 1, 7, 0, 2),
(194, 'G504', 1, 7, 0, 2),
(195, 'G601', 1, 7, 0, 2),
(196, 'G602', 1, 7, 0, 2),
(197, 'G603', 1, 7, 0, 2),
(198, 'G604', 1, 7, 0, 2),
(199, 'G701', 1, 7, 0, 2),
(200, 'G702', 1, 7, 0, 2),
(201, 'G703', 1, 7, 0, 2),
(202, 'G704', 1, 7, 0, 2),
(203, 'G705', 1, 7, 0, 2),
(204, 'H101', 1, 8, 1, 2),
(205, 'H102', 1, 8, 1, 2),
(206, 'H103', 1, 8, 1, 2),
(207, 'H104', 1, 8, 1, 2),
(208, 'H201', 1, 8, 0, 2),
(209, 'H202', 1, 8, 0, 2),
(210, 'H203', 1, 8, 0, 2),
(211, 'H204', 1, 8, 0, 2),
(212, 'H301', 1, 8, 0, 2),
(213, 'H302', 1, 8, 0, 2),
(214, 'H303', 1, 8, 0, 2),
(215, 'H304', 1, 8, 0, 2),
(216, 'H401', 1, 8, 0, 2),
(217, 'H402', 1, 8, 0, 2),
(218, 'H403', 1, 8, 0, 2),
(219, 'H404', 1, 8, 0, 2),
(220, 'H501', 1, 8, 0, 2),
(221, 'H502', 1, 8, 0, 2),
(222, 'H503', 1, 8, 0, 2),
(223, 'H504', 1, 8, 0, 2),
(224, 'H601', 1, 8, 0, 2),
(225, 'H602', 1, 8, 0, 2),
(226, 'H603', 1, 8, 0, 2),
(227, 'H604', 1, 8, 0, 2),
(228, 'H701', 1, 8, 0, 2),
(229, 'H702', 1, 8, 0, 2),
(230, 'H703', 1, 8, 0, 2),
(231, 'H704', 1, 8, 0, 2),
(232, 'H705', 1, 8, 0, 2);

-- --------------------------------------------------------

--
-- Table structure for table `parked_store`
--

CREATE TABLE `parked_store` (
  `id` bigint(100) NOT NULL,
  `lot_id` int(10) NOT NULL,
  `time_in` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `parked_store`
--

INSERT INTO `parked_store` (`id`, `lot_id`, `time_in`) VALUES
(1, 1, '2023-09-10 17:40:45');

-- --------------------------------------------------------

--
-- Table structure for table `parking_type`
--

CREATE TABLE `parking_type` (
  `parking_type_id` int(10) NOT NULL,
  `type_name` char(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `parking_type`
--

INSERT INTO `parking_type` (`parking_type_id`, `type_name`) VALUES
(0, 'normal'),
(1, 'over_height');

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
-- Indexes for table `bay`
--
ALTER TABLE `bay`
  ADD PRIMARY KEY (`bay_id`);

--
-- Indexes for table `card`
--
ALTER TABLE `card`
  ADD PRIMARY KEY (`card_id`),
  ADD KEY `lot_id` (`lot_id`);

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
  ADD KEY `parking_type_id` (`parking_type_id`),
  ADD KEY `status_id` (`status_id`),
  ADD KEY `bay_id` (`bay_id`);

--
-- Indexes for table `parked_store`
--
ALTER TABLE `parked_store`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lot_id` (`lot_id`);

--
-- Indexes for table `parking_type`
--
ALTER TABLE `parking_type`
  ADD PRIMARY KEY (`parking_type_id`);

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
-- Constraints for table `card`
--
ALTER TABLE `card`
  ADD CONSTRAINT `card_ibfk_1` FOREIGN KEY (`lot_id`) REFERENCES `lot` (`lot_id`);

--
-- Constraints for table `lot`
--
ALTER TABLE `lot`
  ADD CONSTRAINT `lot_ibfk_1` FOREIGN KEY (`status_id`) REFERENCES `status` (`status_id`),
  ADD CONSTRAINT `lot_ibfk_2` FOREIGN KEY (`parking_type_id`) REFERENCES `parking_type` (`parking_type_id`),
  ADD CONSTRAINT `lot_ibfk_3` FOREIGN KEY (`bay_id`) REFERENCES `bay` (`bay_id`);

--
-- Constraints for table `parked_store`
--
ALTER TABLE `parked_store`
  ADD CONSTRAINT `parked_store_ibfk_1` FOREIGN KEY (`lot_id`) REFERENCES `lot` (`lot_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
