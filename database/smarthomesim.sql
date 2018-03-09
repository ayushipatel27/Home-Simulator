--Postgresql database configuration for smart home simulation according to
--https://sqldbm.com/Project/SQLServer/Share/k5p6GyD8GUzYNRrqn160Pg

CREATE DATABASE smarthomesim;

--Drop all tables that will be used
DROP TABLE Appliances;

DROP TABLE Sensors;

DROP TABLE Weather;

DROP TABLE HvacUsage;

DROP TABLE WaterUsage;

DROP TABLE DailyUsage;

DROP TABLE EnergyUsage;

DROP TABLE Rooms;

--************************************** [weather]

CREATE TABLE weather
(
 TimeStamp             TIMESTAMP(3) NOT NULL ,
 Temperature           DOUBLE PRECISION NOT NULL ,
 Precipitation         DOUBLE PRECISION NOT NULL ,
 ChanceofPrecipitation DOUBLE PRECISION NOT NULL ,
 State                 VARCHAR(50) NOT NULL ,

 CONSTRAINT PK_weather PRIMARY KEY (TimeStamp)
);



--************************************** [HvacUsage]

CREATE TABLE HvacUsage
(
 TimeStamp    TIMESTAMP(3) NOT NULL ,
 SensorId     INT NOT NULL ,
 EndTimeStamp TIMESTAMP(3) NULL ,
 Usage        DOUBLE PRECISION NOT NULL ,
 Cost         MONEY NOT NULL ,
 Temperature  DOUBLE PRECISION NOT NULL ,

 CONSTRAINT PK_HvacUsage PRIMARY KEY (TimeStamp, SensorId)
);



--************************************** [WaterUsage]

CREATE TABLE WaterUsage
(
 TimeStamp    TIMESTAMP(3) NOT NULL ,
 SensorId     INT NOT NULL ,
 EndTimeStamp TIMESTAMP(3) NULL ,
 Usage        DOUBLE PRECISION NOT NULL ,
 Cost         MONEY NOT NULL ,

 CONSTRAINT PK_WaterUsage PRIMARY KEY (TimeStamp, SensorId)
);



--************************************** [DailyUsage]

CREATE TABLE DailyUsage
(
 Date            DATE NOT NULL ,
 TotalWaterUsage DOUBLE PRECISION NOT NULL ,
 TotalPowerUsage INT NOT NULL ,
 TotalPowerCost  MONEY NOT NULL ,
 TotalWaterCost  MONEY NOT NULL ,
 TotalHvacUsage  DOUBLE PRECISION NOT NULL ,
 TotalHvacCost   MONEY NOT NULL ,

 CONSTRAINT PK_DailyUsage PRIMARY KEY (Date)
);



--************************************** [EnergyUsage]

CREATE TABLE EnergyUsage
(
 TimeStamp    TIMESTAMP(3) NOT NULL ,
 SensorId     INT NOT NULL ,
 EndTimeStamp TIMESTAMP(3) NULL ,
 Usage        INT NOT NULL ,
 Cost         MONEY NOT NULL ,

 CONSTRAINT PK_EnergyUsage PRIMARY KEY (TimeStamp, SensorId)
);



--************************************** [Rooms]

CREATE TABLE Rooms
(
 RoomId   INT NOT NULL ,
 RoomName VARCHAR(50) NOT NULL ,

 CONSTRAINT PK_Rooms PRIMARY KEY (RoomId)
);



--************************************** [Sensors]

CREATE TABLE Sensors
(
 SensorID    INT NOT NULL ,
 SensorName  VARCHAR(50) NOT NULL ,
 SensorState INT NOT NULL ,
 RoomId      INT NOT NULL ,

 CONSTRAINT PK_Sensors PRIMARY KEY (SensorID),
 CONSTRAINT FK_30 FOREIGN KEY (RoomId)
  REFERENCES Rooms(RoomId)
);


CREATE INDEX fkIdx_30 ON Sensors
 (
  RoomId ASC
 );


--************************************** [Appliances]

CREATE TABLE Appliances
(
 ApplianceId INT NOT NULL ,
 SensorID    INT NOT NULL ,
 PowerUsage  INT NOT NULL ,
 PowerRate   MONEY NOT NULL ,
 ApplianceName VARCHAR(50) NOT NULL ,

 CONSTRAINT PK_Appliances PRIMARY KEY (ApplianceId),
 CONSTRAINT FK_38 FOREIGN KEY (SensorID)
  REFERENCES Sensors(SensorID)
);


CREATE INDEX fkIdx_38 ON Appliances
 (
  SensorID ASC
 );