# Day 51 of 100DaysofCode

Feeling excited to start Day 51 of 100 DaysOfCode, today, I watched a Mongodb tutorial video by CodeWithHarry. This video provides a beginner guide to MongoDB, its basic commands, creating, updating and deleting operations and many more. For referneces, [Watch](https://youtu.be/J6mDkcqU_ZE?si=U_XznDhuURGSZPdV) the video.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-51
```

## What is MongoDB?

MongoDB is a popular, open-source, NoSQL database that is designed for high-performance, scalability, and flexibility. It stores data in a flexible, semi-structured, BSON (Binary JSON) format, which allows for rapid development and iteration. MongoDB is known for its ability to handle large volumes of data and is commonly used in modern web applications, mobile applications, and other data-intensive projects.

Some key features of MongoDB include:

- **Document-Oriented:** MongoDB stores data in a document format similar to JSON, which is a highly flexible and easy-to-read structure.

- **Scalability:** MongoDB can scale horizontally by adding more servers to a cluster, making it suitable for handling large datasets and high traffic loads.

- **Query Language:** It provides a powerful and flexible query language for querying and manipulating data.

- **Indexing:** MongoDB supports various types of indexes, making it efficient for querying and searching data.

- **High Availability:** MongoDB can be configured for high availability through replication and failover mechanisms.

- **Geospatial Support:** It has built-in support for geospatial data, which is valuable for location-based applications.

- **Aggregation Framework:** MongoDB includes a versatile aggregation framework for complex data processing tasks.

## How to Install MongoDB

### Installing on Windows

1. **Download MongoDB:**
   - Go to the [MongoDB download page](https://www.mongodb.com/try/download/community) and select the Windows version.
   - Choose the version that matches your system architecture (64-bit recommended).

2. **Install MongoDB:**
   - Run the downloaded installer and follow the installation instructions.
   - During installation, you can choose the installation directory and other settings.

3. **Start MongoDB:**
   - MongoDB runs as a service by default, so it starts automatically after installation.
   - To manually start, stop, or configure the MongoDB service, use the Windows Services application.

4. **Access MongoDB:**
   - You can interact with MongoDB using the MongoDB Shell (mongosh), a command-line interface.
   - Open a command prompt and run `mongosh` to start the shell.

### Installing on macOS

1. **Download MongoDB:**
   - Go to the [MongoDB download page](https://www.mongodb.com/try/download/community) and select macOS.
   - Choose the version compatible with your macOS version.

2. **Install MongoDB:**
   - Open the downloaded .tgz file.
   - Drag and drop the `mongodb` directory to a location on your file system, e.g., `/usr/local/`.

3. **Start MongoDB:**
   - Open a terminal and run the following command to start the MongoDB server: 
     ```shell
     mongod --dbpath /usr/local/mongodb/data
     ```

4. **Access MongoDB:**
   - Open another terminal and run `mongosh` to start the MongoDB Shell.

### Installing on Linux (Ubuntu)

1. **Import MongoDB GPG Key:**
   - Open a terminal and run the following command to import the MongoDB GPG key:
     ```shell
     wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
     ```

2. **Create a MongoDB Source List:**
   - Run the following command to create a MongoDB source list file:
     ```shell
     echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -sc)/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
     ```

3. **Install MongoDB:**
   - Update your package list and install MongoDB with the following commands:
     ```shell
     sudo apt update
     sudo apt install -y mongodb-org
     ```

4. **Start MongoDB:**
   - Start the MongoDB service using the following command:
     ```shell
     sudo service mongod start
     ```

5. **Access MongoDB:**
   - Open a terminal and run `mongosh` to start the MongoDB Shell.

For detailed installation instructions for other operating systems and additional configuration options, refer to the official [MongoDB Installation Guide](https://docs.mongodb.com/manual/installation/).

Congratulations! You have successfully installed MongoDB. You can now start using MongoDB for your data storage needs.

## Basic Commands and CRUD Operations

MongoDB provides a powerful set of commands for managing and manipulating data. This guide will cover some basic commands and CRUD (Create, Read, Update, Delete) operations in MongoDB.

### Basic Commands

### 1. Connect to MongoDB

To connect to a MongoDB server, open a terminal and run:

```shell
mongosh
```

This opens the MongoDB shell, where you can interact with the database.

### 2. Show Databases

List all the available databases:

```shell
show dbs
```

### 3. Switch Database

Switch to a specific database or create one if it doesn't exist:

```shell
use mydb
```

### 4. Show Collections

List all collections in the current database:

```shell
show collections
```

## CRUD Operations

### Create (Insert) Document

To add a new document to a collection, use the `insertOne` or `insertMany` method.

#### Insert a Single Document:

```shell
db.collectionName.insertOne({ field1: "value1", field2: "value2" })
```

#### Insert Multiple Documents:

```shell
db.collectionName.insertMany([
  { field1: "value1", field2: "value2" },
  { field1: "value3", field2: "value4" }
])
```

### Read (Query) Documents

To retrieve data from a collection, use the `find` method. You can specify conditions to filter the data.

#### Find All Documents in a Collection:

```shell
db.collectionName.find()
```

#### Find Documents Matching a Condition:

```shell
db.collectionName.find({ field1: "value1" })
```

### Update (Modify) Document

To update an existing document, use the `updateOne` or `updateMany` method.

#### Update a Single Document:

```shell
db.collectionName.updateOne({ field1: "value1" }, { $set: { field2: "new value" } })
```

#### Update Multiple Documents:

```shell
db.collectionName.updateMany({ field1: "value1" }, { $set: { field2: "new value" } })
```

### Delete (Remove) Document

To remove documents from a collection, use the `deleteOne` or `deleteMany` method.

#### Delete a Single Document:

```shell
db.collectionName.deleteOne({ field1: "value1" })
```

#### Delete Multiple Documents:

```shell
db.collectionName.deleteMany({ field1: "value1" })
```

### Aggregation

MongoDB provides powerful aggregation capabilities. You can use the `aggregate` method to perform complex operations like grouping, sorting, and transforming data.

Here's an example of grouping documents by a field and calculating the average:

```shell
db.collectionName.aggregate([
  {
    $group: {
      _id: "$field1",
      averageValue: { $avg: "$field2" }
    }
  }
])
```

# Advanced Operations and Aggregation

MongoDB provides a wide range of advanced operations and aggregation features for handling complex data queries and transformations. This guide covers sorting and limiting data, query operators, and aggregation using the aggregation pipeline.

## Sorting and Limiting Data

### Sort Documents

You can use the `sort` method to order documents based on one or more fields. For example, to sort documents by a field in ascending order:

```shell
db.collectionName.find().sort({ fieldName: 1 })
```

To sort in descending order:

```shell
db.collectionName.find().sort({ fieldName: -1 })
```

### Limit the Number of Results

To limit the number of documents returned, use the `limit` method:

```shell
db.collectionName.find().limit(10)
```

This query returns only the first 10 documents.

## Query Operators

MongoDB supports a variety of query operators for complex data filtering. Here are some common operators:

### Comparison Operators

- `$eq`: Matches values that are equal to a specified value.
- `$ne`: Matches values that are not equal to a specified value.
- `$gt`: Matches values that are greater than a specified value.
- `$lt`: Matches values that are less than a specified value.

Example:

```shell
db.collectionName.find({ fieldName: { $gt: 50 } })
```

### Logical Operators

- `$and`: Joins query clauses with a logical AND and returns documents that match all the conditions.
- `$or`: Joins query clauses with a logical OR and returns documents that match at least one condition.

Example:

```shell
db.collectionName.find({ $or: [{ field1: "value1" }, { field2: "value2" }] })
```

### Element Operators

- `$exists`: Matches documents that have a specified field.
- `$type`: Matches documents where the value of a field is of a specific type.

Example:

```shell
db.collectionName.find({ fieldName: { $exists: true } })
```

## Aggregation Pipeline

MongoDB's aggregation framework allows for complex data transformations and computations. The aggregation pipeline is a sequence of stages, with each stage performing an operation on the documents. Here's a basic structure:

```shell
db.collectionName.aggregate([
  { $match: { condition: value } },
  { $group: { _id: "$field", total: { $sum: "$value" } } },
  { $sort: { total: -1 } },
  { $limit: 10 }
])
```

In this example, the aggregation pipeline does the following:

1. `$match`: Filters documents based on a condition.
2. `$group`: Groups documents by a field and calculates the total using the `$sum` operator.
3. `$sort`: Sorts the result in descending order based on the total.
4. `$limit`: Limits the number of results to 10.

You can construct more complex aggregation pipelines by chaining stages together. The aggregation framework provides a wide range of operators and expressions for various data transformations.

For advanced queries and complex data manipulation, refer to the official [MongoDB Aggregation Documentation](https://docs.mongodb.com/manual/aggregation/). It provides in-depth information and examples for the aggregation framework.

