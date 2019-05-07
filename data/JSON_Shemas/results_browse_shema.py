RESULT_BROWSE_SHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  
  "properties": {
    "data": {
      
      "properties": {
        "current_year": {
          
        },
        "results": {
          
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
                "results": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    }
                  ]
                },
                "current_race": {
                  
                  "items": {}
                }
              },
              "required": [
                "series",
                "results",
                "current_race"
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
                "results": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    }
                  ]
                },
                "current_race": {
                  
                  "items": {}
                }
              },
              "required": [
                "series",
                "results",
                "current_race"
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
                "results": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    }
                  ]
                },
                "current_race": {
                  
                  "items": {}
                }
              },
              "required": [
                "series",
                "results",
                "current_race"
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
                "results": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    }
                  ]
                },
                "current_race": {
                  
                  "items": {}
                }
              },
              "required": [
                "series",
                "results",
                "current_race"
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
                "results": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    }
                  ]
                },
                "current_race": {
                  
                  "items": {}
                }
              },
              "required": [
                "series",
                "results",
                "current_race"
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
                "results": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    }
                  ]
                },
                "current_race": {
                  
                  "items": {}
                }
              },
              "required": [
                "series",
                "results",
                "current_race"
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
                "results": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    }
                  ]
                },
                "current_race": {
                  
                  "items": {}
                }
              },
              "required": [
                "series",
                "results",
                "current_race"
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
                "results": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                            },
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
                            },
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                            },
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
                            },
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                            },
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
                            },
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    }
                  ]
                },
                "current_race": {
                  
                  "items": {}
                }
              },
              "required": [
                "series",
                "results",
                "current_race"
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
                "results": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    }
                  ]
                },
                "current_race": {
                  
                  "items": {}
                }
              },
              "required": [
                "series",
                "results",
                "current_race"
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
                "results": {
                  
                  "items": [
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                            },
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                            },
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    },
                    {
                      
                      "properties": {
                        "sort_order": {
                          
                        },
                        "position": {
                          
                        },
                        "points": {
                          
                        },
                        "time": {
                          
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
                            },
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
                        }
                      },
                      "required": [
                        "sort_order",
                        "position",
                        "points",
                        "time",
                        "team",
                        "drivers"
                      ]
                    }
                  ]
                },
                "current_race": {
                  
                  "items": {}
                }
              },
              "required": [
                "series",
                "results",
                "current_race"
              ]
            }
          ]
        }
      },
      "required": [
        "current_year",
        "results"
      ]
    }
  },
  "required": [
    "data"
  ]
}

