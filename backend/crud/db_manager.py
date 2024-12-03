from pymongo import MongoClient
from bson import ObjectId

class DatabaseManager:
    def __init__(self, connection_string: str, db_name: str, collection_name: str, max_pool_size: int = 100, min_pool_size: int = 1):
        self.client = MongoClient(
            connection_string,
            maxPoolSize=max_pool_size,
            minPoolSize=min_pool_size
        )
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert(self, data: dict):
        return self.collection.insert_one(data)

    def find_all(self):
        return list(self.collection.find())

    def find_by_id(self, identifier: str):
        return self.collection.find_one({"bom_id": identifier})

    def update(self, identifier: str, updates: dict):
        return self.collection.update_one({"bom_id": identifier}, {"$set": updates})

    def delete(self, identifier: str):
        return self.collection.delete_one({"bom_id": identifier})

    @staticmethod
    def to_dict(item):
        if item:
            item["_id"] = str(item["_id"])
        return item
    
    def execute_transaction(self, operations: list):
        """
        Execute a series of database operations as a transaction. 
        Args:
        - operations (list): A list of functions representing database operations.
        Returns:
        - str: A success message if the transaction is committed.
        """
        session = self.client.start_session()
        try:
            with session.start_transaction():
                for operation in operations:
                    operation(session)
            return "Transaction committed successfully."
        except PyMongoError as e:
            return f"Transaction failed: {str(e)}"
        finally:
            session.end_session()
'''example
    def update_item_and_log(db_manager, item_id, item_updates, log_entry):
    """
    Update an item in the item collection and insert a log entry in the log collection.
    """
    def update_operations(session):
        # Update the item in the item_collection
        db_manager.item_collection.update_one(
            {"bom_id": item_id}, {"$set": item_updates}, session=session
        )
        # Insert a log entry into the log_collection
        db_manager.log_collection.insert_one(log_entry, session=session)

    return db_manager.execute_transaction([update_operations])

    if __name__ == "__main__":
    # Initialize the DatabaseManager
    db_manager = DatabaseManager(
        connection_string="mongodb://localhost:27017/",
        db_name="Scrapit",
        item_collection_name="item",
        log_collection_name="log"
    )

    # Example item update and log entry
    item_id = "101"
    item_updates = {"status": "updated", "last_updated": "2024-11-29"}
    log_entry = {"operation": "update", "bom_id": item_id, "timestamp": "2024-11-29T10:00:00Z"}

    # Execute the transaction
    result = update_item_and_log(db_manager, item_id, item_updates, log_entry)
    print(result)
'''

    def insert_with_transaction(self, data_list: list):
        """
        Insert multiple documents within a transaction.

        Args:
        - data_list (list): List of documents to be inserted.

        Returns:
        - str: A success message if the transaction is committed.
        """
        def operation(session):
            for data in data_list:
                self.collection.insert_one(data, session=session)

        return self.execute_transaction([operation])
