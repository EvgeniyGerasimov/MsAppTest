PROMOTION_AUTHOR_TOOL = {
  "properties": {
    "data": {
      
      "items": [
        {
          
          "properties": {
            "author_tool_id": {
              
            },
            "slot": {
              
            },
            "article": {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "is_target_blank": {
                      
                    },
                    "title": {
                      
                    },
                    "dt_published": {
                      
                    },
                    "alias": {
                      
                    },
                    "original_entity_id": {
                      
                    },
                    "article_edition_id": {
                      
                    },
                    "video_edition_id": {
                      
                    },
                    "media_type": {
                      
                    },
                    "is_prime": {
                      
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
                    "dt_published",
                    "alias",
                    "original_entity_id",
                    "article_edition_id",
                    "video_edition_id",
                    "media_type",
                    "is_prime",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "items": {}
                },
                "author": {
                  
                  "properties": {
                    "author_id": {
                      
                    },
                    "edp": {
                      
                      "properties": {
                        "author_id": {
                          
                        },
                        "first_name": {
                          
                        },
                        "author_edition_id": {
                          
                        },
                        "last_name": {
                          
                        }
                      },
                      "required": [
                        "author_id",
                        "first_name",
                        "author_edition_id",
                        "last_name"
                      ]
                    },
                    "avatar": {
                      
                      "properties": {
                        "s1": {
                          
                        },
                        "s2": {
                          
                        }
                      },
                      "required": [
                        "s1",
                        "s2"
                      ]
                    },
                    "user": {
                      
                      "items": {}
                    },
                    "articles": {
                      
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
                        "race_type_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
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
            },
            "share_link": {
              
            }
          },
          "required": [
            "author_tool_id",
            "slot",
            "article",
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

