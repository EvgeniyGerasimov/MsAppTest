ADMIN_MENU = {

    
    "required": [
        "data"
    ],
    "properties": {
        "data": {
            
            "items": {
                
                "required": [
                    "race_type_id",
                    "edp",
                    "category_edition",
                    "photos",

                ],
                "properties": {
                    "edp": {

                        

                        "required": [
                            "alias",
                            "activity",
                            "title",
                            "full_name",
                            "race_type_edition_id",
                            "edition_id"
                        ]
                    }
                }
            }
        }
    }
}