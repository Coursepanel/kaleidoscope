def return_prompt(en_statement):
    return f"""
    The following is my neo4j graph database schema for storing information about the courses being offered at a university

    ```
    {{
  Department: {{
    relationships: {{
      BELONGS_TO: {{
        count: 2561,
        properties: {{}},
        direction: "in",
        labels: ["Course"]
      }}
    }},
    count: 19,
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
        count: 35750,
        properties: {{}},
        direction: "in",
        labels: ["Course"]
      }}
    }},
    count: 22816,
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
    count: 2561,
    type: "relationship",
    properties: {{}}
  }},
  BOOK: {{
    count: 35750,
    type: "relationship",
    properties: {{}}
  }},
  Tag: {{
    relationships: {{
      TAG: {{
        count: 61641,
        properties: {{}},
        direction: "in",
        labels: ["Course"]
      }}
    }},
    count: 49234,
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
    count: 61641,
    type: "relationship",
    properties: {{}}
  }},
  PREREQUISITE: {{
    count: 331,
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
      }},
      PREREQUISITE: {{
        count: 69,
        properties: {{}},
        direction: "out",
        labels: ["Course", "Course"]
      }}
    }},
    count: 2561,
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
    Extract the keywords and use them to look if a node contains that keyword inside it and generate the cypher query to fetch the information from the database
    Generate and return just the code for a cypher query against this database to actually fetch this information as distinct database entries. Return just the code, not the entire query or the explanation.
    """