DROP TABLE IF EXISTS user_roles;
DROP TABLE IF EXISTS role_permissions;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS sheet_music;
DROP TABLE IF EXISTS permissions;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS roles;


CREATE TABLE users(
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password_hash TEXT
);

CREATE TABLE roles(
	id SERIAL PRIMARY KEY,
	name TEXT
);

CREATE TABLE user_roles(
	user_id INT,
	role_id INT
);

CREATE TABLE role_permissions(
	role_id INT,
	permission_id INT
);

CREATE TABLE lessons(
	id SERIAL PRIMARY KEY,
	student_id INT REFERENCES users(id),
	teacher_id INT REFERENCES users(id),
	lesson_time TIMESTAMP
);

CREATE TABLE permissions(
	id SERIAL PRIMARY KEY,
	name TEXT
);

CREATE TABLE sheet_music(
	id SERIAL PRIMARY KEY,
	title TEXT,
	access_level TEXT
);


