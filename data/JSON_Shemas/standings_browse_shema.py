STANDINGS_BROWSE_SHEMA = {
  
  "properties": {
    "data": {
      
      "items": [
        {
          
          "properties": {
            "series": {
              
              "properties": {
                "race_type_id": {
                  
                },
                "result_series": {
                  
                },
                "idhash": {
                  
                },
                "version": {
                  
                },
                "filename": {
                  
                },
                "alias": {
                  
                },
                "title": {
                  
                },
                "race_type": {
                  
                  "properties": {
                    "race_type_id": {
                      
                    },
                    "version": {
                      
                    },
                    "filename": {
                      
                    },
                    "idhash": {
                      
                    },
                    "has_logo": {
                      
                    }
                  },
                  "required": [
                    "race_type_id",
                    "version",
                    "filename",
                    "idhash",
                    "has_logo"
                  ]
                },
                "championship": {
                  
                  "items": {}
                },
                "photo_edition": {
                  
                  "items": {}
                }
              },
              "required": [
                "race_type_id",
                "result_series",
                "idhash",
                "version",
                "filename",
                "alias",
                "title",
                "race_type",
                "championship",
                "photo_edition"
              ]
            },
            "standings": {
              
              "items": [
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "event": {
                      
                      "items": [
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                },
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                },
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        }
                      ]
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "event",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                }
              ]
            },
            "current_standing_type": {
              
            }
          },
          "required": [
            "series",
            "standings",
            "current_standing_type"
          ]
        },
        {
          
          "properties": {
            "series": {
              
              "properties": {
                "race_type_id": {
                  
                },
                "result_series": {
                  
                },
                "idhash": {
                  
                },
                "version": {
                  
                },
                "filename": {
                  
                },
                "alias": {
                  
                },
                "title": {
                  
                },
                "race_type": {
                  
                  "properties": {
                    "race_type_id": {
                      
                    },
                    "version": {
                      
                    },
                    "filename": {
                      
                    },
                    "idhash": {
                      
                    },
                    "has_logo": {
                      
                    }
                  },
                  "required": [
                    "race_type_id",
                    "version",
                    "filename",
                    "idhash",
                    "has_logo"
                  ]
                },
                "championship": {
                  
                  "items": {}
                },
                "photo_edition": {
                  
                  "items": {}
                }
              },
              "required": [
                "race_type_id",
                "result_series",
                "idhash",
                "version",
                "filename",
                "alias",
                "title",
                "race_type",
                "championship",
                "photo_edition"
              ]
            },
            "standings": {
              
              "items": [
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "event": {
                      
                      "items": [
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        },
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        },
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        }
                      ]
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "event",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                }
              ]
            },
            "current_standing_type": {
              
            }
          },
          "required": [
            "series",
            "standings",
            "current_standing_type"
          ]
        },
        {
          
          "properties": {
            "series": {
              
              "properties": {
                "race_type_id": {
                  
                },
                "result_series": {
                  
                },
                "idhash": {
                  
                },
                "version": {
                  
                },
                "filename": {
                  
                },
                "alias": {
                  
                },
                "title": {
                  
                },
                "race_type": {
                  
                  "properties": {
                    "race_type_id": {
                      
                    },
                    "version": {
                      
                    },
                    "filename": {
                      
                    },
                    "idhash": {
                      
                    },
                    "has_logo": {
                      
                    }
                  },
                  "required": [
                    "race_type_id",
                    "version",
                    "filename",
                    "idhash",
                    "has_logo"
                  ]
                },
                "championship": {
                  
                  "items": {}
                },
                "photo_edition": {
                  
                  "items": {}
                }
              },
              "required": [
                "race_type_id",
                "result_series",
                "idhash",
                "version",
                "filename",
                "alias",
                "title",
                "race_type",
                "championship",
                "photo_edition"
              ]
            },
            "standings": {
              
              "items": [
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "event": {
                      
                      "items": [
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                },
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        },
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        }
                      ]
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "event",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                }
              ]
            },
            "current_standing_type": {
              
            }
          },
          "required": [
            "series",
            "standings",
            "current_standing_type"
          ]
        },
        {
          
          "properties": {
            "series": {
              
              "properties": {
                "race_type_id": {
                  
                },
                "result_series": {
                  
                },
                "idhash": {
                  
                },
                "version": {
                  
                },
                "filename": {
                  
                },
                "alias": {
                  
                },
                "title": {
                  
                },
                "race_type": {
                  
                  "properties": {
                    "race_type_id": {
                      
                    },
                    "version": {
                      
                    },
                    "filename": {
                      
                    },
                    "idhash": {
                      
                    },
                    "has_logo": {
                      
                    }
                  },
                  "required": [
                    "race_type_id",
                    "version",
                    "filename",
                    "idhash",
                    "has_logo"
                  ]
                },
                "championship": {
                  
                  "items": {}
                },
                "photo_edition": {
                  
                  "items": {}
                }
              },
              "required": [
                "race_type_id",
                "result_series",
                "idhash",
                "version",
                "filename",
                "alias",
                "title",
                "race_type",
                "championship",
                "photo_edition"
              ]
            },
            "standings": {
              
              "items": [
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "event": {
                      
                      "items": [
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                },
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        },
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        }
                      ]
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "event",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                }
              ]
            },
            "current_standing_type": {
              
            }
          },
          "required": [
            "series",
            "standings",
            "current_standing_type"
          ]
        },
        {
          
          "properties": {
            "series": {
              
              "properties": {
                "race_type_id": {
                  
                },
                "result_series": {
                  
                },
                "idhash": {
                  
                },
                "version": {
                  
                },
                "filename": {
                  
                },
                "alias": {
                  
                },
                "title": {
                  
                },
                "race_type": {
                  
                  "properties": {
                    "race_type_id": {
                      
                    },
                    "version": {
                      
                    },
                    "filename": {
                      
                    },
                    "idhash": {
                      
                    },
                    "has_logo": {
                      
                    }
                  },
                  "required": [
                    "race_type_id",
                    "version",
                    "filename",
                    "idhash",
                    "has_logo"
                  ]
                },
                "championship": {
                  
                  "items": {}
                },
                "photo_edition": {
                  
                  "items": {}
                }
              },
              "required": [
                "race_type_id",
                "result_series",
                "idhash",
                "version",
                "filename",
                "alias",
                "title",
                "race_type",
                "championship",
                "photo_edition"
              ]
            },
            "standings": {
              
              "items": [
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "event": {
                      
                      "items": [
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        },
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        },
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        }
                      ]
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "event",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                }
              ]
            },
            "current_standing_type": {
              
            }
          },
          "required": [
            "series",
            "standings",
            "current_standing_type"
          ]
        },
        {
          
          "properties": {
            "series": {
              
              "properties": {
                "race_type_id": {
                  
                },
                "result_series": {
                  
                },
                "idhash": {
                  
                },
                "version": {
                  
                },
                "filename": {
                  
                },
                "alias": {
                  
                },
                "title": {
                  
                },
                "race_type": {
                  
                  "properties": {
                    "race_type_id": {
                      
                    },
                    "version": {
                      
                    },
                    "filename": {
                      
                    },
                    "idhash": {
                      
                    },
                    "has_logo": {
                      
                    }
                  },
                  "required": [
                    "race_type_id",
                    "version",
                    "filename",
                    "idhash",
                    "has_logo"
                  ]
                },
                "championship": {
                  
                  "items": {}
                },
                "photo_edition": {
                  
                  "items": {}
                }
              },
              "required": [
                "race_type_id",
                "result_series",
                "idhash",
                "version",
                "filename",
                "alias",
                "title",
                "race_type",
                "championship",
                "photo_edition"
              ]
            },
            "standings": {
              
              "items": [
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "event": {
                      
                      "items": [
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        },
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        },
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        }
                      ]
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "event",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                }
              ]
            },
            "current_standing_type": {
              
            }
          },
          "required": [
            "series",
            "standings",
            "current_standing_type"
          ]
        },
        {
          
          "properties": {
            "series": {
              
              "properties": {
                "race_type_id": {
                  
                },
                "result_series": {
                  
                },
                "idhash": {
                  
                },
                "version": {
                  
                },
                "filename": {
                  
                },
                "alias": {
                  
                },
                "title": {
                  
                },
                "race_type": {
                  
                  "properties": {
                    "race_type_id": {
                      
                    },
                    "version": {
                      
                    },
                    "filename": {
                      
                    },
                    "idhash": {
                      
                    },
                    "has_logo": {
                      
                    }
                  },
                  "required": [
                    "race_type_id",
                    "version",
                    "filename",
                    "idhash",
                    "has_logo"
                  ]
                },
                "championship": {
                  
                  "items": {}
                },
                "photo_edition": {
                  
                  "items": {}
                }
              },
              "required": [
                "race_type_id",
                "result_series",
                "idhash",
                "version",
                "filename",
                "alias",
                "title",
                "race_type",
                "championship",
                "photo_edition"
              ]
            },
            "standings": {
              
              "items": [
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "event": {
                      
                      "items": [
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        },
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        },
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        }
                      ]
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "event",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                }
              ]
            },
            "current_standing_type": {
              
            }
          },
          "required": [
            "series",
            "standings",
            "current_standing_type"
          ]
        },
        {
          
          "properties": {
            "series": {
              
              "properties": {
                "race_type_id": {
                  
                },
                "result_series": {
                  
                },
                "idhash": {
                  
                },
                "version": {
                  
                },
                "filename": {
                  
                },
                "alias": {
                  
                },
                "title": {
                  
                },
                "race_type": {
                  
                  "properties": {
                    "race_type_id": {
                      
                    },
                    "version": {
                      
                    },
                    "filename": {
                      
                    },
                    "idhash": {
                      
                    },
                    "has_logo": {
                      
                    }
                  },
                  "required": [
                    "race_type_id",
                    "version",
                    "filename",
                    "idhash",
                    "has_logo"
                  ]
                },
                "championship": {
                  
                  "items": {}
                },
                "photo_edition": {
                  
                  "items": {}
                }
              },
              "required": [
                "race_type_id",
                "result_series",
                "idhash",
                "version",
                "filename",
                "alias",
                "title",
                "race_type",
                "championship",
                "photo_edition"
              ]
            },
            "standings": {
              
              "items": [
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "event": {
                      
                      "items": [
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        }
                      ]
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "event",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "event": {
                      
                      "items": [
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        }
                      ]
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "event",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "event": {
                      
                      "items": [
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        }
                      ]
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "event",
                    "driver",
                    "team"
                  ]
                }
              ]
            },
            "current_standing_type": {
              
            }
          },
          "required": [
            "series",
            "standings",
            "current_standing_type"
          ]
        },
        {
          
          "properties": {
            "series": {
              
              "properties": {
                "race_type_id": {
                  
                },
                "result_series": {
                  
                },
                "idhash": {
                  
                },
                "version": {
                  
                },
                "filename": {
                  
                },
                "alias": {
                  
                },
                "title": {
                  
                },
                "race_type": {
                  
                  "properties": {
                    "race_type_id": {
                      
                    },
                    "version": {
                      
                    },
                    "filename": {
                      
                    },
                    "idhash": {
                      
                    },
                    "has_logo": {
                      
                    }
                  },
                  "required": [
                    "race_type_id",
                    "version",
                    "filename",
                    "idhash",
                    "has_logo"
                  ]
                },
                "championship": {
                  
                  "items": {}
                },
                "photo_edition": {
                  
                  "items": {}
                }
              },
              "required": [
                "race_type_id",
                "result_series",
                "idhash",
                "version",
                "filename",
                "alias",
                "title",
                "race_type",
                "championship",
                "photo_edition"
              ]
            },
            "standings": {
              
              "items": [
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "event": {
                      
                      "items": [
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        },
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        },
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        }
                      ]
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "event",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                }
              ]
            },
            "current_standing_type": {
              
            }
          },
          "required": [
            "series",
            "standings",
            "current_standing_type"
          ]
        },
        {
          
          "properties": {
            "series": {
              
              "properties": {
                "race_type_id": {
                  
                },
                "result_series": {
                  
                },
                "idhash": {
                  
                },
                "version": {
                  
                },
                "filename": {
                  
                },
                "alias": {
                  
                },
                "title": {
                  
                },
                "race_type": {
                  
                  "properties": {
                    "race_type_id": {
                      
                    },
                    "version": {
                      
                    },
                    "filename": {
                      
                    },
                    "idhash": {
                      
                    },
                    "has_logo": {
                      
                    }
                  },
                  "required": [
                    "race_type_id",
                    "version",
                    "filename",
                    "idhash",
                    "has_logo"
                  ]
                },
                "championship": {
                  
                  "items": {}
                },
                "photo_edition": {
                  
                  "items": {}
                }
              },
              "required": [
                "race_type_id",
                "result_series",
                "idhash",
                "version",
                "filename",
                "alias",
                "title",
                "race_type",
                "championship",
                "photo_edition"
              ]
            },
            "standings": {
              
              "items": [
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "event": {
                      
                      "items": [
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                },
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        },
                        {
                          
                          "properties": {
                            "event_id": {
                              
                            },
                            "result_race_id": {
                              
                            },
                            "sub_event": {
                              
                              "items": [
                                {
                                  
                                  "properties": {
                                    "championship_id": {
                                      
                                    },
                                    "championship_class": {
                                      
                                    },
                                    "pos": {
                                      
                                    },
                                    "result_race_id": {
                                      
                                    },
                                    "race_number": {
                                      
                                    },
                                    "result_driver_id": {
                                      
                                    },
                                    "race_points": {
                                      
                                    },
                                    "race_place": {
                                      
                                    }
                                  },
                                  "required": [
                                    "championship_id",
                                    "championship_class",
                                    "pos",
                                    "result_race_id",
                                    "race_number",
                                    "result_driver_id",
                                    "race_points",
                                    "race_place"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "event_id",
                            "result_race_id",
                            "sub_event"
                          ]
                        }
                      ]
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "event",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                },
                {
                  
                  "properties": {
                    "championship_id": {
                      
                    },
                    "championship_class": {
                      
                    },
                    "sort_order": {
                      
                    },
                    "pos": {
                      
                    },
                    "result_driver_id": {
                      
                    },
                    "total_points": {
                      
                    },
                    "next_points_dropped": {
                      
                    },
                    "next_points_dropped_date": {
                      
                    },
                    "driver": {
                      
                      "properties": {
                        "driver_id": {
                          
                        },
                        "country_id": {
                          
                        },
                        "result_driver_id": {
                          
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
                        "country",
                        "driver_edition"
                      ]
                    },
                    "team": {
                      
                      "properties": {
                        "result_race_id": {
                          
                        },
                        "entry_id": {
                          
                        },
                        "number": {
                          
                        },
                        "result_team": {
                          
                        },
                        "result_team_id": {
                          
                        },
                        "series": {
                          
                        },
                        "car_model": {
                          
                        },
                        "engine_model": {
                          
                        },
                        "tyres": {
                          
                        },
                        "sponsor": {
                          
                        },
                        "team_owner": {
                          
                        },
                        "eligibility": {
                          
                        },
                        "class": {
                          
                        },
                        "championship_id": {
                          
                        },
                        "sequence": {
                          
                        },
                        "result_driver_id": {
                          
                        }
                      },
                      "required": [
                        "result_race_id",
                        "entry_id",
                        "number",
                        "result_team",
                        "result_team_id",
                        "series",
                        "car_model",
                        "engine_model",
                        "tyres",
                        "sponsor",
                        "team_owner",
                        "eligibility",
                        "class",
                        "championship_id",
                        "sequence",
                        "result_driver_id"
                      ]
                    }
                  },
                  "required": [
                    "championship_id",
                    "championship_class",
                    "sort_order",
                    "pos",
                    "result_driver_id",
                    "total_points",
                    "next_points_dropped",
                    "next_points_dropped_date",
                    "driver",
                    "team"
                  ]
                }
              ]
            },
            "current_standing_type": {
              
            }
          },
          "required": [
            "series",
            "standings",
            "current_standing_type"
          ]
        }
      ]
    }
  },
  "required": [
    "data"
  ]
}

