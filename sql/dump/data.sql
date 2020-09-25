CREATE DATABASE IF NOT EXISTS `data`;
USE `data`;

DROP TABLE IF EXISTS `text`;
CREATE TABLE `text` (
    `id` int(11) unsigned PRIMARY KEY AUTO_INCREMENT,
    `text` VARCHAR(255)
);
