VIDEO_LATEST_SHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",

    "properties": {
        "data": {

            "items": [
                {

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
                                "video_edition_id": {

                                },
                                "alias": {

                                },
                                "title": {

                                },
                                "description": {

                                },
                                "dt_created": {

                                },
                                "original_entity_id": {

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
                                "video_edition_id",
                                "alias",
                                "title",
                                "description",
                                "dt_created",
                                "original_entity_id",
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
                                        "event_edition_id": {

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

                            "items": {}
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
                        "sub_event"
                    ]
                }
            ]
        }
    },
    "required": [
        "data"
    ]
}

