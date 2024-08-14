from pathlib import Path


path = Path("Emails")
print(path.exists())
print(path.mkdir())
print(path.rmdir())