-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: pastelaria_db
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `tb_comanda_produto`
--

DROP TABLE IF EXISTS `tb_comanda_produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_comanda_produto` (
  `id_comanda_produto` int NOT NULL AUTO_INCREMENT,
  `funcionario_id` int NOT NULL,
  `produto_id` int NOT NULL,
  `comanda_id` int NOT NULL,
  `quantidade` tinyint DEFAULT NULL,
  `valor_unitario` decimal(11,2) DEFAULT NULL,
  PRIMARY KEY (`id_comanda_produto`),
  KEY `FK_tb_comanda__tb_comanda_produto` (`comanda_id`),
  KEY `FK_tb_produto__tb_comanda_produto` (`produto_id`),
  KEY `FK_tb_funcionario__tb_comanda_Produto` (`funcionario_id`),
  CONSTRAINT `FK_tb_comanda__tb_comanda_produto` FOREIGN KEY (`comanda_id`) REFERENCES `tb_comanda` (`id_comanda`),
  CONSTRAINT `FK_tb_funcionario__tb_comanda_Produto` FOREIGN KEY (`funcionario_id`) REFERENCES `tb_funcionario` (`id_funcionario`),
  CONSTRAINT `FK_tb_produto__tb_comanda_produto` FOREIGN KEY (`produto_id`) REFERENCES `tb_produto` (`id_produto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_comanda_produto`
--

LOCK TABLES `tb_comanda_produto` WRITE;
/*!40000 ALTER TABLE `tb_comanda_produto` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_comanda_produto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-29 23:01:07
