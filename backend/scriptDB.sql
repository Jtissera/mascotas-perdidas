CREATE TABLE mascotas(
	mascotaID int NOT NULL AUTO_INCREMENT,
    nombre varchar(255),
    animal varchar(255),
    raza varchar(255),
    color varchar(255) NOT NULL,
    edad varchar(255),
    zona varchar(255) NOT NULL,
    fecha date,
    descripcion varchar(255),
    estado varchar(255),
	PRIMARY KEY (mascotaID)
);

insert into mascotas (nombre,animal,raza,color,edad,zona,fecha,descripcion,estado) values ("Fito", "Perro", "Doberman","negro",7,"Caballito","2021-12-01","Perro encontrado","perdida");

insert into mascotas (nombre,animal,raza,color,edad,zona,fecha,descripcion,estado) values ("Casper", "Gato", "Siames","marron",2,"Lanus","2024-6-01","Gato encontrado","perdida");

insert into mascotas (nombre,animal,raza,color,edad,zona,fecha,descripcion,estado) values ("Peter", "Perro", "Pastor aleman","rubio",12,"Moron","2023-7-08","Perro encontrado","perdida");


CREATE TABLE personas(
	personaID int NOT NULL AUTO_INCREMENT,
    telefono int NOT NULL,
    email varchar(255) NOT NULL,
	PRIMARY KEY (personaID)
);

insert into personas (telefono,email) values (312354,"email1@deejemplo");

insert into personas (telefono,email) values (5435643,"email2@deejemplo");

insert into personas (telefono,email) values (65479,"email3@deejemplo");

insert into personas (telefono,email) values (5436,"email4@deejemplo");
