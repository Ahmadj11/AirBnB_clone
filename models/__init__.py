"""creates a pythong package out of models directory/module"""
from models.engine.file_storage import FileStorage

# create a unique FIleStorage instance for application
storage = FileStorage()
storage.reload()
