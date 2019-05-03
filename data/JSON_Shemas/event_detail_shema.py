EVENT_DETAIL_SHEMA = {

    

    "required": [
        "data"
    ],
    "properties": {
        "data": {

            

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
            ],
            "properties": {
                "edp": {
                    "$id": "#/properties/data/properties/edp",
                    
                    "title": "The Edp Schema",
                    "required": [
                        "event_edition_id",
                        "event_id",
                        "title",
                        "alias",
                        "edition_id",
                        "creator_user_id",
                        "store_link",
                        "photos"
                    ],

                    "alternatives": {

                        

                        "items": {

                            

                            "required": [
                                "event_id",
                                "edp",
                                "race_type"
                            ],

                            "edp": {

                                

                                "required": [
                                    "alias",
                                    "event_edition_id",
                                    "edition_id"
                                ],

                                "race_type": {

                                    

                                    "required": [
                                        "edp"
                                    ],
                                    "properties": {
                                        "edp": {

                                            

                                            "required": [
                                                "alias"
                                            ],

                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "championship": {

                

                "required": [
                    "championship_id",
                    "race_type_id",
                    "year",
                    "title_year",
                    "race_type"
                ],

                "race_type": {

                    

                    "required": [
                        "race_type_id",
                        "edp",
                        "category_edition",
                        "photos",
                        "race_type_photos",
                        "canonical",
                        "alternatives",
                        "default_duration"
                    ],

                    "edp": {
                        "$id": "#/properties/data/properties/race_type/properties/edp",
                        
                        "title": "The Edp Schema",
                        "required": [
                            "race_type_edition_id",
                            "race_type_id",
                            "title",
                            "alias"
                        ],

                    },

                },
                "location": {
                    "$id": "#/properties/data/properties/location",
                    
                    "title": "The Location Schema",
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
                    ],

                }
            },
            "country": {
                "$id": "#/properties/data/properties/country",
                
                "title": "The Country Schema",
                "required": [
                    "country_id",
                    "lang_code",
                    "code",
                    "title"
                ],

            },
            "sub_event": {
                "$id": "#/properties/data/properties/sub_event",
                
                "title": "The Sub_event Schema",
                "items": {
                    "$id": "#/properties/data/properties/sub_event/items",
                    
                    "title": "The Items Schema",
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
                    ],

                    "edp": {
                        "$id": "#/properties/data/properties/sub_event/items/properties/edp",
                        
                        "title": "The Edp Schema",
                        "required": [
                            "sub_event_edition_id",
                            "sub_event_id",
                            "title",
                            "alias"
                        ],

                    }
                },

            },
            "race_type": {
                "$id": "#/properties/data/properties/sub_event/items/properties/race_type",
                
                "title": "The Race_type Schema",
                "required": [
                    "race_type_id",
                    "edp",
                    "category_edition",
                    "photos",
                    "race_type_photos",
                    "canonical",
                    "alternatives",
                    "default_duration"
                ],

                "edp": {
                    "$id": "#/properties/data/properties/sub_event/items/properties/race_type/properties/edp",
                    
                    "title": "The Edp Schema",
                    "required": [
                        "race_type_edition_id",
                        "race_type_id",
                        "alias"
                    ],

                }

            },
            "event": {
                "$id": "#/properties/data/properties/sub_event/items/properties/event",
                
                "title": "The Event Schema",
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
                ],
                "properties": {
                    "edp": {
                        "$id": "#/properties/data/properties/sub_event/items/properties/event/properties/edp",
                        
                        "title": "The Edp Schema",
                        "required": [
                            "event_edition_id",
                            "event_id",
                            "alias",
                            "photos"
                        ],

                    }
                },

            }
        }
    }
}
