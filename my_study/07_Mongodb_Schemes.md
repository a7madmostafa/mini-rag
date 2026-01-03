# Mongodb Schemes

Although MongoDB is a NoSQL database, using `Collections` which accept different types of data with no schema limitation, it's a good practice to define a schema for your data.

## Schemes

1- Create a new directory named `db_schemes` in the `models` directory contains `class` for each `collection`.

2- Create a new file named `project.py` in the `db_schemes` directory, contains `class` for `project` collection.

3- Create a new file named `data_chunk.py` in the `db_schemes` directory, contains `class` for `data_chunk` collection.

4- Create a new file named `BaseDataModel` in the `models` directory, contains `class` for `BaseDataModel` which is a base class for all other models.

5- Create a new file named `ProjectModel` in the `models` directory, contains `class` for `ProjectModel` which is a model for `project` collection.