def validate_book_data(data: dict) -> bool:
    is_type = type(data["name"])==str and type(data["author"])==str and type(data["genre"])==str
    is_value = len(data["name"])>0 and len(data["author"])>0 and len(data["genre"])>0
    return is_type and is_value