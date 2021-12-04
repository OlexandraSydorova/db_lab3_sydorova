-------------------------
-- Create disney_film table
-------------------------
CREATE TABLE disney_film
(
film_id INT NOT NULL,
film_name char(50) NOT NULL,
film_date DATE NOT NULL
);
-------------------------
-- Create script table
-------------------------
CREATE TABLE script
(
script_id INT NOT NULL,
scene char(15) NOT NULL,
script_text char(1000) NOT NULL,
film_id INT NOT NULL,
genre_id INT NOT NULL
);
-------------------------
-- Create genre table
-------------------------
CREATE TABLE genre
(
genre_id INT NOT NULL,
genre_name char(50) NOT NULL
);
 
 ----------------------
-- Define primary keys
----------------------
ALTER TABLE Disney_film ADD CONSTRAINT PK_Disney_film PRIMARY KEY (film_id);
ALTER TABLE Script ADD CONSTRAINT PK_Script PRIMARY KEY (script_id);
ALTER TABLE Genre ADD CONSTRAINT PK_Genre PRIMARY KEY (genre_id);
----------------------
-- Define foreign keys
----------------------
ALTER TABLE Script
ADD CONSTRAINT FK_Script_Disney_film FOREIGN KEY (film_id) REFERENCES Disney_film
(film_id);
ALTER TABLE Script
ADD CONSTRAINT FK_Script_Genre FOREIGN KEY (genre_id) REFERENCES
Genre (genre_id);
