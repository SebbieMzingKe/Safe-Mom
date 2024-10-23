-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: safe-mom
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `patient_data`
--

DROP TABLE IF EXISTS `patient_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `age` int DEFAULT NULL,
  `height` decimal(5,2) DEFAULT NULL,
  `weight` decimal(5,2) DEFAULT NULL,
  `bmi` decimal(5,2) DEFAULT NULL,
  `sysbp` decimal(5,2) DEFAULT NULL,
  `diabp` decimal(5,2) DEFAULT NULL,
  `hb` decimal(5,2) DEFAULT NULL,
  `pcv` decimal(5,2) DEFAULT NULL,
  `platelet` decimal(10,2) DEFAULT NULL,
  `creatinine` decimal(5,2) DEFAULT NULL,
  `plgf_sflt` decimal(5,2) DEFAULT NULL,
  `SEng` decimal(5,2) DEFAULT NULL,
  `cysC` decimal(5,2) DEFAULT NULL,
  `pp_13` decimal(5,2) DEFAULT NULL,
  `glycerides` decimal(5,2) DEFAULT NULL,
  `htn` tinyint(1) DEFAULT NULL,
  `diabetes` tinyint(1) DEFAULT NULL,
  `fam_htn` tinyint(1) DEFAULT NULL,
  `sp_art` tinyint(1) DEFAULT NULL,
  `occupation` varchar(255) DEFAULT NULL,
  `diet` varchar(255) DEFAULT NULL,
  `activity` varchar(255) DEFAULT NULL,
  `sleep` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `patient_data_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_data`
--

LOCK TABLES `patient_data` WRITE;
/*!40000 ALTER TABLE `patient_data` DISABLE KEYS */;
INSERT INTO `patient_data` VALUES (1,1,1.00,1.00,2.00,2.00,2.00,2.00,1.00,1.00,1.00,NULL,1.00,1.00,11.00,1.00,1,1,1,1,'1','1','1','1','2024-10-20 06:32:03',NULL),(2,1,1.00,1.00,2.00,2.00,2.00,2.00,1.00,1.00,1.00,NULL,1.00,1.00,11.00,1.00,1,1,1,1,'1','1','1','1','2024-10-20 06:36:44',NULL),(3,1,1.00,1.00,2.00,2.00,2.00,2.00,1.00,1.00,1.00,NULL,1.00,1.00,11.00,14.00,1,1,1,18,'1','1','1','114','2024-10-20 06:39:00',NULL),(4,1,1.00,1.00,2.00,2.00,2.00,2.00,1.00,1.00,1.00,NULL,1.00,1.00,11.00,14.00,1,1,1,18,'1','1','1','114','2024-10-20 07:06:44',NULL),(5,12,11.00,1.00,123.00,23.00,2.00,2.00,2.00,23.00,12.00,NULL,34.00,12.00,14.00,54.00,1,1,1,1,'3','4','3','8','2024-10-20 07:47:17',2),(6,12,11.00,1.00,123.00,23.00,2.00,2.00,2.00,23.00,12.00,NULL,34.00,12.00,14.00,54.00,1,1,1,1,'3','4','3','8','2024-10-20 07:48:23',2);
/*!40000 ALTER TABLE `patient_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-23  7:07:00
