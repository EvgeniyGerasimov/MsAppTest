PROMOTION_TOP_BLOCK_SHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  
  "properties": {
    "data": {
      
      "items": [
        {
          
          "properties": {
            "entity_type": {
              
            },
            "slot": {
              
            },
            "promote_type": {
              
            },
            "entity": {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "is_target_blank": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "preview": {
                      
                    },
                    "dt_published": {
                      
                    },
                    "article_edition_id": {
                      
                    },
                    "original_entity_id": {
                      
                    },
                    "video_edition_id": {
                      
                    },
                    "is_prime": {
                      
                    },
                    "extra_query_params": {
                      
                    },
                    "media_type": {
                      
                    },
                    "body": {
                      
                    },
                    "photos": {
                      
                      "properties": {
                        "s1": {
                          
                        },
                        "s2": {
                          
                        },
                        "s3": {
                          
                        },
                        "s4": {
                          
                        },
                        "s6": {
                          
                        },
                        "s7": {
                          
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
                      
                      "items": {}
                    }
                  },
                  "required": [
                    "is_target_blank",
                    "title",
                    "alias",
                    "preview",
                    "dt_published",
                    "article_edition_id",
                    "original_entity_id",
                    "video_edition_id",
                    "is_prime",
                    "extra_query_params",
                    "media_type",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "properties": {
                    "article_type_id": {
                      
                    },
                    "edp": {
                      
                      "properties": {
                        "title": {
                          
                        },
                        "article_type_edition_id": {
                          
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
                  
                  "items": {}
                },
                "co_author": {
                  
                  "items": {}
                },
                "race_type": {
                  
                  "properties": {
                    "race_type_id": {
                      
                    },
                    "edp": {
                      
                      "properties": {
                        "race_type_edition_id": {
                          
                        },
                        "edition_id": {
                          
                        },
                        "race_type_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "edition_id",
                        "race_type_id",
                        "title",
                        "alias"
                      ]
                    },
                    "category_edition": {
                      
                      "items": {}
                    },
                    "photos": {
                      
                      "items": {}
                    },
                    "race_type_photos": {
                      
                      "items": {}
                    },
                    "canonical": {
                      
                      "items": {}
                    },
                    "alternatives": {
                      
                      "items": {}
                    },
                    "default_duration": {
                      
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
                  
                  "items": {}
                },
                "gallery": {
                  
                  "items": {}
                },
                "drivers": {
                  
                  "items": {}
                },
                "teams": {
                  
                  "items": {}
                },
                "topics": {
                  
                  "items": {}
                },
                "alternatives": {
                  
                  "items": {}
                },
                "next_entity": {
                  
                },
                "pre_entity": {
                  
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
            "share_link": {
              
            }
          },
          "required": [
            "entity_type",
            "slot",
            "promote_type",
            "entity",
            "share_link"
          ]
        }
      ]
    }
  },
  "required": [
    "data"
  ]
}

