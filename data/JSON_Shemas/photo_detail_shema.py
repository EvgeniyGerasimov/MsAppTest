PHOTO_DETAIL_SHEMA = {
  
  "properties": {
    "data": {
      
      "properties": {
        "photo": {
          
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
                    "title": {
                      
                    },
                    "photo_edition_id": {
                      
                    },
                    "edition_id": {
                      
                    },
                    "alias": {
                      
                    },
                    "description": {
                      
                    },
                    "dt_created": {
                      
                    },
                    "original_entity_id": {
                      
                    },
                    "creator_user_id": {
                      
                    },
                    "tags": {
                      
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
                    "photo_edition_id",
                    "edition_id",
                    "alias",
                    "description",
                    "dt_created",
                    "original_entity_id",
                    "creator_user_id",
                    "tags",
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
                        "alias": {
                          
                        },
                        "race_type_edition_id": {
                          
                        }
                      },
                      "required": [
                        "title",
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
                },
                "author": {
                  
                  "properties": {
                    "author_id": {
                      
                    },
                    "edp": {
                      
                      "properties": {
                        "first_name": {
                          
                        },
                        "last_name": {
                          
                        },
                        "author_edition_id": {
                          
                        }
                      },
                      "required": [
                        "first_name",
                        "last_name",
                        "author_edition_id"
                      ]
                    },
                    "avatar": {
                      
                      "items": {}
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
                "event": {
                  
                  "properties": {
                    "edp": {
                      
                      "properties": {
                        "title": {
                          
                        },
                        "event_edition_id": {
                          
                        },
                        "store_link": {
                          
                        },
                        "alias": {
                          
                        },
                        "photos": {
                          
                          "items": {}
                        }
                      },
                      "required": [
                        "title",
                        "event_edition_id",
                        "store_link",
                        "alias",
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
                          
                          "properties": {
                            "alias": {
                              
                            }
                          },
                          "required": [
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
                            "alias": {
                              
                            },
                            "photos": {
                              
                              "items": {}
                            }
                          },
                          "required": [
                            "alias",
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
                        "localtime"
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
                "location": {
                  
                  "properties": {
                    "location_id": {
                      
                    },
                    "location_type": {
                      
                    },
                    "lat": {
                      
                    },
                    "lng": {
                      
                    },
                    "has_article": {
                      
                    },
                    "has_photo": {
                      
                    },
                    "has_video": {
                      
                    },
                    "alternatives": {
                      
                      "items": {}
                    },
                    "canonical": {
                      
                      "items": {}
                    },
                    "edp": {
                      
                      "properties": {
                        "title": {
                          
                        },
                        "location_edition_id": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "title",
                        "location_edition_id",
                        "alias"
                      ]
                    },
                    "country": {
                      
                      "items": {}
                    }
                  },
                  "required": [
                    "location_id",
                    "location_type",
                    "lat",
                    "lng",
                    "has_article",
                    "has_photo",
                    "has_video",
                    "alternatives",
                    "canonical",
                    "edp",
                    "country"
                  ]
                },
                "teams": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "team_id": {
                          
                        },
                        "store_link": {
                          
                        },
                        "photo": {
                          
                          "items": {}
                        },
                        "edp": {
                          
                          "properties": {
                            "title": {
                              
                            },
                            "team_edition_id": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "title",
                            "team_edition_id",
                            "alias"
                          ]
                        },
                        "has_article": {
                          
                        },
                        "has_photo": {
                          
                        },
                        "has_video": {
                          
                        },
                        "country": {
                          
                          "items": {}
                        },
                        "alternatives": {
                          
                          "items": {}
                        },
                        "canonical": {
                          
                          "items": {}
                        },
                        "drivers": {
                          
                          "items": {}
                        }
                      },
                      "required": [
                        "team_id",
                        "store_link",
                        "photo",
                        "edp",
                        "has_article",
                        "has_photo",
                        "has_video",
                        "country",
                        "alternatives",
                        "canonical",
                        "drivers"
                      ]
                    }
                  ]
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "birthdate": {
                          
                        },
                        "number": {
                          
                        },
                        "driver_type": {
                          
                        },
                        "store_link": {
                          
                        },
                        "edp": {
                          
                          "properties": {
                            "store_link": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            },
                            "driver_edition_id": {
                              
                            }
                          },
                          "required": [
                            "store_link",
                            "first_name",
                            "last_name",
                            "alias",
                            "driver_edition_id"
                          ]
                        },
                        "photo": {
                          
                          "items": {}
                        },
                        "team": {
                          
                        },
                        "has_article": {
                          
                        },
                        "has_photo": {
                          
                        },
                        "has_video": {
                          
                        },
                        "country": {
                          
                          "items": {}
                        },
                        "alternatives": {
                          
                          "items": {}
                        },
                        "canonical": {
                          
                          "items": {}
                        }
                      },
                      "required": [
                        "driver_id",
                        "birthdate",
                        "number",
                        "driver_type",
                        "store_link",
                        "edp",
                        "photo",
                        "team",
                        "has_article",
                        "has_photo",
                        "has_video",
                        "country",
                        "alternatives",
                        "canonical"
                      ]
                    }
                  ]
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
                "drivers"
              ]
            }
          ]
        },
        "nextPhoto": {
          
          "items": {}
        },
        "prePhoto": {
          
          "items": {}
        }
      },
      "required": [
        "photo",
        "nextPhoto",
        "prePhoto"
      ]
    }
  },
  "required": [
    "data"
  ]
}

