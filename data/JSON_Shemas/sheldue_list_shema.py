SHELDUE_LIST_SHEMA = {
  "items": [
    {
      
      "properties": {
        "edp": {
          
          "properties": {
            "title": {
              
            },
            "alias": {
              
            },
            "event_edition_id": {
              
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
            "title",
            "alias",
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
                    "race_type_edition_id": {
                      
                    },
                    "alias": {
                      
                    },
                    "title": {
                      
                    }
                  },
                  "required": [
                    "race_type_edition_id",
                    "alias",
                    "title"
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
                "race_type_edition_id": {
                  
                },
                "alias": {
                  
                },
                "title": {
                  
                }
              },
              "required": [
                "race_type_edition_id",
                "alias",
                "title"
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
        "location": {
          
          "items": {}
        },
        "country": {
          
          "properties": {
            "code": {
              
            }
          },
          "required": [
            "code"
          ]
        },
        "sub_event": {
          
          "items": [
            {
              
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
                    "sub_event_id": {
                      
                    },
                    "sub_event_edition_id": {
                      
                    },
                    "is_featured": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    }
                  },
                  "required": [
                    "sub_event_id",
                    "sub_event_edition_id",
                    "is_featured",
                    "title",
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
                      
                      "properties": {
                        "alias": {
                          
                        },
                        "race_type_edition_id": {
                          
                        }
                      },
                      "required": [
                        "alias",
                        "race_type_edition_id"
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
                "sub_event_id",
                "dt_from",
                "dt_to",
                "is_featured",
                "sub_event_type",
                "edp",
                "live_text",
                "timezone",
                "race_type"
              ]
            }
          ]
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
    }
  ]
}

