-- Crea la tabla de usuarios para iniciar sesion
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nickname VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);