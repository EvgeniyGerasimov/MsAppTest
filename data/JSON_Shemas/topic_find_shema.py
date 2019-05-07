TOPIC_SHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "topic_id": {
          "type": "integer"
        },
        "edp": {
          "type": "object",
          "properties": {
            "topic_edition_id": {
              "type": "integer"
            },
            "topic_id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "short_title": {
              "type": "string"
            },
            "photos": {
              "type": "array",
              "items": {}
            }
          },
          "required": [
            "topic_edition_id",
            "topic_id",
            "alias",
            "title",
            "subtitle",
            "short_title",
            "photos"
          ]
        },
        "articles": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "article_id": {
                  "type": "integer"
                },
                "edp": {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "dt_published": {
                      "type": "string"
                    },
                    "original_entity_id": {
                      "type": "null"
                    },
                    "video_edition_id": {
                      "type": "null"
                    },
                    "preview": {
                      "type": "string"
                    },
                    "extra_query_params": {
                      "type": "string"
                    },
                    "article_edition_id": {
                      "type": "integer"
                    },
                    "body": {
                      "type": "string"
                    },
                    "photos": {
                      "type": "object",
                      "properties": {
                        "s1": {
                          "type": "string"
                        },
                        "s2": {
                          "type": "string"
                        },
                        "s3": {
                          "type": "string"
                        },
                        "s4": {
                          "type": "string"
                        },
                        "s6": {
                          "type": "string"
                        },
                        "s7": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "s1",
                        "s2",
                        "s3",
                        "s4",
                        "s6",
                        "s7"
                      ]
                    },
                    "gallery_photos": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "title",
                    "alias",
                    "dt_published",
                    "original_entity_id",
                    "video_edition_id",
                    "preview",
                    "extra_query_params",
                    "article_edition_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  "type": "object",
                  "properties": {
                    "article_type_id": {
                      "type": "integer"
                    },
                    "edp": {
                      "type": "object",
                      "properties": {
                        "title": {
                          "type": "string"
                        },
                        "article_type_edition_id": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "title",
                        "article_type_edition_id"
                      ]
                    }
                  },
                  "required": [
                    "article_type_id",
                    "edp"
                  ]
                },
                "author": {
                  "type": "object",
                  "properties": {
                    "author_id": {
                      "type": "integer"
                    },
                    "edp": {
                      "type": "object",
                      "properties": {
                        "author_edition_id": {
                          "type": "integer"
                        },
                        "author_id": {
                          "type": "string"
                        },
                        "first_name": {
                          "type": "string"
                        },
                        "last_name": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "author_edition_id",
                        "author_id",
                        "first_name",
                        "last_name"
                      ]
                    },
                    "avatar": {
                      "type": "array",
                      "items": {}
                    },
                    "user": {
                      "type": "array",
                      "items": {}
                    },
                    "articles": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "author_id",
                    "edp",
                    "avatar",
                    "user",
                    "articles"
                  ]
                },
                "co_author": {
                  "type": "array",
                  "items": {}
                },
                "race_type": {
                  "type": "object",
                  "properties": {
                    "race_type_id": {
                      "type": "integer"
                    },
                    "edp": {
                      "type": "object",
                      "properties": {
                        "race_type_edition_id": {
                          "type": "integer"
                        },
                        "race_type_id": {
                          "type": "string"
                        },
                        "title": {
                          "type": "string"
                        },
                        "alias": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "title",
                        "alias"
                      ]
                    },
                    "category_edition": {
                      "type": "array",
                      "items": {}
                    },
                    "photos": {
                      "type": "object",
                      "properties": {
                        "s1": {
                          "type": "string"
                        },
                        "s2": {
                          "type": "string"
                        },
                        "s3": {
                          "type": "string"
                        },
                        "s4": {
                          "type": "string"
                        },
                        "s5": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "s1",
                        "s2",
                        "s3",
                        "s4",
                        "s5"
                      ]
                    },
                    "race_type_photos": {
                      "type": "array",
                      "items": {}
                    },
                    "canonical": {
                      "type": "array",
                      "items": {}
                    },
                    "alternatives": {
                      "type": "array",
                      "items": {}
                    },
                    "default_duration": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "race_type_id",
                    "edp",
                    "category_edition",
                    "photos",
                    "race_type_photos",
                    "canonical",
                    "alternatives",
                    "default_duration"
                  ]
                },
                "video": {
                  "type": "array",
                  "items": {}
                },
                "gallery": {
                  "type": "array",
                  "items": {}
                },
                "drivers": {
                  "type": "array",
                  "items": {}
                },
                "teams": {
                  "type": "array",
                  "items": {}
                },
                "topics": {
                  "type": "array",
                  "items": {}
                },
                "alternatives": {
                  "type": "array",
                  "items": {}
                },
                "next_entity": {
                  "type": "null"
                },
                "pre_entity": {
                  "type": "null"
                }
              },
              "required": [
                "article_id",
                "edp",
                "article_type",
                "author",
                "co_author",
                "race_type",
                "video",
                "gallery",
                "drivers",
                "teams",
                "topics",
                "alternatives",
                "next_entity",
                "pre_entity"
              ]
            },
            {
              "type": "object",
              "properties": {
                "article_id": {
                  "type": "integer"
                },
                "edp": {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "dt_published": {
                      "type": "string"
                    },
                    "original_entity_id": {
                      "type": "null"
                    },
                    "video_edition_id": {
                      "type": "null"
                    },
                    "preview": {
                      "type": "string"
                    },
                    "extra_query_params": {
                      "type": "null"
                    },
                    "article_edition_id": {
                      "type": "integer"
                    },
                    "body": {
                      "type": "string"
                    },
                    "photos": {
                      "type": "object",
                      "properties": {
                        "s1": {
                          "type": "string"
                        },
                        "s2": {
                          "type": "string"
                        },
                        "s3": {
                          "type": "string"
                        },
                        "s4": {
                          "type": "string"
                        },
                        "s6": {
                          "type": "string"
                        },
                        "s7": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "s1",
                        "s2",
                        "s3",
                        "s4",
                        "s6",
                        "s7"
                      ]
                    },
                    "gallery_photos": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "title",
                    "alias",
                    "dt_published",
                    "original_entity_id",
                    "video_edition_id",
                    "preview",
                    "extra_query_params",
                    "article_edition_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  "type": "object",
                  "properties": {
                    "article_type_id": {
                      "type": "integer"
                    },
                    "edp": {
                      "type": "object",
                      "properties": {
                        "title": {
                          "type": "string"
                        },
                        "article_type_edition_id": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "title",
                        "article_type_edition_id"
                      ]
                    }
                  },
                  "required": [
                    "article_type_id",
                    "edp"
                  ]
                },
                "author": {
                  "type": "object",
                  "properties": {
                    "author_id": {
                      "type": "integer"
                    },
                    "edp": {
                      "type": "object",
                      "properties": {
                        "author_edition_id": {
                          "type": "integer"
                        },
                        "author_id": {
                          "type": "string"
                        },
                        "first_name": {
                          "type": "string"
                        },
                        "last_name": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "author_edition_id",
                        "author_id",
                        "first_name",
                        "last_name"
                      ]
                    },
                    "avatar": {
                      "type": "array",
                      "items": {}
                    },
                    "user": {
                      "type": "array",
                      "items": {}
                    },
                    "articles": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "author_id",
                    "edp",
                    "avatar",
                    "user",
                    "articles"
                  ]
                },
                "co_author": {
                  "type": "array",
                  "items": {}
                },
                "race_type": {
                  "type": "object",
                  "properties": {
                    "race_type_id": {
                      "type": "integer"
                    },
                    "edp": {
                      "type": "object",
                      "properties": {
                        "race_type_edition_id": {
                          "type": "integer"
                        },
                        "race_type_id": {
                          "type": "string"
                        },
                        "title": {
                          "type": "string"
                        },
                        "alias": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "title",
                        "alias"
                      ]
                    },
                    "category_edition": {
                      "type": "array",
                      "items": {}
                    },
                    "photos": {
                      "type": "object",
                      "properties": {
                        "s1": {
                          "type": "string"
                        },
                        "s2": {
                          "type": "string"
                        },
                        "s3": {
                          "type": "string"
                        },
                        "s4": {
                          "type": "string"
                        },
                        "s5": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "s1",
                        "s2",
                        "s3",
                        "s4",
                        "s5"
                      ]
                    },
                    "race_type_photos": {
                      "type": "array",
                      "items": {}
                    },
                    "canonical": {
                      "type": "array",
                      "items": {}
                    },
                    "alternatives": {
                      "type": "array",
                      "items": {}
                    },
                    "default_duration": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "race_type_id",
                    "edp",
                    "category_edition",
                    "photos",
                    "race_type_photos",
                    "canonical",
                    "alternatives",
                    "default_duration"
                  ]
                },
                "video": {
                  "type": "array",
                  "items": {}
                },
                "gallery": {
                  "type": "array",
                  "items": {}
                },
                "drivers": {
                  "type": "array",
                  "items": {}
                },
                "teams": {
                  "type": "array",
                  "items": {}
                },
                "topics": {
                  "type": "array",
                  "items": {}
                },
                "alternatives": {
                  "type": "array",
                  "items": {}
                },
                "next_entity": {
                  "type": "null"
                },
                "pre_entity": {
                  "type": "null"
                }
              },
              "required": [
                "article_id",
                "edp",
                "article_type",
                "author",
                "co_author",
                "race_type",
                "video",
                "gallery",
                "drivers",
                "teams",
                "topics",
                "alternatives",
                "next_entity",
                "pre_entity"
              ]
            }
          ]
        },
        "videos": {
          "type": "array",
          "items": {}
        }
      },
      "required": [
        "topic_id",
        "edp",
        "articles",
        "videos"
      ]
    }
  },
  "required": [
    "data"
  ]
}

