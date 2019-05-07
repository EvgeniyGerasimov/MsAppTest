RESULT_DETAIL_SHEMA_PROD = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  
  "properties": {
    "data": {
      
      "properties": {
        "extra_table_data": {
          
          "properties": {
            "fields": {
              
              "items": [
                {
                  
                  "properties": {
                    "title": {
                      
                    },
                    "field": {
                      
                    },
                    "type": {
                      
                    },
                    "list": {
                      
                    }
                  },
                  "required": [
                    "title",
                    "field",
                    "type",
                    "list"
                  ]
                },
                {
                  
                  "properties": {
                    "title": {
                      
                    },
                    "field": {
                      
                    },
                    "type": {
                      
                    }
                  },
                  "required": [
                    "title",
                    "field",
                    "type"
                  ]
                },
                {
                  
                  "properties": {
                    "title": {
                      
                    },
                    "field": {
                      
                    }
                  },
                  "required": [
                    "title",
                    "field"
                  ]
                },
                {
                  
                  "properties": {
                    "title": {
                      
                    },
                    "field": {
                      
                    }
                  },
                  "required": [
                    "title",
                    "field"
                  ]
                },
                {
                  
                  "properties": {
                    "title": {
                      
                    },
                    "field": {
                      
                    }
                  },
                  "required": [
                    "title",
                    "field"
                  ]
                },
                {
                  
                  "properties": {
                    "title": {
                      
                    },
                    "field": {
                      
                    }
                  },
                  "required": [
                    "title",
                    "field"
                  ]
                },
                {
                  
                  "properties": {
                    "title": {
                      
                    },
                    "field": {
                      
                    }
                  },
                  "required": [
                    "title",
                    "field"
                  ]
                },
                {
                  
                  "properties": {
                    "title": {
                      
                    },
                    "field": {
                      
                    }
                  },
                  "required": [
                    "title",
                    "field"
                  ]
                },
                {
                  
                  "properties": {
                    "title": {
                      
                    },
                    "field": {
                      
                    }
                  },
                  "required": [
                    "title",
                    "field"
                  ]
                },
                {
                  
                  "properties": {
                    "title": {
                      
                    },
                    "field": {
                      
                    }
                  },
                  "required": [
                    "title",
                    "field"
                  ]
                },
                {
                  
                  "properties": {
                    "title": {
                      
                    },
                    "field": {
                      
                    }
                  },
                  "required": [
                    "title",
                    "field"
                  ]
                },
                {
                  
                  "properties": {
                    "title": {
                      
                    },
                    "field": {
                      
                    }
                  },
                  "required": [
                    "title",
                    "field"
                  ]
                }
              ]
            }
          },
          "required": [
            "fields"
          ]
        },
        "current_championship": {
          
          "properties": {
            "championship_id": {
              
            },
            "year": {
              
            },
            "dt_from": {
              
            },
            "dt_to": {
              
            },
            "race_type_id": {
              
            },
            "race_type": {
              
              "properties": {
                "race_type_id": {
                  
                },
                "result_series": {
                  
                },
                "title": {
                  
                },
                "show_range_years": {
                  
                },
                "race_type_edition": {
                  
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
                }
              },
              "required": [
                "race_type_id",
                "result_series",
                "title",
                "show_range_years",
                "race_type_edition"
              ]
            }
          },
          "required": [
            "championship_id",
            "year",
            "dt_from",
            "dt_to",
            "race_type_id",
            "race_type"
          ]
        },
        "current_session_type": {
          
        },
        "current_event": {
          
          "properties": {
            "event_id": {
              
            },
            "event_edition_id": {
              
            },
            "title": {
              
            },
            "alias": {
              
            },
            "result_race_id": {
              
            },
            "dt_start": {
              
            },
            "dt_end": {
              
            },
            "country_id": {
              
            },
            "flag": {
              
            },
            "lang": {
              
            },
            "location_id": {
              
            },
            "event_title": {
              
            },
            "event_alias": {
              
            },
            "country_code": {
              
            },
            "country_title": {
              
            },
            "small_flag": {
              
            },
            "has_content": {
              
            },
            "event_edition": {
              
              "properties": {
                "event_id": {
                  
                },
                "event_edition_id": {
                  
                },
                "title": {
                  
                },
                "alias": {
                  
                },
                "result_race_id": {
                  
                },
                "dt_start": {
                  
                },
                "dt_end": {
                  
                },
                "country_id": {
                  
                },
                "flag": {
                  
                },
                "lang": {
                  
                },
                "location_id": {
                  
                },
                "event_title": {
                  
                },
                "event_alias": {
                  
                },
                "country_code": {
                  
                },
                "country_title": {
                  
                },
                "small_flag": {
                  
                },
                "has_content": {
                  
                }
              },
              "required": [
                "event_id",
                "event_edition_id",
                "title",
                "alias",
                "result_race_id",
                "dt_start",
                "dt_end",
                "country_id",
                
                
                "location_id",
                "event_title",
                "event_alias",
                
                
                
                "has_content"
              ]
            },
            "country": {

              "properties": {
                "country_id": {

                },
                "title": {

                },
                "code": {

                },
                "url": {

                }
              },
              "required": [
                "country_id",
                "title",
                "code",
                "url"
              ]
            }
          },
          "required": [
            "event_id",
            "event_edition_id",
            "title",
            "alias",
            "result_race_id",
            "dt_start",
            "dt_end",
            "country_id",
            
            
            "location_id",
            "event_title",
            "event_alias",
            
            
            
            "has_content",
            "event_edition",
            "country"
          ]
        },
        "years": {

          "items": [
            {

              "properties": {
                "title": {

                },
                "value": {

                }
              },
              "required": [
                "title",
                "value"
              ]
            },
            {

              "properties": {
                "title": {

                },
                "value": {

                }
              },
              "required": [
                "title",
                "value"
              ]
            },
            {

              "properties": {
                "title": {

                },
                "value": {

                }
              },
              "required": [
                "title",
                "value"
              ]
            },
            {

              "properties": {
                "title": {

                },
                "value": {

                }
              },
              "required": [
                "title",
                "value"
              ]
            },
            {

              "properties": {
                "title": {

                },
                "value": {

                }
              },
              "required": [
                "title",
                "value"
              ]
            }
          ]
        },
        "events": {

          "items": [
            {

              "properties": {
                "event_id": {

                },
                "event_edition_id": {

                },
                "title": {

                },
                "alias": {

                },
                "result_race_id": {

                },
                "dt_start": {

                },
                "dt_end": {

                },
                "country_id": {

                },
                "flag": {

                },
                "lang": {

                },
                "location_id": {

                },
                "event_title": {

                },
                "event_alias": {

                },
                "country_code": {

                },
                "country_title": {

                },
                "small_flag": {

                },
                "has_content": {

                },
                "event_edition": {

                  "properties": {
                    "event_id": {

                    },
                    "event_edition_id": {

                    },
                    "title": {

                    },
                    "alias": {

                    },
                    "result_race_id": {

                    },
                    "dt_start": {

                    },
                    "dt_end": {

                    },
                    "country_id": {

                    },
                    "flag": {

                    },
                    "lang": {

                    },
                    "location_id": {

                    },
                    "event_title": {

                    },
                    "event_alias": {

                    },
                    "country_code": {

                    },
                    "country_title": {

                    },
                    "small_flag": {

                    },
                    "has_content": {

                    }
                  },
                  "required": [
                    "event_id",
                    "event_edition_id",
                    "title",
                    "alias",
                    "result_race_id",
                    "dt_start",
                    "dt_end",
                    "country_id",
                    
                    
                    "location_id",
                    "event_title",
                    "event_alias",
                    
                    
                    
                    "has_content"
                  ]
                },
                "country": {

                  "properties": {
                    "country_id": {

                    },
                    "title": {

                    },
                    "code": {

                    },
                    "url": {

                    }
                  },
                  "required": [
                    "country_id",
                    "title",
                    "code",
                    "url"
                  ]
                }
              },
              "required": [
                "event_id",
                "event_edition_id",
                "title",
                "alias",
                "result_race_id",
                "dt_start",
                "dt_end",
                "country_id",
                
                
                "location_id",
                "event_title",
                "event_alias",
                
                
                
                "has_content",
                "event_edition",
                "country"
              ]
            },
            {

              "properties": {
                "event_id": {

                },
                "event_edition_id": {

                },
                "title": {

                },
                "alias": {

                },
                "result_race_id": {

                },
                "dt_start": {

                },
                "dt_end": {

                },
                "country_id": {

                },
                "flag": {

                },
                "lang": {

                },
                "location_id": {

                },
                "event_title": {

                },
                "event_alias": {

                },
                "country_code": {

                },
                "country_title": {

                },
                "small_flag": {

                },
                "has_content": {

                },
                "event_edition": {

                  "properties": {
                    "event_id": {

                    },
                    "event_edition_id": {

                    },
                    "title": {

                    },
                    "alias": {

                    },
                    "result_race_id": {

                    },
                    "dt_start": {

                    },
                    "dt_end": {

                    },
                    "country_id": {

                    },
                    "flag": {

                    },
                    "lang": {

                    },
                    "location_id": {

                    },
                    "event_title": {

                    },
                    "event_alias": {

                    },
                    "country_code": {

                    },
                    "country_title": {

                    },
                    "small_flag": {

                    },
                    "has_content": {

                    }
                  },
                  "required": [
                    "event_id",
                    "event_edition_id",
                    "title",
                    "alias",
                    "result_race_id",
                    "dt_start",
                    "dt_end",
                    "country_id",
                    
                    
                    "location_id",
                    "event_title",
                    "event_alias",
                    
                    
                    
                    "has_content"
                  ]
                },
                "country": {

                  "properties": {
                    "country_id": {

                    },
                    "title": {

                    },
                    "code": {

                    },
                    "url": {

                    }
                  },
                  "required": [
                    "country_id",
                    "title",
                    "code",
                    "url"
                  ]
                }
              },
              "required": [
                "event_id",
                "event_edition_id",
                "title",
                "alias",
                "result_race_id",
                "dt_start",
                "dt_end",
                "country_id",
                
                
                "location_id",
                "event_title",
                "event_alias",
                
                
                
                "has_content",
                "event_edition",
                "country"
              ]
            },
            {

              "properties": {
                "event_id": {

                },
                "event_edition_id": {

                },
                "title": {

                },
                "alias": {

                },
                "result_race_id": {

                },
                "dt_start": {

                },
                "dt_end": {

                },
                "country_id": {

                },
                "flag": {

                },
                "lang": {

                },
                "location_id": {

                },
                "event_title": {

                },
                "event_alias": {

                },
                "country_code": {

                },
                "country_title": {

                },
                "small_flag": {

                },
                "has_content": {

                },
                "event_edition": {

                  "properties": {
                    "event_id": {

                    },
                    "event_edition_id": {

                    },
                    "title": {

                    },
                    "alias": {

                    },
                    "result_race_id": {

                    },
                    "dt_start": {

                    },
                    "dt_end": {

                    },
                    "country_id": {

                    },
                    "flag": {

                    },
                    "lang": {

                    },
                    "location_id": {

                    },
                    "event_title": {

                    },
                    "event_alias": {

                    },
                    "country_code": {

                    },
                    "country_title": {

                    },
                    "small_flag": {

                    },
                    "has_content": {

                    }
                  },
                  "required": [
                    "event_id",
                    "event_edition_id",
                    "title",
                    "alias",
                    "result_race_id",
                    "dt_start",
                    "dt_end",
                    "country_id",
                    
                    
                    "location_id",
                    "event_title",
                    "event_alias",
                    
                    
                    
                    "has_content"
                  ]
                },
                "country": {

                  "properties": {
                    "country_id": {

                    },
                    "title": {

                    },
                    "code": {

                    },
                    "url": {

                    }
                  },
                  "required": [
                    "country_id",
                    "title",
                    "code",
                    "url"
                  ]
                }
              },
              "required": [
                "event_id",
                "event_edition_id",
                "title",
                "alias",
                "result_race_id",
                "dt_start",
                "dt_end",
                "country_id",
                
                
                "location_id",
                "event_title",
                "event_alias",
                
                
                
                "has_content",
                "event_edition",
                "country"
              ]
            },
            {

              "properties": {
                "event_id": {

                },
                "event_edition_id": {

                },
                "title": {

                },
                "alias": {

                },
                "result_race_id": {

                },
                "dt_start": {

                },
                "dt_end": {

                },
                "country_id": {

                },
                "flag": {

                },
                "lang": {

                },
                "location_id": {

                },
                "event_title": {

                },
                "event_alias": {

                },
                "country_code": {

                },
                "country_title": {

                },
                "small_flag": {

                },
                "has_content": {

                },
                "event_edition": {

                  "properties": {
                    "event_id": {

                    },
                    "event_edition_id": {

                    },
                    "title": {

                    },
                    "alias": {

                    },
                    "result_race_id": {

                    },
                    "dt_start": {

                    },
                    "dt_end": {

                    },
                    "country_id": {

                    },
                    "flag": {

                    },
                    "lang": {

                    },
                    "location_id": {

                    },
                    "event_title": {

                    },
                    "event_alias": {

                    },
                    "country_code": {

                    },
                    "country_title": {

                    },
                    "small_flag": {

                    },
                    "has_content": {

                    }
                  },
                  "required": [
                    "event_id",
                    "event_edition_id",
                    "title",
                    "alias",
                    "result_race_id",
                    "dt_start",
                    "dt_end",
                    "country_id",
                    
                    
                    "location_id",
                    "event_title",
                    "event_alias",
                    
                    
                    
                    "has_content"
                  ]
                },
                "country": {

                  "properties": {
                    "country_id": {

                    },
                    "title": {

                    },
                    "code": {

                    },
                    "url": {

                    }
                  },
                  "required": [
                    "country_id",
                    "title",
                    "code",
                    "url"
                  ]
                }
              },
              "required": [
                "event_id",
                "event_edition_id",
                "title",
                "alias",
                "result_race_id",
                "dt_start",
                "dt_end",
                "country_id",
                
                
                "location_id",
                "event_title",
                "event_alias",
                
                
                
                "has_content",
                "event_edition",
                "country"
              ]
            },
            {

              "properties": {
                "event_id": {

                },
                "event_edition_id": {

                },
                "title": {

                },
                "alias": {

                },
                "result_race_id": {

                },
                "dt_start": {

                },
                "dt_end": {

                },
                "country_id": {

                },
                "flag": {

                },
                "lang": {

                },
                "location_id": {

                },
                "event_title": {

                },
                "event_alias": {

                },
                "country_code": {

                },
                "country_title": {

                },
                "small_flag": {

                },
                "has_content": {

                },
                "event_edition": {

                  "properties": {
                    "event_id": {

                    },
                    "event_edition_id": {

                    },
                    "title": {

                    },
                    "alias": {

                    },
                    "result_race_id": {

                    },
                    "dt_start": {

                    },
                    "dt_end": {

                    },
                    "country_id": {

                    },
                    "flag": {

                    },
                    "lang": {

                    },
                    "location_id": {

                    },
                    "event_title": {

                    },
                    "event_alias": {

                    },
                    "country_code": {

                    },
                    "country_title": {

                    },
                    "small_flag": {

                    },
                    "has_content": {

                    }
                  },
                  "required": [
                    "event_id",
                    "event_edition_id",
                    "title",
                    "alias",
                    "result_race_id",
                    "dt_start",
                    "dt_end",
                    "country_id",
                    
                    
                    "location_id",
                    "event_title",
                    "event_alias",
                    
                    
                    
                    "has_content"
                  ]
                },
                "country": {

                  "properties": {
                    "country_id": {

                    },
                    "title": {

                    },
                    "code": {

                    },
                    "url": {

                    }
                  },
                  "required": [
                    "country_id",
                    "title",
                    "code",
                    "url"
                  ]
                }
              },
              "required": [
                "event_id",
                "event_edition_id",
                "title",
                "alias",
                "result_race_id",
                "dt_start",
                "dt_end",
                "country_id",
                
                
                "location_id",
                "event_title",
                "event_alias",
                
                
                
                "has_content",
                "event_edition",
                "country"
              ]
            },
            {

              "properties": {
                "event_id": {

                },
                "event_edition_id": {

                },
                "title": {

                },
                "alias": {

                },
                "result_race_id": {

                },
                "dt_start": {

                },
                "dt_end": {

                },
                "country_id": {

                },
                "flag": {

                },
                "lang": {

                },
                "location_id": {

                },
                "event_title": {

                },
                "event_alias": {

                },
                "country_code": {

                },
                "country_title": {

                },
                "small_flag": {

                },
                "has_content": {

                },
                "event_edition": {

                  "properties": {
                    "event_id": {

                    },
                    "event_edition_id": {

                    },
                    "title": {

                    },
                    "alias": {

                    },
                    "result_race_id": {

                    },
                    "dt_start": {

                    },
                    "dt_end": {

                    },
                    "country_id": {

                    },
                    "flag": {

                    },
                    "lang": {

                    },
                    "location_id": {

                    },
                    "event_title": {

                    },
                    "event_alias": {

                    },
                    "country_code": {

                    },
                    "country_title": {

                    },
                    "small_flag": {

                    },
                    "has_content": {

                    }
                  },
                  "required": [
                    "event_id",
                    "event_edition_id",
                    "title",
                    "alias",
                    "result_race_id",
                    "dt_start",
                    "dt_end",
                    "country_id",
                    
                    
                    "location_id",
                    "event_title",
                    "event_alias",
                    
                    
                    
                    "has_content"
                  ]
                },
                "country": {

                  "properties": {
                    "country_id": {

                    },
                    "title": {

                    },
                    "code": {

                    },
                    "url": {

                    }
                  },
                  "required": [
                    "country_id",
                    "title",
                    "code",
                    "url"
                  ]
                }
              },
              "required": [
                "event_id",
                "event_edition_id",
                "title",
                "alias",
                "result_race_id",
                "dt_start",
                "dt_end",
                "country_id",
                
                
                "location_id",
                "event_title",
                "event_alias",
                
                
                
                "has_content",
                "event_edition",
                "country"
              ]
            }
          ]
        },
        "session_types": {
          
          "items": [
            {
              
              "properties": {
                "title": {
                  
                },
                "session_type": {
                  
                }
              },
              "required": [
                "title",
                "session_type"
              ]
            },
            {
              
              "properties": {
                "title": {
                  
                },
                "session_type": {
                  
                }
              },
              "required": [
                "title",
                "session_type"
              ]
            },
            {
              
              "properties": {
                "title": {
                  
                },
                "session_type": {
                  
                }
              },
              "required": [
                "title",
                "session_type"
              ]
            },
            {
              
              "properties": {
                "title": {
                  
                },
                "session_type": {
                  
                }
              },
              "required": [
                "title",
                "session_type"
              ]
            },
            {
              
              "properties": {
                "title": {
                  
                },
                "session_type": {
                  
                }
              },
              "required": [
                "title",
                "session_type"
              ]
            },
            {
              
              "properties": {
                "title": {
                  
                },
                "session_type": {
                  
                }
              },
              "required": [
                "title",
                "session_type"
              ]
            },
            {
              
              "properties": {
                "title": {
                  
                },
                "session_type": {
                  
                }
              },
              "required": [
                "title",
                "session_type"
              ]
            },
            {
              
              "properties": {
                "title": {
                  
                },
                "session_type": {
                  
                }
              },
              "required": [
                "title",
                "session_type"
              ]
            },
            {
              
              "properties": {
                "title": {
                  
                },
                "session_type": {
                  
                }
              },
              "required": [
                "title",
                "session_type"
              ]
            },
            {
              
              "properties": {
                "title": {
                  
                },
                "session_type": {
                  
                }
              },
              "required": [
                "title",
                "session_type"
              ]
            },
            {
              
              "properties": {
                "title": {
                  
                },
                "session_type": {
                  
                }
              },
              "required": [
                "title",
                "session_type"
              ]
            },
            {
              
              "properties": {
                "title": {
                  
                },
                "session_type": {
                  
                }
              },
              "required": [
                "title",
                "session_type"
              ]
            },
            {
              
              "properties": {
                "title": {
                  
                },
                "session_type": {
                  
                }
              },
              "required": [
                "title",
                "session_type"
              ]
            }
          ]
        },
        "results": {
          
          "items": [
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            },
            {
              
              "properties": {
                "number": {
                  
                },
                "position": {
                  
                },
                "sort_order": {
                  
                },
                "total_points": {
                  
                },
                "time": {
                  
                },
                "car_model": {
                  
                },
                "car_make": {
                  
                },
                "engine_make": {
                  
                },
                "engine_model": {
                  
                },
                "laps": {
                  
                },
                "lap": {
                  
                },
                "laps_led": {
                  
                },
                "gap": {
                  
                },
                "interval": {
                  
                },
                "avg_speed": {
                  
                },
                "speed_trap": {
                  
                },
                "participation": {
                  
                },
                "retirement": {
                  
                },
                "pits": {
                  
                },
                "points": {
                  
                },
                "class": {
                  
                },
                "votes": {
                  
                },
                "max_speed1": {
                  
                },
                "max_speed2": {
                  
                },
                "max_speed3": {
                  
                },
                "tyre_changes": {
                  
                },
                "max_blocks_count": {
                  
                },
                "speed": {
                  
                },
                "tyres": {
                  
                },
                "drivers": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "country": {
                          
                          "properties": {
                            "country_id": {
                              
                            },
                            "code": {
                              
                            },
                            "title": {
                              
                            },
                            "url": {
                              
                            }
                          },
                          "required": [
                            "country_id",
                            "code",
                            "title",
                            "url"
                          ]
                        },
                        "driver_edition": {
                          
                          "properties": {
                            "driver_edition_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            },
                            "alias": {
                              
                            }
                          },
                          "required": [
                            "driver_edition_id",
                            "first_name",
                            "last_name",
                            "alias"
                          ]
                        }
                      },
                      "required": [
                        "driver_id",
                        "country_id",
                        "result_driver_id",
                        "sequence",
                        
                        "driver_edition"
                      ]
                    }
                  ]
                },
                "team": {
                  
                  "properties": {
                    "team_id": {
                      
                    },
                    "country_id": {
                      
                    },
                    "result_team_id": {
                      
                    },
                    "country": {
                      
                      "properties": {
                        "country_id": {
                          
                        },
                        "code": {
                          
                        },
                        "title": {
                          
                        },
                        "url": {
                          
                        }
                      },
                      "required": [
                        "country_id",
                        "code",
                        "title",
                        "url"
                      ]
                    },
                    "team_edition": {
                      
                      "properties": {
                        "team_edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "team_edition_id",
                        "title",
                        "alias"
                      ]
                    }
                  },
                  "required": [
                    "team_id",
                    "country_id",
                    "result_team_id",
                    
                    "team_edition"
                  ]
                }
              },
              "required": [
                "number",
                "position",
                "sort_order",
                "total_points",
                "time",
                "car_model",
                "car_make",
                "engine_make",
                "engine_model",
                "laps",
                "lap",
                "laps_led",
                "gap",
                "interval",
                "avg_speed",
                "speed_trap",
                "participation",
                "retirement",
                "pits",
                "points",
                "class",
                "votes",
                "max_speed1",
                "max_speed2",
                "max_speed3",
                "tyre_changes",
                "max_blocks_count",
                "speed",
                "tyres",
                "drivers",
                "team"
              ]
            }
          ]
        }
      },
      "required": [
        "extra_table_data",
        "current_championship",
        "current_session_type",
        "current_event",
        "years",
        "events",
        "session_types",
        "results"
      ]
    }
  },
  "required": [
    "data"
  ]
}




