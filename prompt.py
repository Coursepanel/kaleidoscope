def return_prompt(en_statement):
    return f"""
    The following is my neo4j graph database schema for storing information about the courses being offered at a university

    ```
    {{
    Department: {{
        relationships: {{
        BELONGS_TO: {{
            count: 1839,
            properties: {{}},
            direction: "in",
            labels: ["Course"]
        }}
        }},
        count: 18,
        type: "node",
        properties: {{
        name: {{
            indexed: false,
            unique: false,
            existence: false,
            type: "STRING"
        }}
        }},
        labels: []
    }},
    Book: {{
        relationships: {{
        BOOK: {{
            count: 25525,
            properties: {{}},
            direction: "in",
            labels: ["Course"]
        }}
        }},
        count: 17022,
        type: "node",
        properties: {{
        name: {{
            indexed: false,
            unique: false,
            existence: false,
            type: "STRING"
        }}
        }},
        labels: []
    }},
    BELONGS_TO: {{
        count: 1839,
        type: "relationship",
        properties: {{}}
    }},
    BOOK: {{
        count: 25525,
        type: "relationship",
        properties: {{}}
    }},
    Tag: {{
        relationships: {{
        TAG: {{
            count: 43877,
            properties: {{}},
            direction: "in",
            labels: ["Course"]
        }}
        }},
        count: 36314,
        type: "node",
        properties: {{
        name: {{
            indexed: false,
            unique: false,
            existence: false,
            type: "STRING"
        }}
        }},
        labels: []
    }},
    TAG: {{
        count: 43877,
        type: "relationship",
        properties: {{}}
    }},
    Course: {{
        relationships: {{
        BELONGS_TO: {{
            count: 0,
            properties: {{}},
            direction: "out",
            labels: ["Department"]
        }},
        BOOK: {{
            count: 0,
            properties: {{}},
            direction: "out",
            labels: ["Book"]
        }},
        TAG: {{
            count: 0,
            properties: {{}},
            direction: "out",
            labels: ["Tag"]
        }}
        }},
        count: 1839,
        type: "node",
        properties: {{
        name: {{
            indexed: false,
            unique: false,
            existence: false,
            type: "STRING"
        }},
        id: {{
            indexed: false,
            unique: false,
            existence: false,
            type: "STRING"
        }},
        extractedPrereqCourseCodes: {{
            indexed: false,
            unique: false,
            existence: false,
            type: "LIST"
        }}
        }},
        labels: []
    }}
    }}
    ```

    A user has requested for the following information from the database - {en_statement}

    Generate and return just the code for a cypher query against this database to actually fetch this information as distinct database entries. Return just the code, not the entire query or the explanation.
    """