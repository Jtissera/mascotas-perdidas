# Ejecutar en orden para evitar errores.

CREATE TABLE mascotas(
	mascotaID int NOT NULL AUTO_INCREMENT,
    nombre varchar(255),
    animal varchar(255),
    raza varchar(255),
    color varchar(255) NOT NULL,
    edad int,
    fecha date,
    descripcion varchar(255),
    estado varchar(255),
    imagen varchar(255),
    latitud DECIMAL(9, 6),
    longitud DECIMAL(9, 6),
    PRIMARY KEY (mascotaID)
);

insert into mascotas (nombre,animal,raza,color,edad,fecha,descripcion,estado,imagen,latitud,longitud) values ("Fito", "Perro", "Doberman","negro",7,"2021-12-01","Perro encontrado","perdida","static/images/perro.jpg",-34.498012, -58.489233);

insert into mascotas (nombre,animal,raza,color,edad,fecha,descripcion,estado,imagen,latitud,longitud) values ("Casper", "Gato", "Siames","marron",2,"2024-6-01","Gato encontrado","perdida","static/images/gato.webp",-34.584517, -58.416623);

insert into mascotas (nombre,animal,raza,color,edad,fecha,descripcion,estado,imagen,latitud,longitud) values ("Peter", "Perro", "Pastor aleman","rubio",12,"2023-7-08","Perro encontrado","perdida","static/images/perro2.webp",-34.616507, -58.432268);


CREATE TABLE personas(
	personaID int NOT NULL AUTO_INCREMENT,
    mascotaID int,
    telefono int NOT NULL,
    email varchar(255) NOT NULL,
	PRIMARY KEY (personaID),
    FOREIGN KEY (mascotaID) REFERENCES mascotas(mascotaID)
);

insert into personas (telefono,email) values (312354,"email@deejemplo");

insert into personas (telefono,email) values (5435643,"email@deejemplo");

insert into personas (telefono,email) values (65479,"email@deejemplo");