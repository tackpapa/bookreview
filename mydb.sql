-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) DEFAULT NULL,
  `author` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (14,'first book','kiyoung tack','2016-05-13 23:08:10','2016-05-13 23:08:10'),(15,'secondbook','lalalsdkfj','2016-05-14 00:18:29','2016-05-14 00:18:29'),(16,'Harrypotter and deathly hollows','lalal','2016-05-14 00:18:53','2016-05-14 00:18:53'),(17,'divergetn','sucks','2016-05-14 00:20:46','2016-05-14 00:20:46'),(18,'codingdojoinc','dunno','2016-05-14 00:33:47','2016-05-14 00:33:47'),(19,'dojosux','me','2016-05-14 01:28:59','2016-05-14 01:28:59'),(20,'reviewdeletetest','can i?','2016-05-14 01:39:24','2016-05-14 01:39:24'),(21,'deletekjtelkj','lkjas;dkflj','2016-05-14 01:58:11','2016-05-14 01:58:11');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `review` varchar(45) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `book_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_reviews_users1_idx` (`user_id`,`id`,`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (7,'first review',5,'2016-05-13 23:08:10','2016-05-13 23:08:10',1,14),(10,'askjfkljal;fkds',1,'2016-05-13 23:30:56','2016-05-13 23:30:56',1,0),(11,'234234234',1,'2016-05-13 23:35:23','2016-05-13 23:35:23',1,14),(12,'whats up',5,'2016-05-13 23:49:38','2016-05-13 23:49:38',1,14),(13,'asdklfj;af',4,'2016-05-14 00:18:29','2016-05-14 00:18:29',1,15),(14,'kasjfkljasfklj;sldf',1,'2016-05-14 00:18:53','2016-05-14 00:18:53',1,16),(15,'skldjf;lkaj;klfj',1,'2016-05-14 00:20:46','2016-05-14 00:20:46',1,17),(16,'hmmmm',4,'2016-05-14 00:33:47','2016-05-14 00:33:47',2,18),(17,'im not sure',1,'2016-05-14 00:33:55','2016-05-14 00:33:55',2,18),(18,'hmmmmmmmmm',5,'2016-05-14 01:28:59','2016-05-14 01:28:59',3,19),(19,'i forgot to say something',3,'2016-05-14 01:29:12','2016-05-14 01:29:12',3,19),(20,'ok me 2',1,'2016-05-14 01:29:52','2016-05-14 01:29:52',1,19);
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `alias` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `pw` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'kiyoung','tackpapa','caca@ca.com','$2b$12$kcjr6Dr6hQ1G758UY703A.Rg9Aj4wOdygcXqxi91F3ZJA6DjTN02G','2016-05-13 21:11:53','2016-05-13 21:11:53'),(2,'kyle','jjang','coco@co.com','$2b$12$eGb4cn5bF6Guwa2xGul7VO02s.6pAtdkzuNetEjOLlLWZEJmmfIIi','2016-05-14 00:24:53','2016-05-14 00:24:53'),(3,'ben','benrox','benrox@ben.com','$2b$12$DFVipX34cksTkPn8q1sAF.dWmXdemv20tE.CsDC7BtXOoQKcTwtF.','2016-05-14 01:28:29','2016-05-14 01:28:29');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-14  2:30:14
