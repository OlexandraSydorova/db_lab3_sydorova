DO $$
DECLARE
    film_id_count   disney_film_copy.film_id%TYPE;
    film_prod disney_film_copy.film_name%TYPE;

BEGIN
    film_id_count := 200;
    film_prod := 'Film';
    FOR counter IN 1..10
        LOOP
            INSERT INTO disney_film_copy(film_id, film_name)
            VALUES (counter + film_id_count, film_prod || counter);
        END LOOP;
END;
$$