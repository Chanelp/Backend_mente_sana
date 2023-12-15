class CustomException(Exception):
    def __init__(self, message:str, status_code:int, *args) -> None:
        super().__init__(*args)
        
        self.message:str = message or ''
        self.status_code:int = status_code or ''

        