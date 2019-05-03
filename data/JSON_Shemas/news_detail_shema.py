NEWS_DETAIL_SHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  
  "properties": {
    "data": {
      
      "properties": {
        "article_id": {
          
        },
        "edp": {
          
          "properties": {
            "article_edition_id": {
              
            },
            "video_edition_id": {
              
            },
            "livetext_edition_id": {
              
            },
            "edition_id": {
              
            },
            "title": {
              
            },
            "alias": {
              
            },
            "preview": {
              
            },
            "dt_published": {
              
            },
            "is_comment_disabled": {
              
            },
            "translator_id": {
              
            },
            "seo_title": {
              
            },
            "seo_description": {
              
            },
            "outside_link": {
              
            },
            "original_entity_id": {
              
            },
            "dt_modified": {
              
            },
            "creator_user_id": {
              
            },
            "modifier_user_id": {
              
            },
            "activity": {
              
            },
            "is_featured": {
              
            },
            "is_target_blank": {
              
            },
            "is_prime": {
              
            },
            "is_press_release": {
              
            },
            "add_to_digest": {
              
            },
            "show_ads": {
              
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
                        "photo_id": {
                          
                        },
                        "edition_id": {
                          
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
                        "photo_edition_id",
                        "photo_id",
                        "edition_id",
                        "title",
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
                            "alias": {
                              
                            },
                            "edition_id": {
                              
                            },
                            "race_type_edition_id": {
                              
                            }
                          },
                          "required": [
                            "title",
                            "alias",
                            "edition_id",
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
                            "author_edition_id": {
                              
                            },
                            "author_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            }
                          },
                          "required": [
                            "author_edition_id",
                            "author_id",
                            "first_name",
                            "last_name"
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
                        "photo_id": {
                          
                        },
                        "edition_id": {
                          
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
                        "photo_edition_id",
                        "photo_id",
                        "edition_id",
                        "title",
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
                            "alias": {
                              
                            },
                            "edition_id": {
                              
                            },
                            "race_type_edition_id": {
                              
                            }
                          },
                          "required": [
                            "title",
                            "alias",
                            "edition_id",
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
                            "author_edition_id": {
                              
                            },
                            "author_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            }
                          },
                          "required": [
                            "author_edition_id",
                            "author_id",
                            "first_name",
                            "last_name"
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
                        "photo_id": {
                          
                        },
                        "edition_id": {
                          
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
                        "photo_edition_id",
                        "photo_id",
                        "edition_id",
                        "title",
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
                            "alias": {
                              
                            },
                            "edition_id": {
                              
                            },
                            "race_type_edition_id": {
                              
                            }
                          },
                          "required": [
                            "title",
                            "alias",
                            "edition_id",
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
                            "author_edition_id": {
                              
                            },
                            "author_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            }
                          },
                          "required": [
                            "author_edition_id",
                            "author_id",
                            "first_name",
                            "last_name"
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
                        "photo_id": {
                          
                        },
                        "edition_id": {
                          
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
                        "photo_edition_id",
                        "photo_id",
                        "edition_id",
                        "title",
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
                            "alias": {
                              
                            },
                            "edition_id": {
                              
                            },
                            "race_type_edition_id": {
                              
                            }
                          },
                          "required": [
                            "title",
                            "alias",
                            "edition_id",
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
                            "author_edition_id": {
                              
                            },
                            "author_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            }
                          },
                          "required": [
                            "author_edition_id",
                            "author_id",
                            "first_name",
                            "last_name"
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
                        "photo_id": {
                          
                        },
                        "edition_id": {
                          
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
                        "photo_edition_id",
                        "photo_id",
                        "edition_id",
                        "title",
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
                            "alias": {
                              
                            },
                            "edition_id": {
                              
                            },
                            "race_type_edition_id": {
                              
                            }
                          },
                          "required": [
                            "title",
                            "alias",
                            "edition_id",
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
                            "author_edition_id": {
                              
                            },
                            "author_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            }
                          },
                          "required": [
                            "author_edition_id",
                            "author_id",
                            "first_name",
                            "last_name"
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
                        "photo_id": {
                          
                        },
                        "edition_id": {
                          
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
                        "photo_edition_id",
                        "photo_id",
                        "edition_id",
                        "title",
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
                            "alias": {
                              
                            },
                            "edition_id": {
                              
                            },
                            "race_type_edition_id": {
                              
                            }
                          },
                          "required": [
                            "title",
                            "alias",
                            "edition_id",
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
                            "author_edition_id": {
                              
                            },
                            "author_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            }
                          },
                          "required": [
                            "author_edition_id",
                            "author_id",
                            "first_name",
                            "last_name"
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
                        "photo_id": {
                          
                        },
                        "edition_id": {
                          
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
                        "photo_edition_id",
                        "photo_id",
                        "edition_id",
                        "title",
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
                            "alias": {
                              
                            },
                            "edition_id": {
                              
                            },
                            "race_type_edition_id": {
                              
                            }
                          },
                          "required": [
                            "title",
                            "alias",
                            "edition_id",
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
                            "author_edition_id": {
                              
                            },
                            "author_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            }
                          },
                          "required": [
                            "author_edition_id",
                            "author_id",
                            "first_name",
                            "last_name"
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
                        "photo_id": {
                          
                        },
                        "edition_id": {
                          
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
                        "photo_edition_id",
                        "photo_id",
                        "edition_id",
                        "title",
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
                            "alias": {
                              
                            },
                            "edition_id": {
                              
                            },
                            "race_type_edition_id": {
                              
                            }
                          },
                          "required": [
                            "title",
                            "alias",
                            "edition_id",
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
                            "author_edition_id": {
                              
                            },
                            "author_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            }
                          },
                          "required": [
                            "author_edition_id",
                            "author_id",
                            "first_name",
                            "last_name"
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
                        "photo_id": {
                          
                        },
                        "edition_id": {
                          
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
                        "photo_edition_id",
                        "photo_id",
                        "edition_id",
                        "title",
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
                            "alias": {
                              
                            },
                            "edition_id": {
                              
                            },
                            "race_type_edition_id": {
                              
                            }
                          },
                          "required": [
                            "title",
                            "alias",
                            "edition_id",
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
                            "author_edition_id": {
                              
                            },
                            "author_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            }
                          },
                          "required": [
                            "author_edition_id",
                            "author_id",
                            "first_name",
                            "last_name"
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
                        "photo_id": {
                          
                        },
                        "edition_id": {
                          
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
                        "photo_edition_id",
                        "photo_id",
                        "edition_id",
                        "title",
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
                            "alias": {
                              
                            },
                            "edition_id": {
                              
                            },
                            "race_type_edition_id": {
                              
                            }
                          },
                          "required": [
                            "title",
                            "alias",
                            "edition_id",
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
                            "author_edition_id": {
                              
                            },
                            "author_id": {
                              
                            },
                            "first_name": {
                              
                            },
                            "last_name": {
                              
                            }
                          },
                          "required": [
                            "author_edition_id",
                            "author_id",
                            "first_name",
                            "last_name"
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
            }
          },
          "required": [
            "article_edition_id",
            "video_edition_id",
            "livetext_edition_id",
            "edition_id",
            "title",
            "alias",
            "preview",
            "dt_published",
            "is_comment_disabled",
            "translator_id",
            "seo_title",
            "seo_description",
            "outside_link",
            "original_entity_id",
            "dt_modified",
            "creator_user_id",
            "modifier_user_id",
            "activity",
            "is_featured",
            "is_target_blank",
            "is_prime",
            "is_press_release",
            "add_to_digest",
            "show_ads",
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
                "article_type_edition_id": {
                  
                },
                "article_type_id": {
                  
                },
                "title": {
                  
                }
              },
              "required": [
                "article_type_edition_id",
                "article_type_id",
                "title"
              ]
            }
          },
          "required": [
            "article_type_id",
            "edp"
          ]
        },
        "author": {
          
          "properties": {
            "author_id": {
              
            },
            "edp": {
              
              "properties": {
                "author_edition_id": {
                  
                },
                "author_id": {
                  
                },
                "first_name": {
                  
                },
                "last_name": {
                  
                },
                "mood": {
                  
                },
                "official_title": {
                  
                },
                "alias": {
                  
                }
              },
              "required": [
                "author_edition_id",
                "author_id",
                "first_name",
                "last_name",
                "mood",
                "official_title",
                "alias"
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
                    "store_link",
                    "driver_edition_id",
                    "first_name",
                    "last_name",
                    "alias"
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
                    "store_link": {
                      
                    },
                    "team_edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    }
                  },
                  "required": [
                    "store_link",
                    "team_edition_id",
                    "title",
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
        "topics": {
          
          "items": {}
        },
        "alternatives": {
          
          "items": [
            {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "article_edition_id": {
                      
                    },
                    "edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "link_entity_id": {
                      
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
                    "article_edition_id",
                    "edition_id",
                    "title",
                    "alias",
                    "link_entity_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "items": {}
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
                        "race_type_id": {
                          
                        },
                        "edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "edition_id",
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
            {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "article_edition_id": {
                      
                    },
                    "edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "link_entity_id": {
                      
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
                    "article_edition_id",
                    "edition_id",
                    "title",
                    "alias",
                    "link_entity_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "items": {}
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
                        "race_type_id": {
                          
                        },
                        "edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "edition_id",
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
            {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "article_edition_id": {
                      
                    },
                    "edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "link_entity_id": {
                      
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
                    "article_edition_id",
                    "edition_id",
                    "title",
                    "alias",
                    "link_entity_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "items": {}
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
                        "race_type_id": {
                          
                        },
                        "edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "edition_id",
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
            {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "article_edition_id": {
                      
                    },
                    "edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "link_entity_id": {
                      
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
                    "article_edition_id",
                    "edition_id",
                    "title",
                    "alias",
                    "link_entity_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "items": {}
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
                        "race_type_id": {
                          
                        },
                        "edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "edition_id",
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
            {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "article_edition_id": {
                      
                    },
                    "edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "link_entity_id": {
                      
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
                    "article_edition_id",
                    "edition_id",
                    "title",
                    "alias",
                    "link_entity_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "items": {}
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
                        "race_type_id": {
                          
                        },
                        "edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "edition_id",
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
            {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "article_edition_id": {
                      
                    },
                    "edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "link_entity_id": {
                      
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
                    "article_edition_id",
                    "edition_id",
                    "title",
                    "alias",
                    "link_entity_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "items": {}
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
                        "race_type_id": {
                          
                        },
                        "edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "edition_id",
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
            {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "article_edition_id": {
                      
                    },
                    "edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "link_entity_id": {
                      
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
                    "article_edition_id",
                    "edition_id",
                    "title",
                    "alias",
                    "link_entity_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "items": {}
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
                        "race_type_id": {
                          
                        },
                        "edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "edition_id",
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
            {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "article_edition_id": {
                      
                    },
                    "edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "link_entity_id": {
                      
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
                    "article_edition_id",
                    "edition_id",
                    "title",
                    "alias",
                    "link_entity_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "items": {}
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
                        "race_type_id": {
                          
                        },
                        "edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "edition_id",
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
            {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "article_edition_id": {
                      
                    },
                    "edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "link_entity_id": {
                      
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
                    "article_edition_id",
                    "edition_id",
                    "title",
                    "alias",
                    "link_entity_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "items": {}
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
                        "race_type_id": {
                          
                        },
                        "edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "edition_id",
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
            {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "article_edition_id": {
                      
                    },
                    "edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "link_entity_id": {
                      
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
                    "article_edition_id",
                    "edition_id",
                    "title",
                    "alias",
                    "link_entity_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "items": {}
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
                        "race_type_id": {
                          
                        },
                        "edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "edition_id",
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
            {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "article_edition_id": {
                      
                    },
                    "edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "link_entity_id": {
                      
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
                    "article_edition_id",
                    "edition_id",
                    "title",
                    "alias",
                    "link_entity_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "items": {}
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
                        "race_type_id": {
                          
                        },
                        "edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "edition_id",
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
            {
              
              "properties": {
                "article_id": {
                  
                },
                "edp": {
                  
                  "properties": {
                    "article_edition_id": {
                      
                    },
                    "edition_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    },
                    "link_entity_id": {
                      
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
                    "article_edition_id",
                    "edition_id",
                    "title",
                    "alias",
                    "link_entity_id",
                    "body",
                    "photos",
                    "gallery_photos"
                  ]
                },
                "article_type": {
                  
                  "items": {}
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
                        "race_type_id": {
                          
                        },
                        "edition_id": {
                          
                        },
                        "title": {
                          
                        },
                        "alias": {
                          
                        }
                      },
                      "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "edition_id",
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
          ]
        },
        "next_entity": {
          
          "properties": {
            "article_id": {
              
            },
            "edp": {
              
              "properties": {
                "article_edition_id": {
                  
                },
                "edition_id": {
                  
                },
                "title": {
                  
                },
                "alias": {
                  
                },
                "preview": {
                  
                },
                "dt_published": {
                  
                },
                "outside_link": {
                  
                },
                "original_entity_id": {
                  
                },
                "dt_modified": {
                  
                },
                "is_target_blank": {
                  
                },
                "is_featured": {
                  
                },
                "is_prime": {
                  
                },
                "video_edition_id": {
                  
                },
                "media_type": {
                  
                },
                "extra_query_params": {
                  
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
                "article_edition_id",
                "edition_id",
                "title",
                "alias",
                "preview",
                "dt_published",
                "outside_link",
                "original_entity_id",
                "dt_modified",
                "is_target_blank",
                "is_featured",
                "is_prime",
                "video_edition_id",
                "media_type",
                "extra_query_params",
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
                    "article_type_edition_id": {
                      
                    },
                    "title": {
                      
                    }
                  },
                  "required": [
                    "article_type_edition_id",
                    "title"
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
                    "race_type_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    }
                  },
                  "required": [
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
        "pre_entity": {
          
          "properties": {
            "article_id": {
              
            },
            "edp": {
              
              "properties": {
                "article_edition_id": {
                  
                },
                "edition_id": {
                  
                },
                "title": {
                  
                },
                "alias": {
                  
                },
                "preview": {
                  
                },
                "dt_published": {
                  
                },
                "outside_link": {
                  
                },
                "original_entity_id": {
                  
                },
                "dt_modified": {
                  
                },
                "is_target_blank": {
                  
                },
                "is_featured": {
                  
                },
                "is_prime": {
                  
                },
                "video_edition_id": {
                  
                },
                "media_type": {
                  
                },
                "extra_query_params": {
                  
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
                "article_edition_id",
                "edition_id",
                "title",
                "alias",
                "preview",
                "dt_published",
                "outside_link",
                "original_entity_id",
                "dt_modified",
                "is_target_blank",
                "is_featured",
                "is_prime",
                "video_edition_id",
                "media_type",
                "extra_query_params",
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
                    "article_type_edition_id": {
                      
                    },
                    "title": {
                      
                    }
                  },
                  "required": [
                    "article_type_edition_id",
                    "title"
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
                    "race_type_id": {
                      
                    },
                    "title": {
                      
                    },
                    "alias": {
                      
                    }
                  },
                  "required": [
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
        "gallery_body": {
          
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
        "pre_entity",
        "gallery_body"
      ]
    }
  },
  "required": [
    "data"
  ]
}

