# Ejecutar en orden para evitar errores.

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
    imagen varchar(255),
	PRIMARY KEY (mascotaID)
);

insert into mascotas (nombre,animal,raza,color,edad,zona,fecha,descripcion,estado,imagen) values ("Fito", "Perro", "Doberman","negro",7,"Caballito","2021-12-01","Perro encontrado","perdida","static/images/perro.jpg");

insert into mascotas (nombre,animal,raza,color,edad,zona,fecha,descripcion,estado,imagen) values ("Casper", "Gato", "Siames","marron",2,"Lanus","2024-6-01","Gato encontrado","perdida","static/images/gato.webp");

insert into mascotas (nombre,animal,raza,color,edad,zona,fecha,descripcion,estado,imagen) values ("Peter", "Perro", "Pastor aleman","rubio",12,"Moron","2023-7-08","Perro encontrado","perdida","static/images/perro2.webp");


CREATE TABLE personas(
	personaID int NOT NULL AUTO_INCREMENT,
    mascotaID int,
    telefono int NOT NULL,
    email varchar(255) NOT NULL,
	PRIMARY KEY (personaID),
    FOREIGN KEY (mascotaID) REFERENCES mascotas(mascotaID)
);

insert into personas (mascotaID,telefono,email) values (2,312354,"email@deejemplo");

insert into personas (mascotaID,telefono,email) values (3,5435643,"email@deejemplo");

insert into personas (mascotaID,telefono,email) values (1,65479,"email@deejemplo");