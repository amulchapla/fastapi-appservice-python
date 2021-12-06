import os

from dotenv import load_dotenv

load_dotenv()

db_serv = os.getenv('DATABASE_SERVER')
print("DB server name: ", db_serv)

java_home = os.getenv('JAVA_HOME')
print("Java Home: ", java_home)

filestore_path = os.getenv('FILESTORE_PATH')
print("Filestore path: ", filestore_path)