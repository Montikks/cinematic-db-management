from mysql.connector import connect, Error
from dotenv import load_dotenv
import os

# Načtení proměnných z .env souboru
load_dotenv()

# Načtení přihlašovacích údajů z prostředí
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Data pro vložení do tabulky directors
directors = [
	('Frank', 'Darabont', 7),
	('Francis Ford', 'Coppola', 8),
	('Quentin', 'Tarantino', 10),
	('Christopher', 'Nolan', 9),
	('David', 'Fincher', 7)
]

# Data pro vložení do tabulky movies
movies = [
	('The Shawshank Redemption', 1994, 'Drama', 1, 8),
	('The Green Mile', 1999, 'Drama', 1, 6),
	('The Godfather', 1972, 'Crime', 2, 7),
	('The Godfather III', 1990, 'Crime', 2, 6),
	('Pulp Fiction', 1994, 'Crime', 3, 9),
	('Inglourious Basterds', 2009, 'War', 3, 8),
	('The Dark Knight', 2008, 'Action', 4, 9),
	('Interstellar', 2014, 'Sci-fi', 4, 8),
	('The Prestige', 2006, 'Drama', 4, 10),
	('Fight Club', 1999, 'Drama', 5, 7),
	('Zodiac', 2007, 'Crime', 5, 5),
	('Seven', 1995, 'Drama', 5, 8),
	('Alien 3', 1992, 'Horror', 5, 5)
]


def insert_directors(cursor, directors):
	"""
	Vloží záznamy do tabulky 'directors' pouze v případě, že ještě neexistují.
	"""
	for director in directors:
		cursor.execute("SELECT * FROM directors WHERE name = %s AND surname = %s", (director[0], director[1]))
		result = cursor.fetchone()
		if result is None:
			cursor.execute("INSERT INTO directors (name, surname, rating) VALUES (%s, %s, %s)", director)
			print(f"✅ Režisér {director[0]} {director[1]} vložen do databáze.")
		else:
			print(f"⏭️ Režisér {director[0]} {director[1]} již existuje.")


def insert_movies(cursor, movies):
	"""
	Vloží záznamy do tabulky 'movies' pouze v případě, že ještě neexistují.
	"""
	for movie in movies:
		cursor.execute("SELECT * FROM movies WHERE title = %s", (movie[0],))
		result = cursor.fetchone()
		if result is None:
			cursor.execute(
				"INSERT INTO movies (title, year, category, director_id, rating) VALUES (%s, %s, %s, %s, %s)", movie)
			print(f"✅ Film '{movie[0]}' vložen do databáze.")
		else:
			print(f"⏭️ Film '{movie[0]}' již existuje.")


def main():
	"""
	Hlavní funkce, která zajišťuje připojení k databázi a volá funkce pro vkládání dat.
	"""
	try:
		with connect(
				host=DB_HOST,
				user=DB_USER,
				password=DB_PASSWORD,
				database=DB_NAME
		) as conn:
			with conn.cursor() as cursor:
				print("🔄 Vkládání režisérů...")
				insert_directors(cursor, directors)
				
				print("\n🔄 Vkládání filmů...")
				insert_movies(cursor, movies)
				
				conn.commit()
				print("\n✅ Všechna data byla úspěšně vložena nebo již existují.")
	
	except Error as e:
		print(f"❌ Nastala chyba: {e}")


if __name__ == "__main__":
	main()
