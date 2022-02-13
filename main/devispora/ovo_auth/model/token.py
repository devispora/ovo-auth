

token_table_name = 'tokens'


class Token:

    def __init__(self, token_id: str, discord_id: str, groups: [str], extra_reps: [str] = None):
        self.token_id = token_id
        self.discord_id = discord_id
        self.groups = groups
        self.extra_reps = extra_reps

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        state = self.__dict__.copy()
        if not state['extra_reps']:
            del state['extra_reps']
        return state
