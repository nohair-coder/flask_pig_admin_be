-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- 主机： localhost:8889
-- 生成日期： 2019-03-19 02:20:43
-- 服务器版本： 5.7.23
-- PHP 版本： 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- 数据库： `pig`
--

-- --------------------------------------------------------

--
-- 表的结构 `notification_contact`
--

CREATE TABLE `notification_contact` (
  `id` int(10) UNSIGNED NOT NULL,
  `email` varchar(100) NOT NULL,
  `comment` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='测定站故障通知联系方式表';

--
-- 转存表中的数据 `notification_contact`
--

INSERT INTO `notification_contact` (`id`, `email`, `comment`) VALUES
(1, 'liu3248184446@outlook.com', '刘星'),
(4, 'lxfriday@126.com', '刘星');

-- --------------------------------------------------------

--
-- 表的结构 `notification_record`
--

CREATE TABLE `notification_record` (
  `id` int(10) UNSIGNED NOT NULL,
  `email` varchar(100) NOT NULL,
  `message` varchar(255) NOT NULL,
  `created_time` int(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='故障通知记录表';

--
-- 转存表中的数据 `notification_record`
--

INSERT INTO `notification_record` (`id`, `email`, `message`, `created_time`) VALUES
(1, 'all', '测定站<b><font color=red>停机</font></b><br>', 1544605449),
(2, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>xxxdddeeeccc</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1544605644),
(3, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>xxxdddeeeccc</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1544614147),
(4, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>xxxdddeeeccc</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1544614809),
(5, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>xxxdddeeeddd</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1544616189),
(6, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>xxxdddeeeddd</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1544617249),
(7, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>xxxdddeeeddd</font><br>错误码：<font color=red>00002</font><br><b>请尽快检查并排除故障</b>', 1544617291),
(8, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>xxxdddeeedde</font><br>错误码：<font color=red>00002</font><br><b>请尽快检查并排除故障</b>', 1544617442),
(9, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>xxxdddeeedbf</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1544617779),
(10, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>oooooooooooo</font><br>错误码：<font color=red>02222</font><br><b>请尽快检查并排除故障</b>', 1544617847),
(11, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117375),
(12, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117381),
(13, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117387),
(14, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117393),
(15, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117399),
(16, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117405),
(17, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117411),
(18, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117417),
(19, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117423),
(20, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117429),
(21, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117435),
(22, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117441),
(23, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117447),
(24, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117453),
(25, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117459),
(26, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117465),
(27, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117471),
(28, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117477),
(29, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117483),
(30, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117489),
(31, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117495),
(32, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117499),
(33, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117505),
(34, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117511),
(35, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117517),
(36, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117523),
(37, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117529),
(38, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117535),
(39, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117541),
(40, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117547),
(41, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117553),
(42, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117559),
(43, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117565),
(44, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117571),
(45, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117577),
(46, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117583),
(47, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117589),
(48, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117595),
(49, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117601),
(50, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117607),
(51, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117613),
(52, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117619),
(53, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117625),
(54, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117631),
(55, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117637),
(56, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117643),
(57, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117649),
(58, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117655),
(59, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117661),
(60, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117667),
(61, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117673),
(62, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117679),
(63, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117685),
(64, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117691),
(65, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117697),
(66, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117703),
(67, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117714),
(68, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117720),
(69, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117732),
(70, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117744),
(71, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117750),
(72, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117756),
(73, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117762),
(74, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117792),
(75, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117804),
(76, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117816),
(77, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117822),
(78, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117834),
(79, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117840),
(80, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117846),
(81, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117852),
(82, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545117901),
(83, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545117907),
(84, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545118024),
(85, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545118039),
(86, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545118054),
(87, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545118069),
(88, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545118099),
(89, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545118114),
(90, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545118129),
(91, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545118540),
(92, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545138069),
(93, 'all', '测定站出现<b><font color=red>故障</font></b><br> 测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00001</font><br><b>请尽快检查并排除故障</b>', 1545217339),
(94, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545217354),
(95, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545224696),
(96, 'all', '测定站<b><font color=red>停机</font></b><br>测定站id：<font color=red>000000012345</font><br>错误码：<font color=red>00000</font><br><b>请尽快检查并排除故障</b>', 1545225413);

-- --------------------------------------------------------

--
-- 表的结构 `pig_base`
--

CREATE TABLE `pig_base` (
  `id` int(10) UNSIGNED NOT NULL,
  `pid` int(10) NOT NULL COMMENT '种猪id',
  `food_intake` float NOT NULL DEFAULT '0' COMMENT '采食量',
  `weight` float NOT NULL DEFAULT '0' COMMENT '体重',
  `body_long` float NOT NULL DEFAULT '0' COMMENT '体长',
  `body_width` float NOT NULL DEFAULT '0' COMMENT '体宽',
  `body_height` float NOT NULL DEFAULT '0' COMMENT '体高',
  `body_temp` float NOT NULL DEFAULT '0' COMMENT '体温',
  `env_temp` float NOT NULL DEFAULT '0' COMMENT '环境温度',
  `env_humi` float NOT NULL DEFAULT '0' COMMENT '环境湿度',
  `start_time` int(10) NOT NULL DEFAULT '0' COMMENT '开始采食时间',
  `end_time` int(10) DEFAULT '0' COMMENT '结束进食时间',
  `sys_time` int(10) DEFAULT '0' COMMENT '服务器本地时间'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='种猪信息表';

--
-- 转存表中的数据 `pig_base`
--

INSERT INTO `pig_base` (`id`, `pid`, `food_intake`, `weight`, `body_long`, `body_width`, `body_height`, `body_temp`, `env_temp`, `env_humi`, `start_time`, `end_time`, `sys_time`) VALUES
(380, 1, 200.22, 180.11, 120.33, 30.22, 50.44, 0, 0, 0, 1552017439, 1552017448, 1552017907),
(381, 1, 200.22, 180.11, 120.33, 30.22, 50.44, 0, 0, 0, 1552017439, 1552017448, 1552032117),
(382, 1, 200.22, 180.11, 120.33, 30.22, 50.44, 0, 0, 0, 1552017439, 1552017448, 1552032288),
(383, 1, 200.22, 180.11, 120.33, 30.22, 50.44, 0, 0, 0, 1552017439, 1552017448, 1552032321),
(384, 3, 200.22, 180.11, 120.33, 30.22, 50.44, 0, 0, 0, 1552017439, 1552017448, 1552033969),
(385, 3, 200.22, 180.11, 120.33, 30.22, 50.44, 0, 0, 0, 1552017439, 1552017448, 1552034367),
(386, 4, 200.22, 180.11, 120.33, 30.22, 50.44, 0, 0, 0, 1552017439, 1552017448, 1552192098),
(387, 5, 200.22, 180.11, 120.33, 30.22, 50.44, 0, 0, 0, 1552017439, 1552017448, 1552192133),
(388, 6, 200.22, 180.11, 120.33, 30.22, 50.44, 0, 0, 0, 1552017439, 1552017448, 1552034634),
(389, 6, 200.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552045627),
(390, 6, 200.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552124986),
(391, 7, 200.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552125014),
(392, 4, 200.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552194384),
(393, 7, 200.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552194451),
(394, 7, 200.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552194465),
(395, 7, 200.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552195282),
(396, 7, 200.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552204989),
(397, 7, 200.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552205018),
(398, 7, 200.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552205610),
(399, 7, 200.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552205693),
(400, 7, 200.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552292234),
(401, 7, 200.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552481977),
(402, 7, 202.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552482587),
(403, 7, 202.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552482721),
(404, 7, 202.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552482865),
(405, 7, 202.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552483013),
(406, 7, 202.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552483569),
(407, 7, 202.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552483597),
(408, 7, 202.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552483647),
(409, 7, 7.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552483674),
(410, 7, 7.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552483730),
(411, 7, 7.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552483808),
(412, 7, 7.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552483824),
(413, 7, 7.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552483842),
(414, 7, 7.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552483884),
(415, 8, 7.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552483913),
(416, 8, 7.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552483950),
(417, 8, 7.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552533833),
(418, 8, 7.22, 180.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552534461),
(419, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552534477),
(420, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552534599),
(421, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552534610),
(422, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552534938),
(423, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552534972),
(424, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552535484),
(425, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552535486),
(426, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552535489),
(427, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552535490),
(428, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552535491),
(429, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552535491),
(430, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552535492),
(431, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552536181),
(432, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552536184),
(433, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552536199),
(434, 8, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552536402),
(435, 9, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552536422),
(436, 9, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552536482),
(437, 10, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552536501),
(438, 11, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552536569),
(439, 11, 7.22, 182.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552536575),
(440, 11, 7.22, 181.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552536579),
(441, 11, 7.22, 181.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552536595),
(442, 11, 7.22, 181.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552536603),
(443, 11, 7.22, 181.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552785677),
(444, 11, 7.22, 181.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552785680),
(445, 11, 7.22, 181.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552785683),
(446, 11, 7.22, 181.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552785685),
(447, 11, 7.22, 181.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552785717),
(448, 11, 7.22, 181.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552785772),
(449, 12, 7.22, 181.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552785814),
(450, 12, 7.22, 181.11, 120.33, 30.22, 50.44, 1, 2, 3, 1552017439, 1552017448, 1552959038);

-- --------------------------------------------------------

--
-- 表的结构 `pig_daily_assess`
--

CREATE TABLE `pig_daily_assess` (
  `id` int(10) UNSIGNED NOT NULL,
  `pid` int(10) NOT NULL COMMENT '种猪id',
  `food_intake_count` smallint(6) NOT NULL COMMENT '单日进食次数',
  `food_intake_total` float(6,2) NOT NULL COMMENT '单日进食量（料重）',
  `weight_ave` float(6,2) NOT NULL COMMENT '单日猪体重均值',
  `prev_weight_compare` float(6,2) NOT NULL COMMENT '体重相比前一天的变化值（这天-前一天），正值表示增加，负值表示降低',
  `prev_foodintake_compare` float(6,2) NOT NULL COMMENT '采食量相比前一天的变化值（这天-前一天），正值表示增加，负值表示降低',
  `record_date` date NOT NULL COMMENT '时间（记录的哪一天的）'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='种猪一日信息表';

--
-- 转存表中的数据 `pig_daily_assess`
--

INSERT INTO `pig_daily_assess` (`id`, `pid`, `food_intake_count`, `food_intake_total`, `weight_ave`, `prev_weight_compare`, `prev_foodintake_compare`, `record_date`) VALUES
(1, 1, 6, 7.88, 120.22, 0.80, 1.00, '2019-03-12'),
(2, 4, 6, 8.55, 124.35, 0.90, 1.00, '2019-03-12'),
(3, 4, 5, 7.55, 123.45, 0.60, 1.10, '2019-03-11'),
(4, 4, 7, 6.45, 122.85, 0.00, 0.00, '2019-03-10'),
(5, 1, 5, 6.88, 119.42, 0.00, 0.00, '2019-03-11'),
(6, 1, 7, 7.98, 121.22, 1.00, 0.10, '2019-03-13'),
(7, 7, 5, 7.22, 180.11, 0.00, 0.00, '2019-03-13'),
(8, 8, 2, 14.44, 180.11, 0.00, 0.00, '2019-03-13'),
(9, 8, 17, 122.74, 181.87, 1.76, 108.30, '2019-03-14'),
(10, 9, 2, 14.44, 182.11, 0.00, 0.00, '2019-03-14'),
(11, 10, 1, 7.22, 182.11, 0.00, 0.00, '2019-03-14'),
(12, 11, 5, 36.10, 181.51, 0.00, 0.00, '2019-03-14'),
(13, 11, 6, 43.32, 181.11, -0.40, 7.22, '2019-03-17'),
(14, 12, 1, 7.22, 181.11, 0.00, 0.00, '2019-03-17'),
(15, 12, 1, 7.22, 181.11, 0.00, 0.00, '2019-03-19');

-- --------------------------------------------------------

--
-- 表的结构 `pig_daily_first_intake`
--

CREATE TABLE `pig_daily_first_intake` (
  `id` int(10) UNSIGNED NOT NULL,
  `pid` int(10) NOT NULL COMMENT '种猪id, 对应到 pig_list 的id',
  `pigbase_id` int(10) NOT NULL COMMENT 'pig_base表 中对应的记录的id',
  `record_date` date NOT NULL COMMENT 'YYYYmmdd'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='种猪每天的首次进食信息记录';

--
-- 转存表中的数据 `pig_daily_first_intake`
--

INSERT INTO `pig_daily_first_intake` (`id`, `pid`, `pigbase_id`, `record_date`) VALUES
(1, 5, 387, '2019-03-10'),
(2, 4, 386, '2019-03-10'),
(3, 7, 393, '2019-03-10'),
(4, 7, 400, '2019-03-11'),
(5, 7, 401, '2019-03-13'),
(6, 8, 415, '2019-03-13'),
(7, 8, 417, '2019-03-14'),
(8, 9, 435, '2019-03-14'),
(9, 10, 437, '2019-03-14'),
(10, 11, 438, '2019-03-14'),
(11, 11, 443, '2019-03-17'),
(12, 12, 449, '2019-03-17'),
(13, 12, 450, '2019-03-19');

-- --------------------------------------------------------

--
-- 表的结构 `pig_list`
--

CREATE TABLE `pig_list` (
  `id` int(10) UNSIGNED NOT NULL,
  `facnum` char(4) NOT NULL COMMENT '猪场代码',
  `animalnum` char(12) NOT NULL COMMENT '种猪号（对种猪的自定义代指）',
  `earid` char(12) NOT NULL COMMENT '耳标号 id',
  `stationid` char(12) NOT NULL COMMENT '测定站 id',
  `entry_time` int(10) NOT NULL DEFAULT '0' COMMENT '入栏时间',
  `exit_time` int(10) DEFAULT NULL COMMENT '出栏时间'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='种猪信息表';

--
-- 转存表中的数据 `pig_list`
--

INSERT INTO `pig_list` (`id`, `facnum`, `animalnum`, `earid`, `stationid`, `entry_time`, `exit_time`) VALUES
(1, 'icbc', '00000001254s', '00000001254s', '000000012545', 1551856710, NULL),
(2, '', '', '0000ss01254s', 's00000012545', 1552033796, NULL),
(3, '', '', '0000sa01254s', 'xxxdddeeedbn', 1552033886, NULL),
(4, '', '', 'sss0sa01254s', 'xxxdddeeedbn', 1552034506, NULL),
(5, '', '', 'wss0sa01254s', 'xxxdddeeedbn', 1552034595, NULL),
(6, '', '', 'wss0sa012547', 'xxxdddeeedbn', 1552034634, NULL),
(7, '', '', 'wss0sav12547', 'xxxdddeeedbn', 1552125014, NULL),
(8, '', '', 'xxx0sav12547', 'xxxdddeeedbn', 1552483913, NULL),
(9, '', '', 'xxx0sav1ss47', 'xxxdddeeedbn', 1552536422, NULL),
(10, '', '', 'xxx0sav1sscs', 'xxxdddeeedbn', 1552536501, NULL),
(11, '', '', 'xxxssav1sscs', 'xaxaaaeeedbn', 1552536569, NULL),
(12, '', '', 'xxxssav2sscs', 'xaxaaaeeedbn', 1552785814, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `station_errorcode_reference`
--

CREATE TABLE `station_errorcode_reference` (
  `id` int(10) UNSIGNED NOT NULL,
  `errorcode` char(5) NOT NULL,
  `comment` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='测定站故障错误码参照表';

--
-- 转存表中的数据 `station_errorcode_reference`
--

INSERT INTO `station_errorcode_reference` (`id`, `errorcode`, `comment`) VALUES
(1, '00000', '机器正常运行或者已停机'),
(3, '00002', '部件2故障'),
(5, '00005', '部件5故障'),
(7, '00004', '部件4故障'),
(8, '00003', '部件3故障'),
(9, '00006', '部件6故障'),
(10, '00008', '部件8故障'),
(14, '00009', '部件9故障'),
(15, '00010', '部件10故障'),
(17, '00011', 'dsadsa');

-- --------------------------------------------------------

--
-- 表的结构 `station_info`
--

CREATE TABLE `station_info` (
  `id` int(10) UNSIGNED NOT NULL,
  `stationid` char(12) NOT NULL,
  `comment` varchar(50) DEFAULT '' COMMENT '测定站备注',
  `status` enum('on','off') NOT NULL COMMENT '测定站机器的运行状态（''on'', ''off''）',
  `changetime` int(10) NOT NULL DEFAULT '0',
  `errorcode` char(5) NOT NULL DEFAULT '00000' COMMENT '故障编号（代表不同的机器的故障状态）'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='测定站机器运行状况表';

--
-- 转存表中的数据 `station_info`
--

INSERT INTO `station_info` (`id`, `stationid`, `comment`, `status`, `changetime`, `errorcode`) VALUES
(1, 'qwertyuiopas', NULL, 'on', 1544414826, '12345'),
(33, 'xxxdddeeeccc', NULL, 'off', 1544414826, '00000'),
(40, 'xxxdddeeeddd', NULL, 'on', 1544617291, '00002'),
(41, 'xxxdddeeedde', NULL, 'on', 1544617577, '00000'),
(42, 'xxxdddeeedef', NULL, 'on', 1544617588, '00000'),
(43, 'xxxdddeeedeg', NULL, 'on', 1544617593, '00000'),
(44, 'xxxdddeeedeh', NULL, 'on', 1544617598, '00000'),
(45, 'xxxdddeeedei', NULL, 'on', 1544617602, '00000'),
(46, 'xxxdddeeedej', NULL, 'on', 1544617605, '00000'),
(47, 'xxxdddeeedek', NULL, 'on', 1544617610, '00000'),
(48, 'xxxdddeeedel', NULL, 'on', 1544617644, '00000'),
(49, 'xxxdddeeedem', NULL, 'on', 1544617657, '00000'),
(50, 'xxxdddeeeden', NULL, 'on', 1544617661, '00000'),
(51, 'xxxdddeeedeo', NULL, 'on', 1544617664, '00000'),
(52, 'xxxdddeeedep', NULL, 'on', 1544617668, '00000'),
(53, 'xxxdddeeeder', NULL, 'on', 1544617671, '00000'),
(54, 'xxxdddeeedes', NULL, 'on', 1544617674, '00000'),
(55, 'xxxdddeeedet', NULL, 'on', 1544617677, '00000'),
(56, 'xxxdddeeedeu', NULL, 'on', 1544617680, '00000'),
(57, 'xxxdddeeedev', NULL, 'on', 1544617684, '00000'),
(58, 'xxxdddeeedew', NULL, 'on', 1544617688, '00000'),
(59, 'xxxdddeeedex', NULL, 'on', 1544617691, '00000'),
(60, 'xxxdddeeedey', NULL, 'on', 1544617694, '00000'),
(61, 'xxxdddeeedez', NULL, 'on', 1544617697, '00000'),
(62, 'xxxdddeeedaa', NULL, 'on', 1544617702, '00000'),
(63, 'xxxdddeeedbb', NULL, 'on', 1544617759, '00000'),
(64, 'xxxdddeeedbc', NULL, 'on', 1544617764, '00000'),
(65, 'xxxdddeeedbd', NULL, 'on', 1544617767, '00000'),
(66, 'xxxdddeeedbe', NULL, 'on', 1544617770, '00000'),
(67, 'xxxdddeeedbf', NULL, 'off', 1544617778, '00000'),
(68, 'xxxdddeeedbg', NULL, 'on', 1544617787, '00000'),
(69, 'xxxdddeeedbh', NULL, 'on', 1544617791, '00000'),
(70, 'xxxdddeeedbi', NULL, 'on', 1544617794, '00000'),
(71, 'xxxdddeeedbj', NULL, 'on', 1544617798, '00000'),
(72, 'xxxdddeeedbk', NULL, 'on', 1544617802, '00000'),
(73, 'xxxdddeeedbl', NULL, 'on', 1544617806, '00000'),
(74, 'xxxdddeeedbm', NULL, 'on', 1544617809, '00000'),
(75, 'xxxdddeeedbn', NULL, 'on', 1544617813, '00000'),
(76, 'oooooooooooo', 'oooooooooooo', 'on', 1551774736, '02222'),
(77, '000000012345', '备注2', 'off', 1551770947, '00000'),
(83, '000000012545', '备注aaa', 'on', 1551774414, '00000'),
(85, 's00000012545', '测定站号自动生成，生成时间 2019年03月08日-08:05:21', 'on', 1552032321, '00000'),
(86, 'xaxaaaeeedbn', '测定站号自动生成，生成时间 2019年03月17日 -- 09:22:52', 'on', 1552785772, '00000');

-- --------------------------------------------------------

--
-- 表的结构 `station_timer`
--

CREATE TABLE `station_timer` (
  `id` int(10) UNSIGNED NOT NULL,
  `stationid` char(12) NOT NULL COMMENT '测定站 id',
  `type` enum('on','off') NOT NULL COMMENT 'on 开启机器的指令',
  `exe_time` int(10) NOT NULL COMMENT '指令执行时间',
  `created_time` int(10) NOT NULL COMMENT '记录创建时间'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='测定站启停定时表';

-- --------------------------------------------------------

--
-- 表的结构 `syscfg`
--

CREATE TABLE `syscfg` (
  `name` varchar(50) NOT NULL COMMENT '配置名',
  `comment` varchar(50) NOT NULL COMMENT '备注',
  `value` varchar(200) NOT NULL COMMENT '配置的值',
  `created_time` int(10) NOT NULL DEFAULT '0' COMMENT '记录创建时间'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='系统配置表';

--
-- 转存表中的数据 `syscfg`
--

INSERT INTO `syscfg` (`name`, `comment`, `value`, `created_time`) VALUES
('FAC_NUM', '系统设置-猪场代码', 'icbc', 0),
('PIG_BASE_DATA_ALLOWED_FIELDS', '基础数据页面允许选择显示的所有字段', 'earid,animalnum,stationid,food_intake,weight,body_long,body_width,body_height,body_temp,env_temp,env_humi,start_time,end_time,sys_time', 0),
('PIG_BASE_DATA_FIELDS', '基础数据页面允许显示的字段', 'earid,stationid,facnum', 0),
('SHOW_SELECT_LANGUAGE', '系统设置-显示选择语言', 'false', 0),
('SHOW_TIME_SYNC', '系统设置-显示时间同步区域', 'false', 0),
('PIG_DAILY_INTAKE_START_TIME', '日采食开始计算的时间，测定站第二日首次采食数据统计，四位数字（2位小时2位分钟）（0800 点整）', '0800', 0),
('PIG_DAILY_ASSESS_LAST_TWO_DATE', 'pig_daily_assess 表更新截止的最近的两个日期，大的日期在后面，小的日期在前面', '20190309,20190310', 0);

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `id` int(10) UNSIGNED NOT NULL,
  `username` varchar(50) NOT NULL COMMENT '昵称',
  `password` char(64) NOT NULL COMMENT '哈希密码',
  `token` char(64) NOT NULL COMMENT '64位哈希字符串token',
  `phone` char(11) NOT NULL COMMENT '手机号',
  `email` varchar(100) NOT NULL COMMENT '邮箱',
  `rank` enum('super','common') NOT NULL DEFAULT 'common' COMMENT '用户级别(super、common)，高级别用户可以控制设置页面的 基础数据显示列',
  `created_time` int(10) NOT NULL DEFAULT '0' COMMENT '该用户创建时间',
  `last_login_time` int(10) NOT NULL DEFAULT '0' COMMENT '最近一次的登录时间'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='系统用户表';

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `token`, `phone`, `email`, `rank`, `created_time`, `last_login_time`) VALUES
(1, 'lxfriday', '9a6f6b5aa85c259f683441ed17e1862558e88e33ddd17ec12d5b75cad733d9a4', 'daskdnasbjfkabdfjksdbfkjbdkf', '18627825090', 'lxfriday@126.com', 'common', 0, 0),
(2, 'root', '9a6f6b5aa85c259f683441ed17e1862558e88e33ddd17ec12d5b75cad733d9a4', 'nfjdfnjkdsnfldjsbnfljksbdflkjbdsfjbs', '15623401867', '3248184446@qq.com', 'super', 0, 0),
(3, 'lxfriday001', '9a6f6b5aa85c259f683441ed17e1862558e88e33ddd17ec12d5b75cad733d9a4', 'cf9f5d2c50ab6710785528ba97504da4f4e15084fb00bb50b34775fe9dc9f665', '15623401868', 'liu3248184446@outlook.com', 'common', 1551678859, 1551680861),
(4, 'lxfriday002', '0d7890f1bfb827c8f7f45057f5ab32f88f573ade592b16c15c0e29dc7851b2da', '3b44c07dd4a5183241834b76c531130de2704c7897833c96fe0c201bd044bf86', '15623401869', '3248184447@outlook.com', 'common', 1551686197, 1551686197);

-- --------------------------------------------------------

--
-- 表的结构 `user_find_pass`
--

CREATE TABLE `user_find_pass` (
  `id` int(10) UNSIGNED NOT NULL,
  `email` varchar(100) NOT NULL COMMENT '用户邮箱',
  `verifycode` char(128) NOT NULL COMMENT '128位验证字符串',
  `password` char(64) NOT NULL COMMENT '用户输入的哈希密码',
  `created_time` int(10) NOT NULL COMMENT '记录产生时间'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='邮件找回密码的记录表';

--
-- 转储表的索引
--

--
-- 表的索引 `notification_contact`
--
ALTER TABLE `notification_contact`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- 表的索引 `notification_record`
--
ALTER TABLE `notification_record`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `pig_base`
--
ALTER TABLE `pig_base`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `pig_daily_assess`
--
ALTER TABLE `pig_daily_assess`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Uni_pid_date` (`pid`,`record_date`);

--
-- 表的索引 `pig_daily_first_intake`
--
ALTER TABLE `pig_daily_first_intake`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Uni_pid_date` (`pid`,`record_date`);

--
-- 表的索引 `pig_list`
--
ALTER TABLE `pig_list`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `station_errorcode_reference`
--
ALTER TABLE `station_errorcode_reference`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `errorcode` (`errorcode`);

--
-- 表的索引 `station_info`
--
ALTER TABLE `station_info`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `stationid` (`stationid`),
  ADD KEY `stationid_2` (`stationid`);

--
-- 表的索引 `station_timer`
--
ALTER TABLE `station_timer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Uni_stationid` (`stationid`);

--
-- 表的索引 `syscfg`
--
ALTER TABLE `syscfg`
  ADD PRIMARY KEY (`name`);

--
-- 表的索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD UNIQUE KEY `token` (`token`);

--
-- 表的索引 `user_find_pass`
--
ALTER TABLE `user_find_pass`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `verifycode` (`verifycode`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `notification_contact`
--
ALTER TABLE `notification_contact`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- 使用表AUTO_INCREMENT `notification_record`
--
ALTER TABLE `notification_record`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- 使用表AUTO_INCREMENT `pig_base`
--
ALTER TABLE `pig_base`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=451;

--
-- 使用表AUTO_INCREMENT `pig_daily_assess`
--
ALTER TABLE `pig_daily_assess`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- 使用表AUTO_INCREMENT `pig_daily_first_intake`
--
ALTER TABLE `pig_daily_first_intake`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- 使用表AUTO_INCREMENT `pig_list`
--
ALTER TABLE `pig_list`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- 使用表AUTO_INCREMENT `station_errorcode_reference`
--
ALTER TABLE `station_errorcode_reference`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- 使用表AUTO_INCREMENT `station_info`
--
ALTER TABLE `station_info`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87;

--
-- 使用表AUTO_INCREMENT `station_timer`
--
ALTER TABLE `station_timer`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `user`
--
ALTER TABLE `user`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- 使用表AUTO_INCREMENT `user_find_pass`
--
ALTER TABLE `user_find_pass`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
