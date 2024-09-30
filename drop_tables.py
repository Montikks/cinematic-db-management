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


def drop_tables(cursor):
	"""
	Odstraní tabulky 'directors' a 'movies' z databáze.
	"""
	drop_movies_query = "DROP TABLE IF EXISTS movies;"
	drop_directors_query = "DROP TABLE IF EXISTS directors;"
	
	try:
		cursor.execute(drop_movies_query)
		print("🗑️ Tabulka 'movies' byla odstraněna.")
		
		cursor.execute(drop_directors_query)
		print("🗑️ Tabulka 'directors' byla odstraněna.")
	except Error as e:
		print(f"❌ Chyba při odstraňování tabulek: {e}")


def main():
	"""
	Hlavní funkce, která zajišťuje připojení k databázi a volá funkci pro odstranění tabulek.
	"""
	try:
		with connect(
				host=DB_HOST,
				user=DB_USER,
				password=DB_PASSWORD,
				database=DB_NAME
		) as conn:
			with conn.cursor() as cursor:
				print("🔍 Odstraňování tabulek...")
				drop_tables(cursor)
	
	except Error as e:
		print(f"❌ Nastala chyba: {e}")


if __name__ == "__main__":
	main()
