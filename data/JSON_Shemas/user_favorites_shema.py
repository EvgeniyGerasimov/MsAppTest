USER_FAVORITES = {
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "news": {
          "type": "array",
          "items": {}
        },
        "video": {
          "type": "array",
          "items": {}
        },
        "photo": {
          "type": "array",
          "items": {}
        },
        "event": {
          "type": "array",
          "items": {}
        },
        "topic": {
          "type": "array",
          "items": {}
        }
      },
      "required": [
        "news",
        "video",
        "photo",
        "event",
        "topic"
      ]
    }
  },
  "required": [
    "data"
  ]
}

