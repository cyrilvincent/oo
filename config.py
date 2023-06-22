import demo_directx
import repository

driver = demo_directx.NVidiaImpl()
version = "0.1"
default_path = "data/media/books.csv"
default_repository = repository.BookCSVRepository(default_path)