from mysql.connector import connect, Error

try:
	with (connect(
			host="localhost",
			user="root",
			password="69660469",
			database="cinematic"
	)
	as conn):
		
		with conn.cursor() as cursor:
			create_directors_table = """
            CREATE TABLE IF NOT EXISTS directors (
                director_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                name VARCHAR(30) NOT NULL,
                surname VARCHAR(30) NOT NULL,
                rating INT NOT NULL
            );
            """
			cursor.execute(create_directors_table)
			create_movies_table = """
            CREATE TABLE IF NOT EXISTS movies (
                movie_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                title VARCHAR(50) NOT NULL,
                year INT UNSIGNED NOT NULL,
                category VARCHAR(30) NOT NULL,
                director_id INT NOT NULL,
                rating INT NOT NULL,
                FOREIGN KEY (director_id) REFERENCES directors(director_id)
            );
            """
			cursor.execute(create_movies_table)
			
			conn.commit()
			print("Tabulky byly vytvořeny nebo již existují!")
except Error as e:
	print(f"Nastala chyba: {e}")
