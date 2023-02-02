-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: facial_recog
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `user_log`
--

DROP TABLE IF EXISTS `user_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_log` (
  `userid` int NOT NULL AUTO_INCREMENT,
  `captured_date` datetime DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `photo_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_log`
--

LOCK TABLES `user_log` WRITE;
/*!40000 ALTER TABLE `user_log` DISABLE KEYS */;
INSERT INTO `user_log` VALUES (1,'2023-01-29 21:24:48','Unknown','recognized\\Unknown_2023-01-29_21_24_47.682430.jpg'),(2,'2023-01-29 21:26:48','Adnan Sulaiman','recognized\\Adnan Sulaiman_2023-01-29_21_26_48.068266.jpg'),(3,'2023-01-30 11:20:10','Unknown','recognized\\Unknown_2023-01-30_11_20_09.900376.jpg'),(4,'2023-01-30 11:21:53','Adnan Sulaiman','recognized\\Adnan Sulaiman_2023-01-30_11_21_53.324194.jpg'),(5,'2023-01-30 11:22:23','Adnan Sulaiman','recognized\\Adnan Sulaiman_2023-01-30_11_22_23.220135.jpg'),(6,'2023-01-30 17:37:14','Adnan Sulaiman','recognized\\Adnan Sulaiman_2023-01-30_17_37_13.833035.jpg'),(7,'2023-01-30 17:37:51','Unknown','recognized\\Unknown_2023-01-30_17_37_51.245923.jpg'),(8,'2023-01-30 17:38:42','Unknown','recognized\\Unknown_2023-01-30_17_38_42.075544.jpg'),(9,'2023-01-30 17:40:05','Waqqas','recognized\\Waqqas_2023-01-30_17_40_05.353488.jpg'),(10,'2023-01-30 17:41:02','Waqqas','recognized\\Waqqas_2023-01-30_17_41_01.544214.jpg');
/*!40000 ALTER TABLE `user_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'facial_recog'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-02 22:23:01
