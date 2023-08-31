from dataclasses import dataclass
import os

@dataclass
class TestCase:
    """"""
    table_name: str
    test_scenario: str
    query: str
    
    def save_query(self, location: str):
        """Write the sql query to file at the specified location"""
        filename = "_".join([self.table_name, self.test_scenario])
        filepath = os.path.join(location, filename)

        with open(filepath, "w") as query_file:
            query_file.write(self.query)
