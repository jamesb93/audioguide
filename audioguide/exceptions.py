from util import ladytext

class AudioGuideError(Exception):
    def __init__(self, error_type:str, error_data:str):
        super().__init__(
            ladytext(
                f'{error_type.upper()} ERROR: \033[1m"{error_data}"\033[0;0m'
            )
        )
