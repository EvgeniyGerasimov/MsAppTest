PHOTOS_BROWSE_SHEMA ={
 
  
  "properties": {
    "data": {
      
      "properties": {
        "photos": {
          
          "items": [
            {
              
              "properties": {
                "photo_id": {
                  
                },
                "is_stuff": {
                  
                },
                "ratio": {
                  
                },
                "is_prime": {
                  "type": "boolean"
                },
                "next_photo_id": {
                  
                },
                "preview_photo_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "photo_edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "dt_created": {
                      
                    },
                    "alias": {
                      
                    },
                    "original_entity_id": {
                      
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
                          
                        },
                        "s6": {
                          
                        },
                        "s7": {
                          
                        },
                        "s8": {
                          
                        },
                        "s9": {
                          
                        },
                        "sp1": {
                          
                        },
                        "sp2": {
                          
                        },
                        "sp8": {
                          
                        }
                      },
                      "required": [
                        "s1",
                        "s2",
                        "s3",
                        "s4",
                        "s5",
                        "s6",
                        "s7",
                        "s8",
                        "s9",
                        "sp1",
                        "sp2",
                        "sp8"
                      ]
                    }
                  },
                  "required": [
                    "photo_edition_id",
                    "title",
                    "dt_created",
                    "alias",
                    "original_entity_id",
                    "photos"
                  ]
                },
                "race_type": {
                  
                  "properties": {
                    "race_type_id": {
                      
                    },
                    "edp": {
                      
                      "properties": {
                        "title": {
                          
                        },
                        "race_type_edition_id": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "title",
                        "race_type_edition_id",
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
                "author": {
                  
                  "items": {}
                },
                "event": {
                  
                  "properties": {
                    "edp": {
                      
                      "properties": {
                        "alias": {
                          
                        },
                        "title": {
                          
                        },
                        "event_edition_id": {
                          
                        },
                        "photos": {
                          
                          "items": {}
                        }
                      },
                      "required": [
                        "alias",
                        "title",
                        "event_edition_id",
                        "photos"
                      ]
                    },
                    "event_id": {
                      
                    },
                    "origin_data_from": {
                      
                    },
                    "count_photos": {
                      
                    },
                    "month": {
                      
                    },
                    "number": {
                      
                    },
                    "event_type": {
                      
                    },
                    "has_articles": {
                      
                    },
                    "has_photos": {
                      
                    },
                    "has_videos": {
                      
                    },
                    "dt_from": {
                      
                    },
                    "dt_to": {
                      
                    },
                    "tickets_url": {
                      
                    },
                    "store_link": {
                      
                    },
                    "has_results": {
                      
                    },
                    "result_race_id": {
                      
                    },
                    "creator_user_id": {
                      
                    },
                    "has_race_sub_events": {
                      
                    },
                    "localtime": {
                      
                    },
                    "position": {
                      
                    },
                    "alternatives": {
                      
                      "items": {}
                    },
                    "championship": {
                      
                      "properties": {
                        "championship_id": {
                          
                        },
                        "race_type_id": {
                          
                        },
                        "year": {
                          
                        },
                        "title_year": {
                          
                        },
                        "race_type": {
                          
                          "items": {}
                        }
                      },
                      "required": [
                        "championship_id",
                        "race_type_id",
                        "year",
                        "title_year",
                        "race_type"
                      ]
                    },
                    "race_type": {
                      
                      "properties": {
                        "race_type_id": {
                          
                        },
                        "edp": {
                          
                          "items": {}
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
                    "location": {
                      
                      "items": {}
                    },
                    "country": {
                      
                      "items": {}
                    },
                    "sub_event": {
                      
                      "items": {}
                    }
                  },
                  "required": [
                    "edp",
                    "event_id",
                    "origin_data_from",
                    "count_photos",
                    "month",
                    "number",
                    "event_type",
                    "has_articles",
                    "has_photos",
                    "has_videos",
                    "dt_from",
                    "dt_to",
                    "tickets_url",
                    "store_link",
                    "has_results",
                    "result_race_id",
                    "creator_user_id",
                    "has_race_sub_events",
                    "localtime",
                    "position",
                    "alternatives",
                    "championship",
                    "race_type",
                    "location",
                    "country",
                    "sub_event"
                  ]
                },
                "sub_event": {
                  
                  "items": {}
                },
                "location": {
                  
                  "items": {}
                },
                "teams": {
                  
                  "items": {}
                },
                "drivers": {
                  
                  "items": {}
                },
                "share_link": {
                  
                }
              },
              "required": [
                "photo_id",
                "is_stuff",
                "ratio",
                "is_prime",
                "next_photo_id",
                "preview_photo_id",
                "edp",
                "race_type",
                "author",
                "event",
                "sub_event",
                "location",
                "teams",
                "drivers",
                "share_link"
              ]
            }
          ]
        },
        "photos_count": {
          
        }
      },
      "required": [
        "photos",
        "photos_count"
      ]
    }
  },
  "required": [
    "data"
  ]
}

