VIDEO_DETAIL_SHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  
  "properties": {
    "video_id": {
      
    },
    "duration": {
      
    },
    "is_prime": {
      "type": "boolean"
    },
    "embed": {
      
    },
    "embed_meta": {
      
    },
    "source": {
      
    },
    "edp": {
      
      "properties": {
        "title": {
          
        },
        "dt_created": {
          
        },
        "video_edition_id": {
          
        },
        "original_entity_id": {
          
        },
        "creator_user_id": {
          
        },
        "edition_id": {
          
        },
        "activity": {
          
        },
        "description": {
          
        },
        "alias": {
          
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
              
            }
          },
          "required": [
            "s1",
            "s2",
            "s3",
            "s4",
            "s5",
            "s6"
          ]
        }
      },
      "required": [
        "title",
        "dt_created",
        "video_edition_id",
        "original_entity_id",
        "creator_user_id",
        "edition_id",
        "activity",
        "description",
        "alias",
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
    "drivers": {
      
      "items": {}
    },
    "teams": {
      
      "items": {}
    },
    "event": {
      
      "properties": {
        "edp": {
          
          "properties": {
            "title": {
              
            },
            "alias": {
              
            },
            "event_edition_id": {
              
            },
            "store_link": {
              
            },
            "photos": {
              
              "items": {}
            }
          },
          "required": [
            "title",
            "alias",
            "event_edition_id",
            "store_link",
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
        
        "creator_user_id": {
          
        },
        "has_race_sub_events": {
          
        },
        "localtime": {
          
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
        
        "creator_user_id",
        "has_race_sub_events",
        "localtime",
        
        "alternatives",
        "championship",
        "race_type",
        "location",
        "country",
        "sub_event"
      ]
    },
    "sub_event": {
      
      "properties": {
        "sub_event_id": {
          
        },
        "dt_from": {
          
        },
        "dt_to": {
          
        },
        "is_featured": {
          
        },
        "sub_event_type": {
          
        },
        "edp": {
          
          "properties": {
            "title": {
              
            },
            "sub_event_edition_id": {
              
            },
            "alias": {
              
            }
          },
          "required": [
            "title",
            "sub_event_edition_id",
            "alias"
          ]
        },
        "live_text": {
          
          "items": {}
        },
        "timezone": {
          
          "items": {}
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
        "event": {
          
          "properties": {
            "edp": {
              
              "properties": {
                "photos": {
                  
                  "items": {}
                }
              },
              "required": [
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
            
            "creator_user_id",
            "has_race_sub_events",
            "localtime",
           
          ]
        }
      },
      "required": [
        "sub_event_id",
        "dt_from",
        "dt_to",
        "is_featured",
        "sub_event_type",
        "edp",
        "live_text",
        "timezone",
        "race_type",
        "event"
      ]
    },
    "video_url": {
      
    },
    "video_type": {
      
    }
  },
  "required": [
    "video_id",
    "duration",
    "is_prime",
    "embed",
    "embed_meta",
    "source",
    "edp",
    "race_type",
    "drivers",
    "teams",
    "event",
    "sub_event",
    "video_url",
    "video_type"
  ]
}

