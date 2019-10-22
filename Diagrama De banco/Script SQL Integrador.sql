-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema integrador
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema integrador
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `integrador` DEFAULT CHARACTER SET utf8 ;
USE `integrador` ;

-- -----------------------------------------------------
-- Table `integrador`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `integrador`.`Users` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(250) NOT NULL,
  `UserName` VARCHAR(250) NOT NULL,
  `Password` VARCHAR(250) NOT NULL,
  `Tipo` BIGINT(15) NOT NULL,
  `Email` VARCHAR(250) NOT NULL,
  `Phone` VARCHAR(15) NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `integrador`.`Post`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `integrador`.`Post` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Titulo` VARCHAR(100) NOT NULL,
  `Conteudo` VARCHAR(250) NULL,
  `DataInicial` DATETIME NULL,
  `DataFinal` DATETIME NULL,
  `Tipo` INT NULL,
  `InsertDate` DATETIME NULL,
  `Users_Id` INT NOT NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_Post_Users_idx` (`Users_Id` ASC) VISIBLE,
  CONSTRAINT `fk_Post_Users`
    FOREIGN KEY (`Users_Id`)
    REFERENCES `integrador`.`Users` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `integrador`.`Imagens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `integrador`.`Imagens` (
  `Id` INT NOT NULL,
  `Image` LONGTEXT NOT NULL,
  `InsertDate` DATETIME NOT NULL,
  `Post_Id` INT NOT NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_Imagens_Post1_idx` (`Post_Id` ASC) VISIBLE,
  CONSTRAINT `fk_Imagens_Post1`
    FOREIGN KEY (`Post_Id`)
    REFERENCES `integrador`.`Post` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
