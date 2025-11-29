-- MySQL dump 10.13  Distrib 8.4.7, for Win64 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.4.7

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'testaga','test@test.com','test',1,'2025-11-12 03:39:11'),(2,'role1','role1@test.com','role1',10,'2025-11-12 03:44:59'),(3,'role2','role2@test.com','role2',100,'2025-11-12 03:44:59'),(4,'role3','role3@test.com','role3',1000,'2025-11-12 03:44:59'),(5,'role4','role4@test.com','role4',10000,'2025-11-12 03:44:59'),(7,'newplayer','new@test.com','newp',0,'2025-11-21 13:08:26'),(8,'更菜的','vege@test.com','vege',0,'2025-11-22 02:28:19');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` int NOT NULL AUTO_INCREMENT,
  `member_id` int NOT NULL,
  `content` text NOT NULL,
  `like_count` int NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'Hello world',100,'2025-11-13 17:19:01'),(2,2,'Heyyy',30,'2025-11-13 17:19:01'),(3,3,'What\'s up',5,'2025-11-13 17:19:01'),(4,4,'Yoooooooooo',3,'2025-11-13 17:19:01'),(5,5,'Ohayou',10,'2025-11-13 17:19:01'),(6,1,'I\'m test2',20,'2025-11-13 17:19:01'),(7,2,'How are you doing',70,'2025-11-13 17:19:01'),(8,3,'Man---',15,'2025-11-13 17:19:01'),(9,4,'Don\'t watch an anime called Boku',87,'2025-11-13 17:19:01'),(10,5,'Genki?',190,'2025-11-13 17:19:01'),(12,2,'11:30 right now',0,'2025-11-18 23:37:15'),(16,7,'嗨嗨 我是新來的',0,'2025-11-21 13:10:14'),(17,7,'呀呼!!!!!!!!!!!!!!!!!!!!!!',0,'2025-11-21 13:10:43'),(18,1,'week6任務完成!!',0,'2025-11-21 13:11:23'),(19,7,'不要刪我留言QQ',0,'2025-11-21 13:12:00'),(20,8,'我偏要來刪看看',0,'2025-11-22 02:29:17'),(21,8,'刪不掉 可惡',0,'2025-11-22 02:29:34'),(22,8,'那我來刪自己的看看',0,'2025-11-22 02:29:43'),(24,8,'哇啊啊 成功刪掉了',0,'2025-11-22 02:30:25');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `query_record`
--

DROP TABLE IF EXISTS `query_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `query_record` (
  `id` int NOT NULL AUTO_INCREMENT,
  `searcher_id` int NOT NULL,
  `target_id` int NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `searcher_id` (`searcher_id`),
  KEY `target_id` (`target_id`),
  CONSTRAINT `query_record_ibfk_1` FOREIGN KEY (`searcher_id`) REFERENCES `member` (`id`),
  CONSTRAINT `query_record_ibfk_2` FOREIGN KEY (`target_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `query_record`
--

LOCK TABLES `query_record` WRITE;
/*!40000 ALTER TABLE `query_record` DISABLE KEYS */;
INSERT INTO `query_record` VALUES (1,7,3,'2025-11-29 19:04:29'),(2,7,1,'2025-11-29 19:04:33'),(3,1,8,'2025-11-29 19:06:18'),(4,1,8,'2025-11-29 19:06:32'),(5,1,5,'2025-11-29 19:06:36'),(6,8,5,'2025-11-29 19:06:59'),(7,8,3,'2025-11-29 19:07:19'),(8,8,2,'2025-11-29 19:07:23'),(9,7,3,'2025-11-29 20:59:26'),(10,7,2,'2025-11-29 20:59:30'),(11,7,1,'2025-11-29 20:59:34'),(12,7,8,'2025-11-29 20:59:56'),(13,4,8,'2025-11-29 23:58:47'),(14,8,3,'2025-11-29 23:59:13'),(15,8,4,'2025-11-29 23:59:16'),(16,3,2,'2025-11-30 00:00:28');
/*!40000 ALTER TABLE `query_record` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-30  0:14:45
