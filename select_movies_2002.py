from mysql.connector import connect, Error
from dotenv import load_dotenv
import os


load_dotenv()


DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def select_movies_from_2002(cursor):
	"""
	Vybere všechny filmy z tabulky 'movies', které byly vydány v roce 2002.
	"""
	query = "SELECT * FROM movies WHERE year = 2002;"
	cursor.execute(query)
	result = cursor.fetchall()
	
	if result:
		print("📅 Filmy z roku 2002:")
		for row in result:
			print(row)
	else:
		print("🚫 Žádné filmy z roku 2002 nebyly nalezeny.")


def main():
	"""
	Hlavní funkce, která zajišťuje připojení k databázi a volá funkci pro výběr filmů.
	"""
	try:
		with connect(
				host=DB_HOST,
				user=DB_USER,
				password=DB_PASSWORD,
				database=DB_NAME
		) as conn:
			with conn.cursor() as cursor:
				print("🔍 Vyhledávání filmů z roku 2002...")
				select_movies_from_2002(cursor)
	
	except Error as e:
		print(f"❌ Nastala chyba: {e}")


if __name__ == "__main__":
	main()
