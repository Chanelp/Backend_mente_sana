class CustomException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
        self.message = args[0] or ''
        self.status_code = int(args[1]) or ''

        