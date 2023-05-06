-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2021 at 08:26 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `office`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendtable`
--

CREATE TABLE `attendtable` (
  `name` varchar(100) NOT NULL,
  `sr_no` int(100) NOT NULL,
  `attfrom` date NOT NULL,
  `attto` date NOT NULL,
  `pdays` int(100) NOT NULL,
  `adays` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendtable`
--

INSERT INTO `attendtable` (`name`, `sr_no`, `attfrom`, `attto`, `pdays`, `adays`) VALUES
('akshit', 16, '2021-05-01', '2021-05-20', 18, 1),
('shallu', 17, '2021-05-01', '2021-05-31', 23, 7);

-- --------------------------------------------------------

--
-- Table structure for table `ordertable`
--

CREATE TABLE `ordertable` (
  `ordernumber` varchar(100) NOT NULL,
  `timestamp` varchar(100) NOT NULL,
  `day` int(100) NOT NULL,
  `revenue` varchar(100) NOT NULL,
  `estime` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ordertable`
--

INSERT INTO `ordertable` (`ordernumber`, `timestamp`, `day`, `revenue`, `estime`) VALUES
('7', '2021_5_17_14_17_41', 17, '46000', '0'),
('17', '2021_5_17_14_20_11', 17, '7000', '0'),
('79', '2021_5_17_14_28_31', 17, '92000', '0'),
('30', '2021_5_17_14_29_03', 17, '84000', '0');

-- --------------------------------------------------------

--
-- Table structure for table `phonebook`
--

CREATE TABLE `phonebook` (
  `occu` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `custname` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `phonebook`
--

INSERT INTO `phonebook` (`occu`, `email`, `custname`, `phone`) VALUES
('student', 'waliaakshit1972@gmail.com', 'akshit walia', '8968559107'),
('house wife', 'waliaakshit1972@gmail.com', 'shallu walia', '7696124055'),
('bussiness man ', 'waliaakshit1972@gmail.com', 'vishwas walia', '9417040102');

-- --------------------------------------------------------

--
-- Table structure for table `prodrank`
--

CREATE TABLE `prodrank` (
  `prod_names` varchar(100) NOT NULL,
  `rank` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `prodrank`
--

INSERT INTO `prodrank` (`prod_names`, `rank`) VALUES
('iphone11', 2),
('nokia 334', 1),
('oppo f1', 2),
('samsung fold 2', 1);

-- --------------------------------------------------------

--
-- Table structure for table `producttable`
--

CREATE TABLE `producttable` (
  `name` varchar(100) NOT NULL,
  `price` int(100) NOT NULL,
  `cat` varchar(100) NOT NULL,
  `esttime` varchar(100) NOT NULL,
  `image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `producttable`
--

INSERT INTO `producttable` (`name`, `price`, `cat`, `esttime`, `image`) VALUES
('iphone11', 92000, 'IOS', '0', '1621240608iphone.png'),
('nokia 334', 7000, 'KaiOS', '0', '1621240716nokia.png'),
('oppo f1', 23000, 'Android', '0', '1621240684oppo.png'),
('samsung fold 2', 84000, 'Android', '0', '1621240570samsung.png');

-- --------------------------------------------------------

--
-- Table structure for table `stafftable`
--

CREATE TABLE `stafftable` (
  `sr_no` int(10) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `qualf` varchar(100) NOT NULL,
  `salary` int(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `landline` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `DOB` date NOT NULL,
  `address` varchar(100) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `religion` varchar(100) NOT NULL,
  `strtdate` date NOT NULL,
  `bg` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stafftable`
--

INSERT INTO `stafftable` (`sr_no`, `fname`, `lname`, `qualf`, `salary`, `phone`, `landline`, `gender`, `DOB`, `address`, `image`, `religion`, `strtdate`, `bg`, `email`) VALUES
(16, 'akshit', 'walia', 'engineer', 5000, '8968559101', '2460578', 'Male', '2021-05-17', '911 mota singh nagar jalandhar punjab\n\n', '1621242879interest .png', 'Hindu', '2021-05-17', 'AB-', 'waliaakshit1972@gmail.com'),
(17, 'shallu', 'walia', 'engineer', 7000, '7696124055', '2442417', 'Female', '1999-06-01', '911 mota singh nagar jalandhar\n', '1621250838grass.png', 'Hindu', '2021-05-17', 'A+', 'waliaakshit1972@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE `usertable` (
  `uname` varchar(100) NOT NULL,
  `pass` varchar(100) NOT NULL,
  `utype` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `usertable`
--

INSERT INTO `usertable` (`uname`, `pass`, `utype`) VALUES
('akshit', 'akshit123', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendtable`
--
ALTER TABLE `attendtable`
  ADD PRIMARY KEY (`sr_no`);

--
-- Indexes for table `ordertable`
--
ALTER TABLE `ordertable`
  ADD PRIMARY KEY (`timestamp`);

--
-- Indexes for table `phonebook`
--
ALTER TABLE `phonebook`
  ADD PRIMARY KEY (`custname`);

--
-- Indexes for table `prodrank`
--
ALTER TABLE `prodrank`
  ADD PRIMARY KEY (`prod_names`);

--
-- Indexes for table `producttable`
--
ALTER TABLE `producttable`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `stafftable`
--
ALTER TABLE `stafftable`
  ADD PRIMARY KEY (`sr_no`);

--
-- Indexes for table `usertable`
--
ALTER TABLE `usertable`
  ADD PRIMARY KEY (`uname`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `stafftable`
--
ALTER TABLE `stafftable`
  MODIFY `sr_no` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
