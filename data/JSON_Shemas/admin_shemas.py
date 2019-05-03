ADMIN_INFO = {
  "$id": "http://example.com/root.json",
  
  "title": "The Root Schema",
  "required": [
    "editions",
    "widgets",
    "pictures_sizes",
    "staticLinks",
    "application_versions"
  ],
  "properties": {
    "editions": {
      "$id": "#/properties/editions",
      
      "title": "The Editions Schema",
      "required": [
        "editions",
        "current_edition"
      ],
      "properties": {
        "editions": {
          "$id": "#/properties/editions/properties/editions",
          
          "title": "The Editions Schema",
          "items": {
            "$id": "#/properties/editions/properties/editions/items",
            
            "title": "The Items Schema",
            "required": [
              "edition_id",
              "parent_id",
              "title",
              "code",
              "locale",
              "hreflang",
              "is_default",
              "domain",
              "subdomain",
              "mode",
              "priority",
              "options",
              "raw_langs",
              "raw_countries",
              "langs",
              "states",
              "flags"
            ],
            "langs": {
              "$id": "#/properties/editions/properties/editions/items/properties/langs",
              
              "title": "The Langs Schema",
              "required": [
                "aa",
                "ab",
                "af",
                "ak",
                "am",
                "ar",
                "an",
                "hy",
                "as",
                "av",
                "ae",
                "ay",
                "az",
                "ba",
                "bm",
                "eu",
                "be",
                "bn",
                "bh",
                "bi",
                "bo",
                "bs",
                "br",
                "bg",
                "ca",
                "ch",
                "ce",
                "zh",
                "cu",
                "cv",
                "kw",
                "co",
                "cr",
                "cy",
                "cs",
                "da",
                "dv",
                "dz",
                "en",
                "eo",
                "et",
                "ee",
                "fo",
                "fj",
                "fi",
                "fr",
                "fy",
                "ff",
                "ka",
                "de",
                "gd",
                "ga",
                "gl",
                "gv",
                "el",
                "gn",
                "gu",
                "ht",
                "ha",
                "he",
                "hz",
                "hi",
                "ho",
                "hr",
                "hu",
                "ig",
                "is",
                "io",
                "ii",
                "iu",
                "ie",
                "ia",
                "id",
                "ik",
                "it",
                "jv",
                "ja",
                "kl",
                "kn",
                "ks",
                "kr",
                "kk",
                "km",
                "ki",
                "rw",
                "ky",
                "kv",
                "kg",
                "ko",
                "kj",
                "ku",
                "lo",
                "la",
                "lv",
                "li",
                "ln",
                "lt",
                "lb",
                "lu",
                "lg",
                "mk",
                "mh",
                "ml",
                "mi",
                "mr",
                "mg",
                "mt",
                "mn",
                "ms",
                "my",
                "na",
                "nv",
                "nr",
                "nd",
                "ng",
                "ne",
                "nl",
                "nn",
                "nb",
                "no",
                "ny",
                "oc",
                "oj",
                "or",
                "om",
                "os",
                "pa",
                "fa",
                "pi",
                "pl",
                "pt",
                "ps",
                "qu",
                "rm",
                "ro",
                "rn",
                "ru",
                "sg",
                "sa",
                "si",
                "sk",
                "sl",
                "se",
                "sm",
                "sn",
                "sd",
                "so",
                "st",
                "es",
                "sq",
                "sc",
                "sr",
                "ss",
                "su",
                "sw",
                "sv",
                "ty",
                "ta",
                "tt",
                "te",
                "tg",
                "tl",
                "th",
                "ti",
                "to",
                "tn",
                "ts",
                "tk",
                "tr",
                "tw",
                "ug",
                "uk",
                "ur",
                "uz",
                "ve",
                "vi",
                "vo",
                "wa",
                "wo",
                "xh",
                "yi",
                "yo",
                "za",
                "zu"
              ],
              "current_edition": {
                
                "title": "The Current_edition Schema",
                "required": [
                  "edition_id",
                  "parent_id",
                  "title",
                  "code",
                  "locale",
                  "hreflang",
                  "is_default",
                  "domain",
                  "subdomain",
                  "mode",
                  "priority",
                  "options",
                  "raw_langs",
                  "raw_countries",
                  "langs",
                  "states"
                ],
                "widgets": {
                  
                  "required": [
                    "pages",
                    "config"
                  ],
                  "properties": {
                    "pages": {
                      
                      "required": [
                        "all",
                        "global",
                        "fr",
                        "de",
                        "ru",
                        "hu",
                        "id",
                        "jp",
                        "nl",
                        "in",
                        "us",
                        "ch_it",
                        "ch_de",
                        "ch_fr",
                        "en_au",
                        "ua"
                      ],
                      "properties": {
                        "all": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "global": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "title": "The 1 Schema",
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "fr": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "de": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "title": "The News Schema",
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "ru": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "hu": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ],
                                        "pattern": "^(.*)$"
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ],
                                        "pattern": "^(.*)$"
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "id": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "jp": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ],
                                        "pattern": "^(.*)$"
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ],
                                        "pattern": "^(.*)$"
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "nl": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ],
                                        "pattern": "^(.*)$"
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "in": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "us": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "ch_it": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "ch_de": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ],
                                        "pattern": "^(.*)$"
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ],
                                        "pattern": "^(.*)$"
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "ch_fr": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ],
                                        "pattern": "^(.*)$"
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "en_au": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        },
                        "ua": {
                          
                          "required": [
                            "news",
                            "videos"
                          ],
                          "properties": {
                            "news": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "top_block",
                                          "author_tool",
                                          "giorgio_piola",
                                          "feature_strip"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "videos": {
                              
                              "required": [
                                "pages"
                              ],
                              "properties": {
                                "pages": {
                                  
                                  "required": [
                                    "1"
                                  ],
                                  "properties": {
                                    "1": {
                                      
                                      "items": {
                                        
                                        "default": "",
                                        "examples": [
                                          "latest_videos"
                                        ]
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    },
                    "config": {
                      "$id": "#/properties/widgets/properties/config",
                      
                      "title": "The Config Schema",
                      "required": [
                        "sections"
                      ],
                      "properties": {
                        "sections": {
                          "$id": "#/properties/widgets/properties/config/properties/sections",
                          
                          "title": "The Sections Schema",
                          "required": [
                            "all"
                          ],
                          "properties": {
                            "all": {
                              "$id": "#/properties/widgets/properties/config/properties/sections/properties/all",
                              
                              "title": "The All Schema",
                              "required": [
                                "top_block",
                                "top_block_main",
                                "event_strip",
                                "feature_strip",
                                "author_tool",
                                "giorgio_piola",
                                "james_alien",
                                "motorsport_tv",
                                "latest_news",
                                "latest_news_first",
                                "latest_videos",
                                "latest_galleries",
                                "latest_events",
                                "trending-content",
                                "trending-content-prime"
                              ],
                              "properties": {
                                "top_block": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block",
                                  
                                  "title": "The Top_block Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "promotion/top-block"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "half_count_items",
                                        "offset",
                                        "count_items",
                                        "without_main_item"
                                      ],
                                      "properties": {
                                        "half_count_items": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/widget_options/properties/half_count_items",
                                          
                                          "title": "The Half_count_items Schema",
                                          "default": 0,
                                          "examples": [
                                            5
                                          ]
                                        },
                                        "offset": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/widget_options/properties/offset",
                                          
                                          "title": "The Offset Schema",
                                          "default": 0,
                                          "examples": [
                                            1
                                          ]
                                        },
                                        "count_items": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/widget_options/properties/count_items",
                                          
                                          "title": "The Count_items Schema",
                                          "default": 0,
                                          "examples": [
                                            10
                                          ]
                                        },
                                        "without_main_item": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/widget_options/properties/without_main_item",
                                          "type": "boolean",
                                          "title": "The Without_main_item Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "big_first_item",
                                        "translation",
                                        "line_color",
                                        "indicator_color",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "big_first_item": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/other_options/properties/big_first_item",
                                          "type": "boolean",
                                          "title": "The Big_first_item Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Top block"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "line_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/other_options/properties/line_color",
                                          
                                          "title": "The Line_color Schema",
                                          "default": "",
                                          "examples": [
                                            "ffdf00"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "indicator_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/other_options/properties/indicator_color",
                                          
                                          "title": "The Indicator_color Schema",
                                          "default": "",
                                          "examples": [
                                            "252525"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                },
                                "top_block_main": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block_main",
                                  
                                  "title": "The Top_block_main Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block_main/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "promotion/top-block"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block_main/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "count_items"
                                      ],
                                      "properties": {
                                        "count_items": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block_main/properties/widget_options/properties/count_items",
                                          
                                          "title": "The Count_items Schema",
                                          "default": 0,
                                          "examples": [
                                            1
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block_main/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "translation",
                                        "line_color",
                                        "indicator_color",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block_main/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block_main/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block_main/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Top block"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "line_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block_main/properties/other_options/properties/line_color",
                                          
                                          "title": "The Line_color Schema",
                                          "default": "",
                                          "examples": [
                                            "ffdf00"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "indicator_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block_main/properties/other_options/properties/indicator_color",
                                          
                                          "title": "The Indicator_color Schema",
                                          "default": "",
                                          "examples": [
                                            "252525"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/top_block_main/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                },
                                "event_strip": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/event_strip",
                                  
                                  "title": "The Event_strip Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/event_strip/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "event/strip"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/event_strip/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "different_days"
                                      ],
                                      "properties": {
                                        "different_days": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/event_strip/properties/widget_options/properties/different_days",
                                          
                                          "title": "The Different_days Schema",
                                          "default": 0,
                                          "examples": [
                                            7
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/event_strip/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "translation",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/event_strip/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/event_strip/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/event_strip/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Event strip"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/event_strip/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                },
                                "feature_strip": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/feature_strip",
                                  
                                  "title": "The Feature_strip Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/feature_strip/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "promotion/feature-strip"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/feature_strip/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "half_count_items",
                                        "count_items"
                                      ],
                                      "properties": {
                                        "half_count_items": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/feature_strip/properties/widget_options/properties/half_count_items",
                                          
                                          "title": "The Half_count_items Schema",
                                          "default": 0,
                                          "examples": [
                                            5
                                          ]
                                        },
                                        "count_items": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/feature_strip/properties/widget_options/properties/count_items",
                                          
                                          "title": "The Count_items Schema",
                                          "default": 0,
                                          "examples": [
                                            10
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/feature_strip/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "translation",
                                        "title_background",
                                        "big_first_item"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/feature_strip/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/feature_strip/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/feature_strip/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Feature strip"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/feature_strip/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "big_first_item": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/feature_strip/properties/other_options/properties/big_first_item",
                                          "type": "boolean",
                                          "title": "The Big_first_item Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        }
                                      }
                                    }
                                  }
                                },
                                "author_tool": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/author_tool",
                                  
                                  "title": "The Author_tool Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/author_tool/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "promotion/author-tool"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/author_tool/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "count_items"
                                      ],
                                      "properties": {
                                        "count_items": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/author_tool/properties/widget_options/properties/count_items",
                                          
                                          "title": "The Count_items Schema",
                                          "default": 0,
                                          "examples": [
                                            5
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/author_tool/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "big_first_item",
                                        "translation",
                                        "line_color",
                                        "indicator_color",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/author_tool/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/author_tool/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "big_first_item": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/author_tool/properties/other_options/properties/big_first_item",
                                          "type": "boolean",
                                          "title": "The Big_first_item Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/author_tool/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Author tool"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "line_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/author_tool/properties/other_options/properties/line_color",
                                          
                                          "title": "The Line_color Schema",
                                          "default": "",
                                          "examples": [
                                            "0000ff"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "indicator_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/author_tool/properties/other_options/properties/indicator_color",
                                          
                                          "title": "The Indicator_color Schema",
                                          "default": "",
                                          "examples": [
                                            "0000ff"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/author_tool/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                },
                                "giorgio_piola": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola",
                                  
                                  "title": "The Giorgio_piola Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "topic/find"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "count_articles",
                                        "count_videos",
                                        "topic_id"
                                      ],
                                      "properties": {
                                        "count_articles": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/widget_options/properties/count_articles",
                                          
                                          "title": "The Count_articles Schema",
                                          "default": 0,
                                          "examples": [
                                            5
                                          ]
                                        },
                                        "count_videos": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/widget_options/properties/count_videos",
                                          
                                          "title": "The Count_videos Schema",
                                          "default": 0,
                                          "examples": [
                                            1
                                          ]
                                        },
                                        "topic_id": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/widget_options/properties/topic_id",
                                          
                                          "title": "The Topic_id Schema",
                                          "default": 0,
                                          "examples": [
                                            23
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "big_first_item",
                                        "line_color",
                                        "indicator_color",
                                        "background_color",
                                        "title_color",
                                        "subtitle_color",
                                        "logo",
                                        "translation",
                                        "subtitle_translation",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "big_first_item": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/other_options/properties/big_first_item",
                                          "type": "boolean",
                                          "title": "The Big_first_item Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "line_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/other_options/properties/line_color",
                                          
                                          "title": "The Line_color Schema",
                                          "default": "",
                                          "examples": [
                                            "007200"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "indicator_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/other_options/properties/indicator_color",
                                          
                                          "title": "The Indicator_color Schema",
                                          "default": "",
                                          "examples": [
                                            "007200"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "background_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/other_options/properties/background_color",
                                          
                                          "title": "The Background_color Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/other_options/properties/title_color",
                                          
                                          "title": "The Title_color Schema",
                                          "default": "",
                                          "examples": [
                                            "FFFFFF"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "subtitle_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/other_options/properties/subtitle_color",
                                          
                                          "title": "The Subtitle_color Schema",
                                          "default": "",
                                          "examples": [
                                            "FF0000"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "logo": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/other_options/properties/logo",
                                          
                                          "title": "The Logo Schema",
                                          "default": "",
                                          "examples": [
                                            "http://motorsport.com-cdn.s3.amazonaws.com/static/img/tf/giola.png"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Джорджо Піола"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "subtitle_translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/other_options/properties/subtitle_translation",
                                          
                                          "title": "The Subtitle_translation Schema",
                                          "default": "",
                                          "examples": [
                                            "giorgio_piola_widget_subtitle"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/giorgio_piola/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                },
                                "james_alien": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien",
                                  
                                  "title": "The James_alien Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "topic/find"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "count_articles",
                                        "topic_id"
                                      ],
                                      "properties": {
                                        "count_articles": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/widget_options/properties/count_articles",
                                          
                                          "title": "The Count_articles Schema",
                                          "default": 0,
                                          "examples": [
                                            5
                                          ]
                                        },
                                        "topic_id": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/widget_options/properties/topic_id",
                                          
                                          "title": "The Topic_id Schema",
                                          "default": 0,
                                          "examples": [
                                            322
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "big_first_item",
                                        "line_color",
                                        "indicator_color",
                                        "background_color",
                                        "title_color",
                                        "subtitle_color",
                                        "logo",
                                        "translation",
                                        "subtitle_translation",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "big_first_item": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/other_options/properties/big_first_item",
                                          "type": "boolean",
                                          "title": "The Big_first_item Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "line_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/other_options/properties/line_color",
                                          
                                          "title": "The Line_color Schema",
                                          "default": "",
                                          "examples": [
                                            "fe0000"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "indicator_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/other_options/properties/indicator_color",
                                          
                                          "title": "The Indicator_color Schema",
                                          "default": "",
                                          "examples": [
                                            "fe0000"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "background_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/other_options/properties/background_color",
                                          
                                          "title": "The Background_color Schema",
                                          "default": "",
                                          "examples": [
                                            "FF0000"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/other_options/properties/title_color",
                                          
                                          "title": "The Title_color Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "subtitle_color": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/other_options/properties/subtitle_color",
                                          
                                          "title": "The Subtitle_color Schema",
                                          "default": "",
                                          "examples": [
                                            "FFFFFF"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "logo": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/other_options/properties/logo",
                                          
                                          "title": "The Logo Schema",
                                          "default": "",
                                          "examples": [
                                            "http://motorsport.com-cdn.s3.amazonaws.com/static/img/tf/ja_f1.png"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Джеймс Аллен"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "subtitle_translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/other_options/properties/subtitle_translation",
                                          
                                          "title": "The Subtitle_translation Schema",
                                          "default": "",
                                          "examples": [
                                            "james_alien_widget_subtitle"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/james_alien/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                },
                                "motorsport_tv": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/motorsport_tv",
                                  
                                  "title": "The Motorsport_tv Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/motorsport_tv/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "videos/latest"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/motorsport_tv/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "count_videos",
                                        "video_source"
                                      ],
                                      "properties": {
                                        "count_videos": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/motorsport_tv/properties/widget_options/properties/count_videos",
                                          
                                          "title": "The Count_videos Schema",
                                          "default": 0,
                                          "examples": [
                                            3
                                          ]
                                        },
                                        "video_source": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/motorsport_tv/properties/widget_options/properties/video_source",
                                          
                                          "title": "The Video_source Schema",
                                          "default": "",
                                          "examples": [
                                            "motorsport"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/motorsport_tv/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "translation",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/motorsport_tv/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/motorsport_tv/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/motorsport_tv/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Motorsport tv"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/motorsport_tv/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                },
                                "latest_news": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news",
                                  
                                  "title": "The Latest_news Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "article/latest"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "count_articles"
                                      ],
                                      "properties": {
                                        "count_articles": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news/properties/widget_options/properties/count_articles",
                                          
                                          "title": "The Count_articles Schema",
                                          "default": 0,
                                          "examples": [
                                            12
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "translation",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Останні відео"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                },
                                "latest_news_first": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news_first",
                                  
                                  "title": "The Latest_news_first Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news_first/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "article/latest"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news_first/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "count_articles",
                                        "is_first_page"
                                      ],
                                      "properties": {
                                        "count_articles": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news_first/properties/widget_options/properties/count_articles",
                                          
                                          "title": "The Count_articles Schema",
                                          "default": 0,
                                          "examples": [
                                            12
                                          ]
                                        },
                                        "is_first_page": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news_first/properties/widget_options/properties/is_first_page",
                                          "type": "boolean",
                                          "title": "The Is_first_page Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news_first/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "translation",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news_first/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news_first/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news_first/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Останні відео"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_news_first/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                },
                                "latest_videos": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_videos",
                                  
                                  "title": "The Latest_videos Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_videos/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "videos/latest"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_videos/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "count_videos"
                                      ],
                                      "properties": {
                                        "count_videos": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_videos/properties/widget_options/properties/count_videos",
                                          
                                          "title": "The Count_videos Schema",
                                          "default": 0,
                                          "examples": [
                                            3
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_videos/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "big_first_item",
                                        "translation",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_videos/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_videos/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "big_first_item": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_videos/properties/other_options/properties/big_first_item",
                                          "type": "boolean",
                                          "title": "The Big_first_item Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_videos/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Останні відео"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_videos/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                },
                                "latest_galleries": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_galleries",
                                  
                                  "title": "The Latest_galleries Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_galleries/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "photos/latest"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_galleries/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "count_photos"
                                      ],
                                      "properties": {
                                        "count_photos": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_galleries/properties/widget_options/properties/count_photos",
                                          
                                          "title": "The Count_photos Schema",
                                          "default": 0,
                                          "examples": [
                                            5
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_galleries/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "translation",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_galleries/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_galleries/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_galleries/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Останні фото"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_galleries/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                },
                                "latest_events": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_events",
                                  
                                  "title": "The Latest_events Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_events/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "event/latest"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_events/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "count_events"
                                      ],
                                      "properties": {
                                        "count_events": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_events/properties/widget_options/properties/count_events",
                                          
                                          "title": "The Count_events Schema",
                                          "default": 0,
                                          "examples": [
                                            5
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_events/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "big_first_item",
                                        "translation",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_events/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_events/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "big_first_item": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_events/properties/other_options/properties/big_first_item",
                                          "type": "boolean",
                                          "title": "The Big_first_item Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_events/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Останні події"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/latest_events/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                },
                                "trending-content": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content",
                                  
                                  "title": "The Trending-content Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "trending/latest"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "count_items"
                                      ],
                                      "properties": {
                                        "count_items": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content/properties/widget_options/properties/count_items",
                                          
                                          "title": "The Count_items Schema",
                                          "default": 0,
                                          "examples": [
                                            5
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "big_first_item",
                                        "translation",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "big_first_item": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content/properties/other_options/properties/big_first_item",
                                          "type": "boolean",
                                          "title": "The Big_first_item Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Контент у тренді"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                },
                                "trending-content-prime": {
                                  "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content-prime",
                                  
                                  "title": "The Trending-content-prime Schema",
                                  "required": [
                                    "widget_alias",
                                    "widget_options",
                                    "other_options"
                                  ],
                                  "properties": {
                                    "widget_alias": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content-prime/properties/widget_alias",
                                      
                                      "title": "The Widget_alias Schema",
                                      "default": "",
                                      "examples": [
                                        "trending/latest"
                                      ],
                                      "pattern": "^(.*)$"
                                    },
                                    "widget_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content-prime/properties/widget_options",
                                      
                                      "title": "The Widget_options Schema",
                                      "required": [
                                        "count_items"
                                      ],
                                      "properties": {
                                        "count_items": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content-prime/properties/widget_options/properties/count_items",
                                          
                                          "title": "The Count_items Schema",
                                          "default": 0,
                                          "examples": [
                                            6
                                          ]
                                        }
                                      }
                                    },
                                    "other_options": {
                                      "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content-prime/properties/other_options",
                                      
                                      "title": "The Other_options Schema",
                                      "required": [
                                        "first_item_contains_author",
                                        "last_items_contains_author",
                                        "big_first_item",
                                        "translation",
                                        "title_background"
                                      ],
                                      "properties": {
                                        "first_item_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content-prime/properties/other_options/properties/first_item_contains_author",
                                          "type": "boolean",
                                          "title": "The First_item_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "last_items_contains_author": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content-prime/properties/other_options/properties/last_items_contains_author",
                                          "type": "boolean",
                                          "title": "The Last_items_contains_author Schema",
                                          "default": False,
                                          "examples": [
                                            False
                                          ]
                                        },
                                        "big_first_item": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content-prime/properties/other_options/properties/big_first_item",
                                          "type": "boolean",
                                          "title": "The Big_first_item Schema",
                                          "default": False,
                                          "examples": [
                                            True
                                          ]
                                        },
                                        "translation": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content-prime/properties/other_options/properties/translation",
                                          
                                          "title": "The Translation Schema",
                                          "default": "",
                                          "examples": [
                                            "Контент у тренді"
                                          ],
                                          "pattern": "^(.*)$"
                                        },
                                        "title_background": {
                                          "$id": "#/properties/widgets/properties/config/properties/sections/properties/all/properties/trending-content-prime/properties/other_options/properties/title_background",
                                          
                                          "title": "The Title_background Schema",
                                          "default": "",
                                          "examples": [
                                            "000000"
                                          ],
                                          "pattern": "^(.*)$"
                                        }
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "pictures_sizes": {
                  "$id": "#/properties/pictures_sizes",
                  
                  "title": "The Pictures_sizes Schema",
                  "required": [
                    "mgl",
                    "vmt",
                    "amp",
                    "mkt",
                    "mst",
                    "atr",
                    "src",
                    "flg",
                    "ads",
                    "skw",
                    "usa",
                    "upc",
                    "mgz",
                    "rtp",
                    "mrtp"
                  ],
                  "properties": {
                    "mgl": {
                      "$id": "#/properties/pictures_sizes/properties/mgl",
                      
                      "title": "The Mgl Schema",
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
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/mgl/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                970
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                648
                              ]
                            }
                          }
                        },
                        "s2": {
                          "$id": "#/properties/pictures_sizes/properties/mgl/properties/s2",
                          
                          "title": "The S2 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s2/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                350
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s2/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                350
                              ]
                            }
                          }
                        },
                        "s3": {
                          "$id": "#/properties/pictures_sizes/properties/mgl/properties/s3",
                          
                          "title": "The S3 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s3/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s3/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            }
                          }
                        },
                        "s4": {
                          "$id": "#/properties/pictures_sizes/properties/mgl/properties/s4",
                          
                          "title": "The S4 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s4/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                250
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s4/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                250
                              ]
                            }
                          }
                        },
                        "s5": {
                          "$id": "#/properties/pictures_sizes/properties/mgl/properties/s5",
                          
                          "title": "The S5 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s5/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                200
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s5/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                133
                              ]
                            }
                          }
                        },
                        "s6": {
                          "$id": "#/properties/pictures_sizes/properties/mgl/properties/s6",
                          
                          "title": "The S6 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s6/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                150
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s6/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                150
                              ]
                            }
                          }
                        },
                        "s7": {
                          "$id": "#/properties/pictures_sizes/properties/mgl/properties/s7",
                          
                          "title": "The S7 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s7/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                1440
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s7/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                960
                              ]
                            }
                          }
                        },
                        "s8": {
                          "$id": "#/properties/pictures_sizes/properties/mgl/properties/s8",
                          
                          "title": "The S8 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s8/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                800
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s8/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                533
                              ]
                            }
                          }
                        },
                        "s9": {
                          "$id": "#/properties/pictures_sizes/properties/mgl/properties/s9",
                          
                          "title": "The S9 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s9/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                335
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/s9/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                250
                              ]
                            }
                          }
                        },
                        "sp1": {
                          "$id": "#/properties/pictures_sizes/properties/mgl/properties/sp1",
                          
                          "title": "The Sp1 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/sp1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                800
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/sp1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                533
                              ]
                            }
                          }
                        },
                        "sp2": {
                          "$id": "#/properties/pictures_sizes/properties/mgl/properties/sp2",
                          
                          "title": "The Sp2 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/sp2/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                800
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/sp2/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                533
                              ]
                            }
                          }
                        },
                        "sp8": {
                          "$id": "#/properties/pictures_sizes/properties/mgl/properties/sp8",
                          
                          "title": "The Sp8 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/sp8/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                800
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgl/properties/sp8/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                533
                              ]
                            }
                          }
                        }
                      }
                    },
                    "vmt": {
                      "$id": "#/properties/pictures_sizes/properties/vmt",
                      
                      "title": "The Vmt Schema",
                      "required": [
                        "s1",
                        "s2",
                        "s3",
                        "s4",
                        "s5",
                        "s6"
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/vmt/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/vmt/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                640
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/vmt/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                360
                              ]
                            }
                          }
                        },
                        "s2": {
                          "$id": "#/properties/pictures_sizes/properties/vmt/properties/s2",
                          
                          "title": "The S2 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/vmt/properties/s2/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                186
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/vmt/properties/s2/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                104
                              ]
                            }
                          }
                        },
                        "s3": {
                          "$id": "#/properties/pictures_sizes/properties/vmt/properties/s3",
                          
                          "title": "The S3 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/vmt/properties/s3/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                160
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/vmt/properties/s3/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                90
                              ]
                            }
                          }
                        },
                        "s4": {
                          "$id": "#/properties/pictures_sizes/properties/vmt/properties/s4",
                          
                          "title": "The S4 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/vmt/properties/s4/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                134
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/vmt/properties/s4/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                75
                              ]
                            }
                          }
                        },
                        "s5": {
                          "$id": "#/properties/pictures_sizes/properties/vmt/properties/s5",
                          
                          "title": "The S5 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/vmt/properties/s5/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/vmt/properties/s5/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                169
                              ]
                            }
                          }
                        },
                        "s6": {
                          "$id": "#/properties/pictures_sizes/properties/vmt/properties/s6",
                          
                          "title": "The S6 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/vmt/properties/s6/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                30
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/vmt/properties/s6/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                17
                              ]
                            }
                          }
                        }
                      }
                    },
                    "amp": {
                      "$id": "#/properties/pictures_sizes/properties/amp",
                      
                      "title": "The Amp Schema",
                      "required": [
                        "s1",
                        "s2",
                        "s3",
                        "s4",
                        "s6",
                        "s7"
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/amp/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/amp/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                600
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/amp/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                400
                              ]
                            }
                          }
                        },
                        "s2": {
                          "$id": "#/properties/pictures_sizes/properties/amp/properties/s2",
                          
                          "title": "The S2 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/amp/properties/s2/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                413
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/amp/properties/s2/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                275
                              ]
                            }
                          }
                        },
                        "s3": {
                          "$id": "#/properties/pictures_sizes/properties/amp/properties/s3",
                          
                          "title": "The S3 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/amp/properties/s3/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/amp/properties/s3/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                200
                              ]
                            }
                          }
                        },
                        "s4": {
                          "$id": "#/properties/pictures_sizes/properties/amp/properties/s4",
                          
                          "title": "The S4 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/amp/properties/s4/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                135
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/amp/properties/s4/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                90
                              ]
                            }
                          }
                        },
                        "s6": {
                          "$id": "#/properties/pictures_sizes/properties/amp/properties/s6",
                          
                          "title": "The S6 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/amp/properties/s6/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                800
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/amp/properties/s6/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                533
                              ]
                            }
                          }
                        },
                        "s7": {
                          "$id": "#/properties/pictures_sizes/properties/amp/properties/s7",
                          
                          "title": "The S7 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/amp/properties/s7/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                40
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/amp/properties/s7/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                30
                              ]
                            }
                          }
                        }
                      }
                    },
                    "mkt": {
                      "$id": "#/properties/pictures_sizes/properties/mkt",
                      
                      "title": "The Mkt Schema",
                      "required": [
                        "s1",
                        "s2"
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/mkt/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h",
                            "is_main"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mkt/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                600
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mkt/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                600
                              ]
                            },
                            "is_main": {
                              "$id": "#/properties/pictures_sizes/properties/mkt/properties/s1/properties/is_main",
                              "type": "boolean",
                              "title": "The Is_main Schema",
                              "default": False,
                              "examples": [
                                True
                              ]
                            }
                          }
                        },
                        "s2": {
                          "$id": "#/properties/pictures_sizes/properties/mkt/properties/s2",
                          
                          "title": "The S2 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mkt/properties/s2/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mkt/properties/s2/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            }
                          }
                        }
                      }
                    },
                    "mst": {
                      "$id": "#/properties/pictures_sizes/properties/mst",
                      
                      "title": "The Mst Schema",
                      "required": [
                        "s1",
                        "s2"
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/mst/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h",
                            "is_main"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mst/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                600
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mst/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                600
                              ]
                            },
                            "is_main": {
                              "$id": "#/properties/pictures_sizes/properties/mst/properties/s1/properties/is_main",
                              "type": "boolean",
                              "title": "The Is_main Schema",
                              "default": False,
                              "examples": [
                                True
                              ]
                            }
                          }
                        },
                        "s2": {
                          "$id": "#/properties/pictures_sizes/properties/mst/properties/s2",
                          
                          "title": "The S2 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mst/properties/s2/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mst/properties/s2/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            }
                          }
                        }
                      }
                    },
                    "atr": {
                      "$id": "#/properties/pictures_sizes/properties/atr",
                      
                      "title": "The Atr Schema",
                      "required": [
                        "s1",
                        "s2"
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/atr/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h",
                            "is_main"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/atr/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                600
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/atr/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                600
                              ]
                            },
                            "is_main": {
                              "$id": "#/properties/pictures_sizes/properties/atr/properties/s1/properties/is_main",
                              "type": "boolean",
                              "title": "The Is_main Schema",
                              "default": False,
                              "examples": [
                                True
                              ]
                            }
                          }
                        },
                        "s2": {
                          "$id": "#/properties/pictures_sizes/properties/atr/properties/s2",
                          
                          "title": "The S2 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/atr/properties/s2/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/atr/properties/s2/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            }
                          }
                        }
                      }
                    },
                    "src": {
                      "$id": "#/properties/pictures_sizes/properties/src",
                      
                      "title": "The Src Schema",
                      "required": [
                        "s1"
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/src/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h",
                            "is_main"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/src/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/src/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                100
                              ]
                            },
                            "is_main": {
                              "$id": "#/properties/pictures_sizes/properties/src/properties/s1/properties/is_main",
                              "type": "boolean",
                              "title": "The Is_main Schema",
                              "default": False,
                              "examples": [
                                True
                              ]
                            }
                          }
                        }
                      }
                    },
                    "flg": {
                      "$id": "#/properties/pictures_sizes/properties/flg",
                      
                      "title": "The Flg Schema",
                      "required": [
                        "s2"
                      ],
                      "properties": {
                        "s2": {
                          "$id": "#/properties/pictures_sizes/properties/flg/properties/s2",
                          
                          "title": "The S2 Schema",
                          "required": [
                            "w",
                            "h",
                            "is_main"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/flg/properties/s2/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                100
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/flg/properties/s2/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                60
                              ]
                            },
                            "is_main": {
                              "$id": "#/properties/pictures_sizes/properties/flg/properties/s2/properties/is_main",
                              "type": "boolean",
                              "title": "The Is_main Schema",
                              "default": False,
                              "examples": [
                                True
                              ]
                            }
                          }
                        }
                      }
                    },
                    "ads": {
                      "$id": "#/properties/pictures_sizes/properties/ads",
                      
                      "title": "The Ads Schema",
                      "required": [
                        "s1"
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/ads/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h",
                            "is_main"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/ads/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                728
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/ads/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                90
                              ]
                            },
                            "is_main": {
                              "$id": "#/properties/pictures_sizes/properties/ads/properties/s1/properties/is_main",
                              "type": "boolean",
                              "title": "The Is_main Schema",
                              "default": False,
                              "examples": [
                                True
                              ]
                            }
                          }
                        }
                      }
                    },
                    "skw": {
                      "$id": "#/properties/pictures_sizes/properties/skw",
                      
                      "title": "The Skw Schema",
                      "required": [
                        "s1"
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/skw/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h",
                            "is_main"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/skw/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/skw/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                250
                              ]
                            },
                            "is_main": {
                              "$id": "#/properties/pictures_sizes/properties/skw/properties/s1/properties/is_main",
                              "type": "boolean",
                              "title": "The Is_main Schema",
                              "default": False,
                              "examples": [
                                True
                              ]
                            }
                          }
                        }
                      }
                    },
                    "usa": {
                      "$id": "#/properties/pictures_sizes/properties/usa",
                      
                      "title": "The Usa Schema",
                      "required": [
                        "s1",
                        "s2"
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/usa/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h",
                            "is_main"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/usa/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                400
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/usa/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                400
                              ]
                            },
                            "is_main": {
                              "$id": "#/properties/pictures_sizes/properties/usa/properties/s1/properties/is_main",
                              "type": "boolean",
                              "title": "The Is_main Schema",
                              "default": False,
                              "examples": [
                                True
                              ]
                            }
                          }
                        },
                        "s2": {
                          "$id": "#/properties/pictures_sizes/properties/usa/properties/s2",
                          
                          "title": "The S2 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/usa/properties/s2/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                160
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/usa/properties/s2/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                160
                              ]
                            }
                          }
                        }
                      }
                    },
                    "upc": {
                      "$id": "#/properties/pictures_sizes/properties/upc",
                      
                      "title": "The Upc Schema",
                      "required": [
                        "s1",
                        "s2",
                        "s3",
                        "s4",
                        "s5"
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/upc/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h",
                            "is_main"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/upc/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                200
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/upc/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                200
                              ]
                            },
                            "is_main": {
                              "$id": "#/properties/pictures_sizes/properties/upc/properties/s1/properties/is_main",
                              "type": "boolean",
                              "title": "The Is_main Schema",
                              "default": False,
                              "examples": [
                                True
                              ]
                            }
                          }
                        },
                        "s2": {
                          "$id": "#/properties/pictures_sizes/properties/upc/properties/s2",
                          
                          "title": "The S2 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/upc/properties/s2/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                150
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/upc/properties/s2/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                150
                              ]
                            }
                          }
                        },
                        "s3": {
                          "$id": "#/properties/pictures_sizes/properties/upc/properties/s3",
                          
                          "title": "The S3 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/upc/properties/s3/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                100
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/upc/properties/s3/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                100
                              ]
                            }
                          }
                        },
                        "s4": {
                          "$id": "#/properties/pictures_sizes/properties/upc/properties/s4",
                          
                          "title": "The S4 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/upc/properties/s4/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                75
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/upc/properties/s4/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                75
                              ]
                            }
                          }
                        },
                        "s5": {
                          "$id": "#/properties/pictures_sizes/properties/upc/properties/s5",
                          
                          "title": "The S5 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/upc/properties/s5/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                35
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/upc/properties/s5/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                35
                              ]
                            }
                          }
                        }
                      }
                    },
                    "mgz": {
                      "$id": "#/properties/pictures_sizes/properties/mgz",
                      
                      "title": "The Mgz Schema",
                      "required": [
                        "s1",
                        "s3"
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/mgz/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h",
                            "is_main"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgz/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": "",
                              "examples": [
                                "*"
                              ],
                              "pattern": "^(.*)$"
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgz/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": "",
                              "examples": [
                                "*"
                              ],
                              "pattern": "^(.*)$"
                            },
                            "is_main": {
                              "$id": "#/properties/pictures_sizes/properties/mgz/properties/s1/properties/is_main",
                              "type": "boolean",
                              "title": "The Is_main Schema",
                              "default": False,
                              "examples": [
                                True
                              ]
                            }
                          }
                        },
                        "s3": {
                          "$id": "#/properties/pictures_sizes/properties/mgz/properties/s3",
                          
                          "title": "The S3 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mgz/properties/s3/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                360
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mgz/properties/s3/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                280
                              ]
                            }
                          }
                        }
                      }
                    },
                    "rtp": {
                      "$id": "#/properties/pictures_sizes/properties/rtp",
                      
                      "title": "The Rtp Schema",
                      "required": [
                        "s1",
                        "s2",
                        "s3",
                        "s4",
                        "s5"
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/rtp/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/rtp/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                600
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/rtp/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                400
                              ]
                            }
                          }
                        },
                        "s2": {
                          "$id": "#/properties/pictures_sizes/properties/rtp/properties/s2",
                          
                          "title": "The S2 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/rtp/properties/s2/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                413
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/rtp/properties/s2/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                275
                              ]
                            }
                          }
                        },
                        "s3": {
                          "$id": "#/properties/pictures_sizes/properties/rtp/properties/s3",
                          
                          "title": "The S3 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/rtp/properties/s3/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/rtp/properties/s3/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                200
                              ]
                            }
                          }
                        },
                        "s4": {
                          "$id": "#/properties/pictures_sizes/properties/rtp/properties/s4",
                          
                          "title": "The S4 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/rtp/properties/s4/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                135
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/rtp/properties/s4/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                90
                              ]
                            }
                          }
                        },
                        "s5": {
                          "$id": "#/properties/pictures_sizes/properties/rtp/properties/s5",
                          
                          "title": "The S5 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/rtp/properties/s5/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                1060
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/rtp/properties/s5/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                707
                              ]
                            }
                          }
                        }
                      }
                    },
                    "mrtp": {
                      "$id": "#/properties/pictures_sizes/properties/mrtp",
                      
                      "title": "The Mrtp Schema",
                      "required": [
                        "s1",
                        "s2",
                        "s3",
                        "s4",
                        "s5"
                      ],
                      "properties": {
                        "s1": {
                          "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s1",
                          
                          "title": "The S1 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s1/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                600
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s1/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                400
                              ]
                            }
                          }
                        },
                        "s2": {
                          "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s2",
                          
                          "title": "The S2 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s2/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                413
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s2/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                275
                              ]
                            }
                          }
                        },
                        "s3": {
                          "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s3",
                          
                          "title": "The S3 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s3/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                300
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s3/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                200
                              ]
                            }
                          }
                        },
                        "s4": {
                          "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s4",
                          
                          "title": "The S4 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s4/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                135
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s4/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                90
                              ]
                            }
                          }
                        },
                        "s5": {
                          "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s5",
                          
                          "title": "The S5 Schema",
                          "required": [
                            "w",
                            "h"
                          ],
                          "properties": {
                            "w": {
                              "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s5/properties/w",
                              
                              "title": "The W Schema",
                              "default": 0,
                              "examples": [
                                1060
                              ]
                            },
                            "h": {
                              "$id": "#/properties/pictures_sizes/properties/mrtp/properties/s5/properties/h",
                              
                              "title": "The H Schema",
                              "default": 0,
                              "examples": [
                                707
                              ]
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "staticLinks": {
                  "$id": "#/properties/staticLinks",
                  
                  "title": "The Staticlinks Schema",
                  "required": [
                    "about",
                    "feedback",
                    "about_motorsport_network",
                    "terms_conditions",
                    "privacy_policy"
                  ],
                  "application_versions": {
                    "$id": "#/properties/application_versions",
                    
                    "title": "The Application_versions Schema",
                    "required": [
                      "ios_min_version",
                      "ios_next_min_version",
                      "android_min_version",
                      "android_next_min_version",
                      "current_backend_version"
                    ]
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
