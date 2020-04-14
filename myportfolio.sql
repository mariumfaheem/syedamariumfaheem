-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2020 at 02:54 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `myportfolio`
--

-- --------------------------------------------------------

--
-- Table structure for table `client_review`
--

CREATE TABLE `client_review` (
  `sno` int(11) NOT NULL,
  `c_name` varchar(50) NOT NULL,
  `c_title` text NOT NULL,
  `c_content` text NOT NULL,
  `c_image` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `client_review`
--

INSERT INTO `client_review` (`sno`, `c_name`, `c_title`, `c_content`, `c_image`) VALUES
(1, 'Ethan McCown', 'pakistani', '“Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.”', '7.jpg'),
(3, 'kled', 'CEO ', 'kakssd', '');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone_num` varchar(15) NOT NULL,
  `msg` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `email`, `phone_num`, `msg`) VALUES
(1, 'Exterior Car Washing', 'mariums82@gmail.com', '2939494', 'dmd,,dm'),
(2, 'Exterior Car Washing', 'mariums82@gmail.com', '2939494', 'dmd,,dm'),
(3, 'Exterior Car Washing', 'mariums82@gmail.com', '2939494', 'dmd,,dm'),
(4, 'Exterior Car Washing', 'mariums82@gmail.com', '2939494', 'dmd,,dm');

-- --------------------------------------------------------

--
-- Table structure for table `education`
--

CREATE TABLE `education` (
  `sno` int(50) NOT NULL,
  `in_name` text NOT NULL,
  `in_des` text NOT NULL,
  `in_city` text NOT NULL,
  `in_date_s` varchar(12) NOT NULL,
  `in_date_l` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `education`
--

INSERT INTO `education` (`sno`, `in_name`, `in_des`, `in_city`, `in_date_s`, `in_date_l`) VALUES
(1, 'NED University of Engineering and technology', 'BE in Computer and Information System', 'Karachi', 'December 201', 'In Progress'),
(2, 'BAMM PECHS Government College', 'Intermediate in Pre-Engineering with A+', 'Karachi', 'October 2014', 'July 2016'),
(5, 'Metropolis Education System', 'Matriculation in Science with A+', 'Karachi', 'April 2012', 'July 2014');

-- --------------------------------------------------------

--
-- Table structure for table `experince`
--

CREATE TABLE `experince` (
  `sno` int(50) NOT NULL,
  `e_name` varchar(50) NOT NULL,
  `e_role` varchar(50) NOT NULL,
  `e_title` varchar(50) NOT NULL,
  `s_date` varchar(20) NOT NULL,
  `l_date` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `experince`
--

INSERT INTO `experince` (`sno`, `e_name`, `e_role`, `e_title`, `s_date`, `l_date`) VALUES
(1, 'Pakistan Meteorological Department', 'Knowledge about function of Pakistan metrological ', 'System Engineer', 'August 2019 ', 'September 2019'),
(2, 'WebXzone', 'build different web pages', 'Web Developer', 'Feb 2019', 'April 2019'),
(4, 'j2knolgies', 'aa', 'Software Engineer ', 'Feb 2019', 'April 2019');

-- --------------------------------------------------------

--
-- Table structure for table `fiverlinks`
--

CREATE TABLE `fiverlinks` (
  `sno` int(50) NOT NULL,
  `heading` varchar(300) NOT NULL,
  `points` varchar(300) NOT NULL,
  `links` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fiverlinks`
--

INSERT INTO `fiverlinks` (`sno`, `heading`, `points`, `links`) VALUES
(1, 'I will be your django,flask, python full stack developer', 'Unique themes for your website. Designing manageable code base with advanced design pattern techniques. UI animation effects with css and JavaScript. Customized UI Elements. Document properly your project.', 'https://www.fiverr.com/share/7Yek8a'),
(2, 'I will build responsive wordpress website design', ' If You want for a high quality Design Wordpress website for increase your business and selling online products then wants to check the right gigs and design Wordpress website...We create a hand coding user friendly a responsive design... And we will try to help you from start to end...', 'https://www.fiverr.com/share/5rzkLv'),
(3, 'I will custom python scripts for you', 'Projects will be created on Python 3.6 by default (can change on request) All code will follow standards and be built efficiently and effectively with future-proofing in mind. All code will be well documented so that you can continue your work without any hiccups.', 'https://www.fiverr.com/share/xX8Kkl');

-- --------------------------------------------------------

--
-- Table structure for table `myservice`
--

CREATE TABLE `myservice` (
  `sno` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `content` text NOT NULL,
  `image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myservice`
--

INSERT INTO `myservice` (`sno`, `title`, `content`, `image`) VALUES
(1, 'CEO XYZ Inc.', '“Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.”', '7.jpg'),
(2, 'CEO XYZ Inc.', '“Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.”', '8.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `skills`
--

CREATE TABLE `skills` (
  `s_name` varchar(50) NOT NULL,
  `s_expertise` text NOT NULL,
  `sno` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `skills`
--

INSERT INTO `skills` (`s_name`, `s_expertise`, `sno`) VALUES
('Javascript', '92', 1),
('C++', '100', 4),
('Python', '100', 5),
('Bootstrap', '95', 6),
('Django Python Framework', '99', 7),
('Flask Python Framework', '100', 8),
('Digital Marketing', '91', 9),
('Search Engine Optimization', '90', 10),
('wordpress', '98', 11),
('shopify', '79', 12),
('Kotlin', '79', 13);

-- --------------------------------------------------------

--
-- Table structure for table `worked`
--

CREATE TABLE `worked` (
  `sno` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `content` varchar(100) NOT NULL,
  `image` varchar(50) NOT NULL,
  `css_class` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `worked`
--

INSERT INTO `worked` (`sno`, `title`, `content`, `image`, `css_class`) VALUES
(1, 'Bloging Website', 'Bloging website', '2.jpg', 'bwebsite'),
(2, 'Ecommerce Website', 'Ecommerce Website', '2.jpg', 'ewebsite'),
(6, 'Python Website', 'Photography website Front page', '1.jpg', 'python_website');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `client_review`
--
ALTER TABLE `client_review`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `education`
--
ALTER TABLE `education`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `experince`
--
ALTER TABLE `experince`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `fiverlinks`
--
ALTER TABLE `fiverlinks`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `myservice`
--
ALTER TABLE `myservice`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `skills`
--
ALTER TABLE `skills`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `worked`
--
ALTER TABLE `worked`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `client_review`
--
ALTER TABLE `client_review`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `education`
--
ALTER TABLE `education`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `experince`
--
ALTER TABLE `experince`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `fiverlinks`
--
ALTER TABLE `fiverlinks`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `myservice`
--
ALTER TABLE `myservice`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `skills`
--
ALTER TABLE `skills`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `worked`
--
ALTER TABLE `worked`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
