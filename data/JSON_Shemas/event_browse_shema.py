

EVENT_BROWSE_SHEMA = {
  "properties": {
    "data": {
      
      "properties": {
        "entity": {
          
          "items": [
            {
              
              "properties": {
                "edp": {
                  
                  "properties": {
                    "dt_created": {
                      
                    },
                    "event_edition_id": {
                      
                    },
                    "title": {
                      
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
                    "dt_created",
                    "event_edition_id",
                    "title",
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
                  
                  "items": {}
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
                            "title": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "sub_event_id",
                            "sub_event_edition_id",
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
                    }
                  ]
                },
                "share_link": {
                  
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
                "sub_event",
                "share_link"
              ]
            },
            {
              
              "properties": {
                "edp": {
                  
                  "properties": {
                    "dt_created": {
                      
                    },
                    "event_edition_id": {
                      
                    },
                    "title": {
                      
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
                    "dt_created",
                    "event_edition_id",
                    "title",
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
                  
                  "items": {}
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
                            "title": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "sub_event_id",
                            "sub_event_edition_id",
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
                            "title": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "sub_event_id",
                            "sub_event_edition_id",
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
                    }
                  ]
                },
                "share_link": {
                  
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
                "sub_event",
                "share_link"
              ]
            }
          ]
        },
        "alphabet": {
          
          "items": {}
        },
        "entity_count": {
          
        },
        "first_letter": {
          
        },
        "years_list": {
          
        },
        "last_photo": {
          
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
                    "alias": {
                      
                    },
                    "photo_edition_id": {
                      
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
                    "alias",
                    "photo_edition_id",
                    "photos"
                  ]
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
                          
                        },
                        "edition_id": {
                          
                        }
                      },
                      "required": [
                        "alias",
                        "race_type_edition_id",
                        "edition_id"
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
                  
                  "items": {}
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
        "all_photo_count": {
          
        },
        "collections": {
          
          "items": {}
        },
        "crash_last_photo": {
          
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
                "alias": {
                  
                },
                "photo_edition_id": {
                  
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
                "alias",
                "photo_edition_id",
                "photos"
              ]
            },
            "race_type": {
              
              "items": {}
            },
            "author": {
              
              "items": {}
            },
            "event": {
              
              "items": {}
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
        },
        "crash_photo_count": {
          
        }
      },
      "required": [
        "entity",
        "alphabet",
        "entity_count",
        "first_letter",
        "years_list",
        "last_photo",
        "all_photo_count",
        "collections",
        "crash_last_photo",
        "crash_photo_count"
      ]
    }
  },
  "required": [
    "data"
  ]
}

