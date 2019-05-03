PROMOTION_FEATURE_STRIP_SHEMA = {
  "properties": {
    "data": {
      
      "items": [
        {
          
          "properties": {
            "promote_id": {
              
            },
            "edition_id": {
              
            },
            "entity_id": {
              
            },
            "photo_edition_id": {
              
            },
            "entity_type": {
              
            },
            "title": {
              
            },
            "header": {
              
            },
            "description": {
              
            },
            "slot": {
              
            },
            "href": {
              
            },
            "promote_type": {
              
            },
            "dt_created": {
              
            },
            "entity": {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "preview": {
                      
                    },
                    "article_edition_id": {
                      
                    },
                    "dt_published": {
                      
                    },
                    "original_entity_id": {
                      
                    },
                    "is_target_blank": {
                      
                    },
                    "is_prime": {
                      
                    },
                    "video_edition_id": {
                      
                    },
                    "dt_created": {
                      
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
                    "title",
                    "alias",
                    "preview",
                    "article_edition_id",
                    "dt_published",
                    "original_entity_id",
                    "is_target_blank",
                    "is_prime",
                    "video_edition_id",
                    "dt_created",
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
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "title",
                        "alias"
                      ]
                    },
                    "category_edition": {
                      
                      "items": {}
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
                        "s5": {
                          
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
            }
          },
          "required": [
            "promote_id",
            "edition_id",
            "entity_id",
            "photo_edition_id",
            "entity_type",
            "title",
            "header",
            "description",
            "slot",
            "href",
            "promote_type",
            "dt_created",
            "entity"
          ]
        }
      ]
    }
  },
  "required": [
    "data"
  ]
}

